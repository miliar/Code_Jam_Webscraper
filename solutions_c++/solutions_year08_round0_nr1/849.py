#include<iostream>
#include<map>
#include<vector>
using namespace std;
int there[1001],s,q;;
void reset()
{
	memset(there,0,sizeof(there));
}
int count()
{
	int cnt=0;
	for(int i=0;i<s;i++)
		if(there[i]) cnt++;
	return cnt;
}
int main()
{
	int t,Case=1;
	cin>>t;
	
	while(t--)
	{
		char str[1000];
		cin>>s;
		map<string,int> M;
		vector<string> query;
		string temp,prev="";
		getchar();
		for(int i=0;i<s;i++)	
		{
			gets(str);			
			temp=str;
			M[temp]=i;
		}
		cin>>q;
		getchar();
		for(int i=0;i<q;i++)
		{
			gets(str);
			temp=str;
			if(temp==prev) continue;
			else
				query.push_back(temp);
			prev=temp;	
		}
		//calculate
		
		reset();
		int tcount=0;
		int scount=0;
		for(int i=0;i<query.size();i++)
		{
			int code=M[query[i]];
			//cout<<count()<<endl;
			if(count()==s-1 && !there[code])
			{
				scount++;
				reset();
				there[code]=1;
			}
			else
				there[code]=1;
		}
		//if(count()<=s-1) scount++;
		cout<<"Case #"<<Case++<<": "<<scount<<endl;
		
	}
	
}
