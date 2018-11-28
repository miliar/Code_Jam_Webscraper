#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

#define minn(a,b) (a>b?b:a)
#define maxx(a,b) (a>b?a:b)
#define abss(a) ((a)>0?(a):-(a))
#define swap(a,b) a=a^b,b=a^b,a=a^b
#define cls(a) memset(a,0,sizeof(a))
#define INF 0x1f1f1f

float p[100010];
float ans;

int main()
{
//	freopen("1.txt","r",stdin);
//	freopen("2.txt","w",stdout);
	int T;
	int i,j;
	int A,B;
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
	{
		scanf("%d%d",&A,&B);
		ans=1;
		for (i=0;i<A;i++)
		{
			scanf("%f",&p[i]);
			ans=ans*p[i];
		}
		ans=ans*(B-A+1)+(1-ans)*(B-A+2+B);
		if (B+2<ans)
			ans=B+2;
		float P=1,tmp;
		for (i=0;i<A;i++)
		{
			tmp=(A-i+B-i+1)*P+(1-P)*(A-i+B-i+2+B);
			if (tmp<ans)
				ans=tmp;
			P=P*p[i];
		}
		printf("Case #%d: %f\n",t,ans);
	}

	return 0;
}