#include <iostream>
using namespace std;
int a[10005];
int main()
{
	int txt,cas=1,n,i,low,high,j;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("2.txt","w",stdout);
	scanf("%d",&txt);
	while(txt--){
		scanf("%d%d%d",&n,&low,&high);
		for(i=0;i<n;++i){
			scanf("%d",&a[i]);
		}
		for(i=low;i<=high;++i){
			for(j=0;j<n&&(a[j]%i==0||i%a[j]==0);++j);
			if(j==n)break;
		}
		printf("Case #%d: ",cas++); 
		if(i<=high)
			printf("%d\n",i);
		else puts("NO");
	}
	return 0;
}