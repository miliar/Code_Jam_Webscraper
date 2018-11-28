#include <iostream>
using namespace std;
int main()
{
	int t,c,d,n;
	char com[4],opp[3],inputc[200],res[200];
	int a1,a2,a3,cnt;
	int to[26][26],op[26];
	int era[26];
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		memset(to,-1,sizeof(to));
		memset(op,-1,sizeof(op));
		memset(era,0,sizeof(era));
		cnt=-1;
		cin>>c;
		for (int j=0;j<c;j++)
		{
			cin>>com;
			a1=com[0]-'A';
			a2=com[1]-'A';
			a3=com[2]-'A';
			to[a1][a2]=to[a2][a1]=a3;
		}
		cin>>d;
		for (int j=0;j<d;j++)
		{
			cin>>opp;
			a1=opp[0]-'A';
			a2=opp[1]-'A';
			op[a1]=a2;
			op[a2]=a1;
		}
		cin>>n;
		cin>>inputc;
		res[++cnt]=inputc[cnt];
		a1=inputc[cnt]-'A';
		if (op[a1]!=-1)
			era[op[a1]]=1;
		for (int j=1;j<n;j++)
		{
			if (cnt==-1)
			{
				a2=inputc[j]-'A';				
				res[++cnt]=a2+'A';
				if (op[a2]!=-1)
					era[op[a2]]++;
			}
			else
			{
				a1=res[cnt]-'A';
				a2=inputc[j]-'A';
				if (to[a1][a2]!=-1)
				{
					res[cnt]=to[a1][a2]+'A';
					if (op[a1]!=-1)
						era[op[a1]]--;
				}
				else if (era[a2])
				{
					cnt=-1;
					memset(era,0,sizeof(era));
				}
				else 
				{
					res[++cnt]=a2+'A';
					if (op[a2]!=-1)
						era[op[a2]]++;
				}
			}

		}
		bool comma=0;
		cout<<"Case #"<<i<<": [";
		for (int j=0;j<=cnt;j++)
		{
			if (comma)
				cout<<", ";
			cout<<res[j];
			comma=1;
		}
		cout<<"]"<<endl;
	}
	return 0;
}