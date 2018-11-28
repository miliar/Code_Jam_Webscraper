#include<stdio.h>

int p[2000];

int main()
{
	freopen("C-large.in", "r", stdin);
    freopen("sample.out", "w", stdout);

	int t,n;
	int i,j,k,m,mm,sum;
	scanf("%d",&t);
	for(i=0;i<t;i++){
		scanf("%d",&n);
		m=0;
		mm=10000000;
		sum=0;
		for(j=0;j<n;j++){
			scanf("%d",&p[j]);
			m=m^p[j];
			sum+=p[j];
			if(mm>p[j])mm=p[j];
		}
		if(m!=0)
			printf("Case #%d: NO\n",i+1);
		else{
			printf("Case #%d: %d\n",i+1,sum-mm);
		}
	}
}