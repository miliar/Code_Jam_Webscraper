#include <iostream>
#include <algorithm>
using namespace std;

int cmp(int x,int y)
{
	if (x>y)
		return 1;
	else return 0;
}

int a[1010];

__int64 ans;


int main()
{
	int T,t,p,k,l;
	int i,j,time;

	freopen("A-large.out","w",stdout);
	freopen("A-large.in","r",stdin);

	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d%d%d",&p,&k,&l);
		for(i=0;i<l;i++){
			scanf("%d",&a[i]);
		}
		sort(a,a+l,cmp);
		
		ans=0;
		for(i=0;i<k;i++){
			time=1;
			for(j=i;j<l;j=j+k){
				ans+=a[j]*time;
				time++;
			}
		}
		printf("Case #%d: %I64d\n",t,ans);
	}
	return 0;
}
