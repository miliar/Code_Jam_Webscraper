using namespace std;
#include<cstdio>
#include<algorithm>
#include<cstring>
const int MAX_N = 107;
int P[MAX_N];
char C[MAX_N];
int nexto[MAX_N], nextb[MAX_N];
int main()
{
	freopen("file.in","r",stdin);    freopen("file.out","w", stdout);
	int N, i, B = 1, O = 1, sol = 0;
	int T;
	scanf("%d\n", &T);
	for(int j = 1;j <= T;++j)
	{
		scanf("%d\n", &N);
		for(i = 1; i <= N; ++i )
		{
		 //   char c; int p;
			scanf("%c %d ", &C[i], &P[i]);
		 //   if( C[i] == 'O' ) { nexto[anto] = i; anto = i; nextb[i] = nextb[i-1]; }
		  //  else { nextb[antb] = i; antb = i; nexto[i] = nexto[i-1]; }
		}
		sol = 0;
		B = O = 0;
		memset( nexto, 0, sizeof( nexto ));
		memset( nextb, 0, sizeof( nextb ));
		for(i = N; i; --i)
		{
			nexto[i] = O;
			nextb[i] = B;
			if(C[i] == 'O' )
			{
				O = i;
			}
			else B = i;
		}
		B = O = 1;
		for(i = 1; i <= N; ++i)
		{
			if( C[i] == 'O' )
			{
				sol += 1 + abs( O - P[i] );
                if( nextb[i] )
				{
			//		printf("( %d %d )", P[nextb[i]] - B, 1 + abs( O - P[i] ));
					if( B < P[nextb[i]] ) B += min( P[nextb[i]] - B, 1 + abs( O - P[i] ) );
					else if( B > P[nextb[i]] ) B -= min( B - P[nextb[i]], 1 + abs( O - P[i] ));
				
				}
				O = P[i];
			}
			else 
			{
                sol += 1 + abs( B - P[i] );
				if( nexto[i] )
				{
					if( O < P[nexto[i]] ) O += min( P[nexto[i]] - O , 1 + abs( B - P[i] ));
					else if( O > P[nexto[i]] ) O -= min( O - P[nexto[i]], 1 + abs( B - P[i] ));
				}
				B = P[i];
			}
	//		printf("%d\n",sol);
		}
	printf("Case #%d: %d\n",j, sol );			
	}
	return 0;
}

