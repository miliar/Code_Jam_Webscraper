#include<iostream>
using namespace std;
float f[100000];
void solve(int A,int B)
{
	float tmp=1.0;
	float ans=A+B+1;
	double cur=0.0;
	for(int i=0;i<A-1;i++)
	{
		scanf("%f",&f[i]);
		tmp=tmp*f[i];
		cur=(tmp*(A+B-2*i-1))+((1-tmp)*(2*B+A-2*i));
		if(tmp*(A+B-2*i-1)+(1-tmp)*(2*B+A-2*i)<ans)
			ans=tmp*(A+B-2*i-1)+(1-tmp)*(2*B+A-2*i);
		
	}
	scanf("%f",&f[A-1]);
	tmp=tmp*f[A-1];
	cur=(B-A+1)*tmp+(2*B-A+2)*(1-tmp);
	if((B-A+1)*tmp+(2*B-A+2)*(1-tmp)<ans)
		ans=(B-A+1)*tmp+(2*B-A+2)*(1-tmp);
	if(B+2<ans)ans=B+2;
	printf("%.6f\n",ans);
	
	
}
int main()
{
	int T;
	int A,B;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		scanf("%d%d",&A,&B);
		solve(A,B);
	}
	return 0;
}