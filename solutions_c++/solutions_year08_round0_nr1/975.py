#include <iostream>
#include <string>
#include <memory>
using namespace std;

string en[200];
int dist[200];
string q[2000];
int ne,nq;
char s[2000];

int main()
{
	int t;
	freopen("A-large.in", "r", stdin);
	freopen("large.out", "w", stdout);
	
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		int i,j;
		cin>>ne;
		gets(s);
		for(i=0;i<ne;i++)
		{
			gets(s);
			en[i]=s;
		}
		cin>>nq;
		gets(s);
		for(i=0;i<nq;i++)
		{
			gets(s);
			q[i]=s;
		}
		int cur=0;
		int res = 0;
		while(cur < nq)
		{
			memset(dist,0x7f,sizeof(dist));
			for(i=0;i<ne;i++)
			{
				for(j=cur;j<nq;j++)
				{
					if(en[i] == q[j])
					{
						dist[i] = j;
						break;
					}
				}
				if(j==nq)
				{
					goto end;
				}
			}
			int dd = 0;
			for(i=0;i<ne;i++)
			{
				dd=max(dd,dist[i]);
			}
			res++;
			cur = dd;
		}
end:;
		printf("Case #%d: %d\n", tt, res);
	}
}