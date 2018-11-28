#include<iostream>
#include<vector>
using namespace std;

int t,c,d,n;
char com[100][100];
bool op[100][100];
vector<char> l;

bool IsOp(char b)
{
	for(int i=0;i<l.size();++i)
	{
		if(op[l[i]][b])
		{
			return true;
		}
	}
	return false;
}

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("B-small-attempt1.in","r",stdin);
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	for(int ca=1;ca<=t;++ca)
	{
		cin>>c;
		memset(com,0,sizeof(com));
		for(int i=0;i<c;++i)
		{
			getchar();
			char a,b,c;
			a=getchar();
			b=getchar();
			c=getchar();
			com[a][b]=c;
			com[b][a]=c;
		}

		cin>>d;
		memset(op,false,sizeof(op));
		for(int i=0;i<d;++i)
		{
			getchar();
			char a,b;
			a=getchar();
			b=getchar();
			op[a][b]=true;
			op[b][a]=true;
		}

		cin>>n;
		getchar();
		l.clear();
		for(int i=0;i<n;++i)
		{
			char a;
			a=getchar();
			l.push_back(a);
			
			if(l.size()>1)
			{
				char a,b;
				
				a=l[l.size()-1];
				b=l[l.size()-2];
				if(com[a][b]!=0)
				{
					l.pop_back();
					l.back()=com[a][b];
				}

				a=l[l.size()-1];
				if(IsOp(a))
				{
					l.clear();
				}
			}
		}

		printf("Case #%d: [",ca);
		for(int i=0;i<l.size();++i)
		{
			if(i>0)
			{
				cout<<", ";
			}
			cout<<l[i];
		}
		puts("]");
	}
	return 0;
}
