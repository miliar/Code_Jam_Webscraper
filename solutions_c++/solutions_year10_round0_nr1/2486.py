#include <stdio.h>
#include <memory>

int a[31];

int main()
{
	//freopen("z:\\a.txt","w",stdout);
	//freopen("z:\\A-small-attempt3.in","r",stdin);
	int c,i,k,n;
	scanf("%d",&c);
	for(i=1;i<=30;++i) a[i]=2*a[i-1]+1;
	for(i=1;i<=c;++i){
		scanf("%d%d",&n,&k);
		if(k%(1+a[n])!=a[n]) printf("Case #%d: OFF\n",i);
		else printf("Case #%d: ON\n",i);

	}
	return 0;
}