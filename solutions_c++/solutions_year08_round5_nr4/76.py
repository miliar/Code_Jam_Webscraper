#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <string.h>
using namespace std;
int T,nT;
int H,W,R;
int p[15][2];
int ans;
int up[15];
int cup;
bool cmpup(int a,int b)
{
	return p[a][0]<p[b][0];
}
int slots[51];
int PICK(int c,int a)
{
	long long d=1;
	int j;
	memset(slots,0,sizeof(slots));
	slots[0]=1;
	for (int i=1;i<=a;i++)
	{
		for (j=0;j<50;j++)
		{
			slots[j]=slots[j]*(c-a+i)+(slots[j-1]>>17);
			slots[j-1]&=(1<<17)-1;
		}
		for (j=50;j--;)
		{
			if (j) slots[j-1]+=(slots[j]%i)<<17;
			slots[j]/=i;
		}
		//d=d*(c-a+i)/i;
	}
	for (j=50;j--;)
		if (j) slots[j-1]+=(slots[j]%10007)<<17;
	return slots[0]%10007;
}
int main()
{
	freopen("C:\\test.in","r",stdin);
	FILE*f=fopen("C:\\test.out","w");
	scanf("%d",&T);
	nT=T;
	p[10][0]=p[10][1]=1;
	while (T--)
	{
		scanf("%d%d%d",&H,&W,&R);
		p[11][0]=H;
		p[11][1]=W;
		int i,j;
		for (i=0;i<R;i++)
			scanf("%d%d",&p[i][0],&p[i][1]);
		ans=0;
		int t=1<<R;
		for (i=0;i<t;i++)
		{
			cup=0;
			for (j=0;j<R;j++)
				if (i&(1<<j))
					up[cup++]=j;
			up[cup++]=10;
			up[cup++]=11;
			printf("%d\n",cup);
			sort(up,up+cup,cmpup);
			for (j=1;j<cup;j++)
				if (p[up[j-1]][1]>p[up[j]][1]||p[up[j-1]][0]>p[up[j]][0])
					goto broke;
			int k=1;
			double a,b,c,d;
			int _a,_b;
			for (j=1;j<cup;j++)
			{
				c=p[up[j]][0]-p[up[j-1]][0];
				d=p[up[j]][1]-p[up[j-1]][1];
				a=(2*c-d)/3;
				b=(2*d-c)/3;
				if (abs(a-floor(a))>1e-6||abs(b-floor(b))>1e-6||a<0||b<0)
					goto broke;
				_a=(int)a;
				_b=(int)b;
				k=(k*PICK(_a+_b,min(_a,_b)))%10007;
			}
			ans+=(cup&1)?-k:k;
			if (!i&&!ans)
				break;
broke:
			continue;
		}
		ans%=10007;
		if (ans<0) ans+=10007;
		printf("%d\n",T);
		fprintf(f,"Case #%d: %d\n",nT-T,ans);
	}
	fclose(f);
}