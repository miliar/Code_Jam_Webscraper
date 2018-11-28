#include <iostream>
#include <string>

using namespace std;

class Eng
{
	public:
	string str;
	int id;
}eng[101];

int t,s,q;

int A[101][1001];
char name[101][101];

int get_id()
{
	int u;
	for(u=0;u<s;u++)
	if(name[0]==eng[u].str)
	return u;
	 return -1;
}

int main()
{	
	int u,i,temp_id,e,z;
	cin >> t;
	for(u=0;u<t;u++)
	{
		cin >> s;
		cin.getline(name[0],1,'\n');
		for(i=0;i<s;i++)
		{
			cin.getline(name[i],101,'\n');
		 	eng[i].str=name[i];
		  	eng[i].id=i;
		  	//cout << eng[i].str << " " << eng[i].id << "\n";
		  	A[i][0]=0;
		 }
		 
		 cin >> q;
		 cin.getline(name[0],1,'\n');
		 for(i=1;i<=q;i++)
		 {
		 	cin.getline(name[0],101,'\n');
		 	temp_id=get_id();
		 	//cout << name[0] << " "  << temp_id  << "\n";
		 	
		 	//cout << i << ": ";
		 	for(e=0;e<s;e++)
		 	{
		 		if(e==temp_id) {A[e][i]=-1;continue;}
		 		
		 		A[e][i]=999999;
		 		for(z=0;z<s;z++)
		 		if(A[z][i-1]!=-1 && z!=e)
		 		A[e][i]=min(A[e][i],A[z][i-1]+1);		 	
		 		
		 		if(A[e][i-1]!=-1) A[e][i]=min(A[e][i],A[e][i-1]);
		 		//cout << e << ":" << A[e][i] << " ";
		 	}
		 	//cout << "\n";
		 }	
		 
		 e=999999;
		 for(i=0;i<s;i++)
		 if(A[i][q]!=-1)
		 e=min(e,A[i][q]);
		 cout << "Case #" << (u+1) << ": "  << e << "\n";
	
	}
	return 0;
}
