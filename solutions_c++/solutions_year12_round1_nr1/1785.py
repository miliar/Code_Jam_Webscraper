#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
int main()
{
	long long int i,j,ca=0,k,l,a,b,t;
	double temp,qq; 
	scanf("%lld",&t);
	while(t--)
	{	
		ca++;
		double arr[1007]={0.0},brr[1007]={0.0},crr[1007]={0.0};
		scanf("%lld %lld",&a,&b);
		brr[0]=1.0;
		temp=b+2.0;
		for(i=1;i<=a;i++)
		{
			scanf("%lf",&arr[i]);
			brr[i]=brr[i-1]*arr[i];
		}
		crr[a+1]=brr[a]*(b-a+1.0)+(1.0-brr[a])*(b-a+2.0+b);
		for(i=0;i<=a;i++)
		{
			crr[i]=brr[i]*(a+b+1-2.0*i)+(1.0-brr[i])*(a+2*b+2.0-2.0*i);
			temp=temp<crr[i]?temp:crr[i];
		}
		printf("Case #%lld: %lf\n",ca,temp);
	}
	return 0;
}