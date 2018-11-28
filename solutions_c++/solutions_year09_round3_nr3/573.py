#include<stdio.h>
#include<algorithm>
#include<string>
#include<math.h>

using namespace std;

int ans;
int in[10];
bool tag[103];
//int ji[10];

int n,m;
void DFS(int p)
{
	if(p==m)
	{
	    int now=0;
		int i,j;
        for(i=1;i<=n;i++)
			tag[i]=true;

		for(i=0;i<m;i++)
		{
		    for(j=in[i]-1;j>=1;j--)
			{
			   if(tag[j])
				   now++;
			   else
				   break;
			}
			for(j=in[i]+1;j<=n;j++)
			{
			    if(tag[j])
					now++;
				else
					break;
			}
			tag[in[i]]=false;
		}
	    if(now<ans)
			ans=now;
	}
    int i;
    for(i=p;i<m;i++)
	{
	    swap(in[i],in[p]);
		DFS(p+1);
		swap(in[i],in[p]);
	}
}
int main()
{
    freopen("C-small.in","r",stdin);
    freopen("C-small.out","w",stdout);
    int t;
	
	scanf("%d",&t);
	int i,j,k;
    
	for(k=1;k<=t;k++)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<m;i++)
		{
		    scanf("%d",&in[i]);
		}
		ans=1000000000;

	    DFS(0);
		printf("Case #%d: %d\n",k,ans);
	}
    
    return 0;
}