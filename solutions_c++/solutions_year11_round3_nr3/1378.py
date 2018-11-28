#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

const int N=10000+10;

int main()
{
	freopen("C-small-attempt0(1).in","r",stdin); 
	freopen("zx.out","w",stdout);
	int ncase,nnum,low,high,arr[N];
	scanf("%d",&ncase);
	for(int ii=1;ii<=ncase;ii++)
	{
		printf("Case #%d: ",ii);
		bool flag=false;
		scanf("%d%d%d",&nnum,&low,&high);
		for(int i=1;i<=nnum;i++) scanf("%d",&arr[i]);
		for(int i=low;i<=high;i++)
		{
			int ans=0;
			for(int j=1;j<=nnum;j++)
			{
				if(i%arr[j]==0 || arr[j]%i==0) ans++;
				else break;
			}
			if(ans==nnum)
			{
				flag=true;
				printf("%d\n",i);
			}
			if(flag) break;
		}
		if(!flag) printf("NO\n");
	}
	return 0;
}
