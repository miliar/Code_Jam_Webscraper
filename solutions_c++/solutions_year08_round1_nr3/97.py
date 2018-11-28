#include<stdio.h>
#include<string.h>

const int fibtable[2][2]=
{
	{0,1},
	{1,1}
};

int d[2][2];
int a[2][2];
int b[2][2];
int t[2][2];
int n;

void mul(int ans[2][2],int a[2][2],int b[2][2])
{
	memset(ans,0,sizeof(int)*4);
	for(int i=0;i<2;i++)
		for(int j=0;j<2;j++)
			for(int k=0;k<2;k++)
			{
				ans[i][j] += a[i][k] * b[k][j];
				ans[i][j] %= 1000;
			}
}

int F(int n)
{
	memcpy(a,d,sizeof(d));
	memcpy(b,d,sizeof(d));
	while(n)
	{
		if(n&1)
		{
			mul(t,b,a);
			memcpy(b,t,sizeof(t));
		}
		mul(t,a,a);
		memcpy(a,t,sizeof(t));
		n /= 2;
	}
	return b[0][0];
}

int T(int n)
{
	int ret = 1;
	int tmp = 2;
	while(n)
	{
		if(n&1) ret = (ret * tmp) % 1000; 
		tmp = (tmp * tmp) % 1000;
		n /= 2;
	}
	return ret;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int ntest;
	scanf("%d",&ntest);
	for(int test=1;test<=ntest;test++)
	{
		scanf("%d",&n);
		memcpy(d,fibtable,sizeof(fibtable));
		int fib = F(n);
		int pow = T(n);
		printf("Case #%d: %03d\n",test,((5*fib*fib%1000+(n%2==0?2:-2))*pow+999)%1000);
	}
	return 0;
}
