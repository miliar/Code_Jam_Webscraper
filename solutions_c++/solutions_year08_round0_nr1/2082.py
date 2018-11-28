#include<iostream>
#include<string>
using namespace std;

int v[101],s;
char ch[101][1001];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int N,i,j,t=1,count,Q;
	char q[100];
	cin>>N;
	while(N--)
	{
		cin>>s;
		getchar();
		for(i=0;i<s;i++)
			gets(ch[i]);
		cin>>Q;
		getchar();
		count=0;
		memset(v,0,sizeof(v));
		int ans=0;
		for(i=0;i<Q;i++)
		{
			gets(q);
			for(j=0;j<s;j++)
			{
				if(strcmp(q,ch[j])==0)
				{
					if(v[j]==0)
					{
					count++;
					v[j]=1;
					}
							
						
					
				if(count==s)
					{
						ans++;
						memset(v,0,sizeof(v));
						v[j]=1;
						count=1;
					}
				break;
				}
			}

		}
		cout<<"Case #"<<t++<<": "<<ans<<endl;
	}



return 0;
}