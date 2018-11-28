#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;

#define MAX 5000
#define MP 12

#define f1(a) (((a)<<1)+1)
#define f2(a) (((a)<<1)+2)

int pd[MAX][MP];
int calc[MAX][MP];
int c[MAX];

int func(int pos, int perdido)
{
	if(calc[pos][perdido])
		return pd[pos][perdido];
	int r1,r2;
	int res=-1;
	r1=func(f1(pos),perdido);
	r2=func(f2(pos),perdido);
	if(r1>=0 && r2>=0)
		res=c[pos]+r1+r2;
	r1=func(f1(pos),perdido+1);
	r2=func(f2(pos),perdido+1);
	if(r1>=0 && r2>=0 && r1+r2<res)
		res=r1+r2;
	calc[pos][perdido]=1;
	return pd[pos][perdido]=res;
}

int main()
{
	int t,ccnt;
	int p;
	int i,j;
	int lim;
	int pos;
	scanf("%d",&t);
	for(ccnt=1;ccnt<=t;++ccnt)
	{
		scanf("%d",&p);
		memset(calc,0,sizeof(calc));
		for(i=0;i<1<<p;++i)
		{
			scanf("%d",&lim);
			pos=(1<<p) -1 +i;
			for(j=0;j<=p;++j)
			{
				calc[pos][j]=1;
				pd[pos][j]=(j<=lim)?0:-1;
			}
		}
		for(j=p-1;j>=0;--j)
		{
			pos=(1<<j) -1;
			for(i=0;i<(1<<j);++i)
				scanf("%d",&c[pos+i]);
		}
		printf("Case #%d: %d\n",ccnt,func(0,0));
	}
	return 0;
}

