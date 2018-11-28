#include <cstdio>
#include <cstdlib>
#include <cstring>
#define MAX 50
int gcd(int a,int b)
{
	while(b)
	{
		const int tmp=a%b;
		a=b;
		b=tmp;
	}
	return a;
}
bool valid[20000];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int nT,t=0;
	scanf("%d",&nT);
	while(nT--)
	{
		memset(valid,1,sizeof(valid));
		int n,low,high;
		scanf("%d%d%d",&n,&low,&high);
		int gg=0;
		for(int i=0;i<n;++i)
		{
			int tmp;
			scanf("%d",&tmp);
			for(int j=0;j<high-low+1;++j)
			{
				if(valid[j])
				{
					if(tmp % (j+low)!=0 && (j+low) % tmp!=0)
						valid[j]=false;
				}
			}
		}
		printf("Case #%d: ",++t);
		bool ok=false;
		for(int i=0;i<high-low+1;++i)
		{
			if(valid[i])
			{
				printf("%d\n",low+i);
				ok=true;
				break;	
			}	
		}
		if(!ok)
			puts("NO");
	}
}
