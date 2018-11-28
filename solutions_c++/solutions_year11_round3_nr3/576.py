// Google Codejam
// May 22, 2011
// Author	::	MIB
// Problem	::	C


#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>


using namespace std;


const int MAX = 105;

int harmony[MAX];
int N, L, H;

int main(void)
{
	freopen ("C:\\Documents and Settings\\Mainul\\My Documents\\Downloads\\Codejam\\input\\C-small-attempt0.in", "rt", stdin);
	freopen ("C:\\Documents and Settings\\Mainul\\My Documents\\Downloads\\Codejam\\output\\C-small-attempt0.out", "wt", stdout);

	int t, T;
	int N, M;
	int i, j;
	bool yes;

	scanf(" %d",&T);
	
	for(t=1; t<=T; t++)
	{
		scanf(" %d %d %d", &N, &L, &H);

		for(i=0; i<N; i++)
		{
			scanf( " %d" ,&harmony[i]);
		}


		if(L == 1) {
			printf( "Case #%d: 1\n", t);
			continue;
		}

		yes = false;

		for(i=L; i<=H; i++)
		{
			for(j=0; j<N; j++)
			{
				if(i > harmony[j])
				{
					if(i % harmony[j] != 0)
						break;
				}

				else
				{
					if(harmony[j] % i != 0)
						break;
				}
			}

			if(j == N)
			{
				yes = true;
				break;
			}
		}

		if(yes)
			printf( "Case #%d: %d\n", t, i);
		else
			printf( "Case #%d: NO\n", t, i);
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
