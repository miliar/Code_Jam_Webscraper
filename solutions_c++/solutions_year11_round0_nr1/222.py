#include <cstdio>
int O,B;
int N;

inline int abs(int a)
{
	return a>0?a:-a;
}

inline void Readin()
{
	scanf("%d",&N);
}

inline void Solve()
{
	O=B=1;
	int delayO=0,delayB=0,tm=0;
	for (int i=1;i<=N;++i)
	{
		char s[10];
		int x;
		scanf("%s%d",s,&x);
		
		if (s[0]=='O')
		{
			if (delayO >= abs(x-O))
			{
				tm += 1;
				delayB += 1;
				O=x;
			}
			else{
				tm += abs(x-O) +1 -delayO;
				delayB += abs(x-O) + 1- delayO;
				O = x;
			}
			delayO = 0;
		}
		else{
			if (delayB >= abs(x-B))
			{
				tm += 1;
				delayO += 1;
				B=x;
			}
			else{
				tm += abs(x-B) +1 -delayB;
				delayO += abs(x-B) + 1- delayB;
				B = x;
			}
			delayB =0 ;
		}
	}
	
	printf("%d\n",tm);
}

int main()
{
	//freopen("i.txt","r",stdin);
	int Test,Case=0;
	
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	
	return 0;
}
