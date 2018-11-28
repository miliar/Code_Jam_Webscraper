#include <cstdio>
int main()
{
	long long int gr[2001];
	long long int dokad[1001];
	long long int koszt[1001];
	long long int t,r,n,k,l,i,j,cykl_num,cykl_koszt,cykl_ilosc_przejazdow;
	long long int d;
	scanf("%lld", &t);
	for(l=1;l<=t;l++)
	{
		scanf("%lld %lld %lld", &r, &k, &n);
		for(j=1;j<=n;j++) 
		{
			dokad[j]=0;
			koszt[j]=0;
			scanf("%lld", &i);
			gr[j]=gr[j+n]=i;
		}
		i=1;
		while(dokad[i]==0)
		{
			d=0;
			for(j=0; j<n ;j++)
			{
				if(koszt[i]+gr[i+j]>k) break;
				koszt[i]+=gr[i+j];
				d++;				
			}
			dokad[i]=i+d;
			if(dokad[i]>n) dokad[i]-=n;
			i=dokad[i];
		}
		cykl_num=i;
		cykl_ilosc_przejazdow=0;
		cykl_koszt=0;
		while(true)
		{
			cykl_koszt+=koszt[i];
			i=dokad[i];
			cykl_ilosc_przejazdow++;
			if(cykl_num==i) break;
		}
		d=0;
		i=1;
		while(r>0)
		{
			if(i==cykl_num)
			{
				j=r/cykl_ilosc_przejazdow;
				r%=cykl_ilosc_przejazdow;
				d+=cykl_koszt*j;
			}
			if(r==0) break;
			d+=koszt[i];
			i=dokad[i];
			r--;				
		}
		printf("Case #%lld: ",l);
		printf("%lld\n", d);
	}	
	return 0;
}
