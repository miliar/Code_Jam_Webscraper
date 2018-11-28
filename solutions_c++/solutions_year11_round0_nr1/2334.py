#include <cstdio>
#include <cstring>
struct Step
{
	int s;
	int b;
};
#define RANGE 120
Step stepB[RANGE],stepO[RANGE];
char str[2];
int N;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,cnt = 1;
	scanf("%d",&t);
	while(t--)
	{
		int currentStep = 0,currentB = 1,currentO = 1;
		memset(stepB,1000,sizeof(stepB));
		memset(stepO,1000,sizeof(stepO));
		int sec = 0,o = 0,b = 0;
		scanf("%d",&N);
		for(int i = 0;i<N;++i)
		{
			int temp;
			scanf("%s%d",str,&temp);
			if(str[0] == 'O')
			{
				stepO[o].s = i;
				stepO[o++].b = temp;
			}
			else
			{
				stepB[b].s = i;
				stepB[b++].b = temp;
			}
		}
		int B = 0,O = 0,push = 0;
		while(true)
		{
			sec++;
			if((stepB[B].b != currentB))
			{
				currentB += (stepB[B].b > currentB?1:-1);
			}
			else if(stepB[B].b==currentB)
			{
				if(currentStep==stepB[B].s)
				{
					push = 1;
					B++;
				}
			}
			if((stepO[O].b != currentO))
			{
				currentO += (stepO[O].b > currentO?1:-1);
			}
			else if(stepO[O].b==currentO)
			{
				if(currentStep==stepO[O].s)
				{
					push = 1;
					O++;
				}
			}
			if(push)
			{
				currentStep++;
				push = 0;
			}
			if(O==o&&B==b)
				break;
		}
		printf("Case #%d: %d\n",cnt++,sec);
	}
	return 0;
}