#include<iostream>

using namespace std;
int res[100] = {0,0,27};
void mult(int a[][2],int b[][2])
{
	int i,j,k,c[2][2]={0,0,0,0};
	for(i=0;i<2;i++)
		for(j=0;j<2;j++)
			for(k=0;k<2;k++)
				c[i][j] =(c[i][j]+a[i][k]*b[k][j])%1000;
	for(i=0;i<2;i++)
		for(j=0;j<2;j++)
			a[i][j] = c[i][j];
}
int fibo(__int64 n)
{
	int mat[2][2]={0,1,1,1};
	int res[2][2]={1,0,0,1};
	while(n)
	{
		if(n&1)
			mult(res,mat);
		mult(mat,mat);
		n>>=1;
	}
	return res[0][1];
}
int two(__int64 n)
{
	int res=1,t=2;
	while(n)
	{
		if(n&1)
			res = res*t%1000;
		t = (t*t)%1000;
		n>>=1;
	}
	return res;
}

int main()
{
	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
	int cas,ca=1;
	__int64 n;
	cin>>cas;
	while(cas--)
	{
		scanf("%I64d",&n);
		int a=fibo(2*n-1),b=fibo(2*n),t=two(n);
	//	cout<<a<<' '<<b<<' '<<t<<endl;
		printf("Case #%d: %03d\n",ca++,(t*2*a+t*b+999)%1000);
	}
}

	