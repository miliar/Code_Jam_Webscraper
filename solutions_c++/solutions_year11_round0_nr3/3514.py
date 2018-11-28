#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

#define read freopen("C-large.in","r",stdin)
#define write freopen("zx.out","w",stdout)
const int MAXN=1000+10;

int main()
{
	read, write;
	int ncase,nnum;
	int zx[MAXN];
	scanf("%d",&ncase);
	for(int ii=1;ii<=ncase;ii++)
	{
		scanf("%d",&nnum);
		for(int i=0;i<nnum;i++) scanf("%d",&zx[i]);
		sort(zx,zx+nnum);
		int result=-1;
		int maxsum=0,sum1=0,sum2=0;
		for(int j=nnum-1;j>=1;j--)
		{
			maxsum+=zx[j];
			sum1^=zx[j];
			for(int t=0;t<j;t++) sum2^=zx[t];
			if(sum1==sum2)
			{
				if(result<maxsum) result=maxsum;
			}
			sum2=0;
		}
		if(result!=-1) printf("Case #%d: %d\n",ii,result);
		else printf("Case #%d: NO\n",ii);
	}
	return 0;
}
