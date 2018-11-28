#include <stdio.h>
#include <conio.h>

int main()
 {
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
    
	int nn;
	scanf("%d",&nn);

	for(int ni=0;ni<nn;ni++)
{
	printf("Case #%d: ",ni+1);
	int n;
	int a[10001];
	long long l,h;
	long long answer=0;
	scanf("%d %lld %lld",&n,&l,&h);
	for(int i=0;i<n;i++)
		scanf("%d ",&a[i]);
	for(long long i=l;i<=h;i++)
	{
		bool ok=true;

		for(int ii=0;ii<n;ii++)
		{
			if(a[ii]%i!=0&&i%a[ii]!=0) ok=false;
			if(!ok) break;
		}
		if(ok) {answer=i; break;}
	}
	
	if(answer==0) printf("NO\n"); else printf("%lld\n",answer);
}
	return 0;
 }