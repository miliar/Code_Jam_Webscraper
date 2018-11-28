#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#define _clr(a,b) (memset((a),(b),sizeof((a))));
#define print(cas) printf("Case #%d: ",(cas)++); 
#define inf 1<<25;
using namespace std;
double a[205],ans[205];
double sum;
int main()
{
	int cas=1,txt,i,j,n,cnt;
	double minval=999999;
	freopen("1.in","r",stdin);
	freopen("3.txt","w",stdout);
	scanf("%d",&txt);
	while(txt--)
	{
		scanf("%d",&n);
		_clr(ans,0);
		sum=0;
		for(i=0;i<n;i++)
		{
			scanf("%lf",&a[i]);
			sum+=a[i];
		}
		double temp=sum*2/n;
		double sum1=0;
		cnt=0;
		for(i=0;i<n;i++)
		{
			if(a[i]>temp)ans[i]=1;
			else {sum1+=a[i];cnt++;}
		}
		sum1=(sum1+sum)/cnt;
		print(cas);
		for(i=0;i<n;i++)
		{
			if(i)printf(" ");
			if(ans[i])printf("%lf",ans[i]-1);
			else
				printf("%lf",100*(sum1-a[i])/sum);
		}
		printf("\n");
	}
	return 0;
}
