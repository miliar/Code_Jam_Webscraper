#include <iostream>
#include <cmath>
using namespace std;
#define inf 999999
int a[1000];
int res,n;
void gao(int l,int ckl,int sss,int backmy,int nimeide)
{
	if(l==n){
		if(ckl==sss&&nimeide)if(backmy>res)res=backmy;
		return ;
	}
	gao(l+1,ckl^a[l],sss,backmy+a[l],nimeide);
	gao(l+1,ckl,sss^a[l],backmy,nimeide+1);
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int t,ttplayer=1;
	scanf("%d",&t);
	while(t--)
	{
		res=-inf;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%d",&a[i]);
		gao(0,0,0,0,0);
		printf("Case #%d: ",ttplayer++);
		if(res!=-inf)
			printf("%d\n",res);
		else
			printf("NO\n");
	}
	return 0;
}
