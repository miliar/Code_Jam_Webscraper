#include<stdio.h>
#include<math.h>
void solve()
{
	int n, steps, O=1, B=1, T=0, G=0;
	char bot[10], prev[10];
	scanf("%d\n", &n);

	scanf("%s %d", bot, &steps );
	G = T = steps;
	prev[0] = bot[0];
	if(bot[0] == 'B') B = steps;
	else O = steps;
	
	for(int i = 1; i < n; i++)
	{
		scanf("%s %d", bot, &steps );
		if( bot[0] == 'B' && bot[0] == prev[0] )
		{
			G += abs(B-steps) + 1;
			T += abs(B-steps) + 1;
			B = steps;
		}
		else if( bot[0] == 'O' && bot[0] == prev[0] )
		{
			G += abs(O-steps) + 1;
			T += abs(O-steps) + 1;
			O = steps;
		}
		else if( bot[0] == 'B' && bot[0] != prev[0] )
		{
			prev[0] = 'B';
			G = ( abs(B-steps) > G ) ?  abs(B-steps) - G + 1 : 1;
			T += G;
			B = steps;
		}
		else
		{
			prev[0] = 'O';
			G = ( abs(O-steps) > G ) ?  abs(O-steps) - G + 1 : 1;
			T += G;
			O = steps;
		}
	}
	printf("%d\n", T);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif

	int T;
	scanf("%d\n", &T);
	for(int i = 1; i <= T; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}

	return 0;

}
