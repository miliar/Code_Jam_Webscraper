/* Tomasz [Tommalla] Zakrzewski, Google Code Jam 2010, Round 1 /
/  Sub-Round B, Task 'File Fix-It' */
#include <iostream>
#include <string>
#include <map>

#define SIZE 1000000

using namespace std;

class CNode
{
    public:
	map<string,unsigned int> sasiedzi;
};

CNode nodes[SIZE];

int main()
{
    unsigned int n,m,t,j,i,k,ptr,result,id=0;
    cin>>t;
    string temp,dir,last;
//     ios_base::sync_with_stdio(0);
    for(j=1;j<=t;++j)
    {
	result=0;
	while(id--)
	    nodes[id].sasiedzi.clear();
	id=1;
	cin>>n>>m;
// 	mapa["/"]=0;
	while(n--)
	{
	    cin>>dir;
	    temp.clear();
	    ptr=0;
	    for(i=1,k=dir.size();i<k;++i)
		if(dir[i]!='/')
		    temp.push_back(dir[i]);
		else
		{
		    if(nodes[ptr].sasiedzi[temp]==0)
		    {
// 			cout<<ptr<<" sasiaduje z "<<temp<<endl;
			ptr=nodes[ptr].sasiedzi[temp]=id++;
// 			cout<<temp<<" otrzymało numer "<<ptr<<endl;
		    }
		    else
			ptr=nodes[ptr].sasiedzi[temp];
		    temp.clear();
// 		    nodes[id-1].sasiedzi.push_back(id);
		}
	    if(nodes[ptr].sasiedzi[temp]==0)
	    {
		nodes[ptr].sasiedzi[temp]=id++;
// 		cout<<temp<<" otrzymało numer "<<id-1<<endl;
// 		cout<<ptr<<" sasiaduje z "<<temp<<endl;
	    }
	}
	
	while(m--)
	{
	    cin>>dir;
	    temp.clear();
	    last="/";
	    ptr=0;
	    for(i=1,k=dir.size();i<k;++i)
		if(dir[i]!='/')
		    temp.push_back(dir[i]);
		else
		{
		    if(nodes[ptr].sasiedzi[temp]==0)
		    {
// 			cout<<temp<<" nie jest sąsiadem "<<ptr<<endl;
			++result;
			ptr=nodes[ptr].sasiedzi[temp]=id++;
		    }
		    else
			ptr=nodes[ptr].sasiedzi[temp];
		    temp.clear();
		}
		
	    if(nodes[ptr].sasiedzi[temp]==0)
	    {
// 		cout<<temp<<" nie jest sąsiadem "<<ptr<<endl;
		++result;
		nodes[ptr].sasiedzi[temp]=id++;
	    }
	}
	cout<<"Case #"<<j<<": "<<result<<"\n"; //%u: %u\n",j,result);
    }
    return 0;
}
