#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <bitset>
#include <string.h>
using namespace std;

int R, C, D;
vector<vector<char>> weight;

void readCase()
{
	scanf("%d %d %d", &R, &C, &D);
	weight.resize( R );
	for(int i = 0; i < R; i++) 
	{
		weight[i].resize(C);
		static char buf[1000];
		scanf("%s\n", buf);
		for(int j = 0; j < C; j++) 
			weight[i][j] = ( buf[j] - '0' );
	}
}

void solve()
{
	for(int K = max(C, R); K >= 3; K--)
		for(int x = 0; x < R - K + 1; x++)
			for(int y = 0; y < C - K + 1; y++)
			{
				double xc = x + K / 2.;
				double yc = y + K / 2.;
				double ccx = 0;
				double ccy = 0;
				for(int i = 0; i < K; i++ )
					for(int j = 0; j < K; j++ )
					{
						ccx += (x + i - xc + 0.5) * weight[x+i][y+j];
						ccy += (y + j - yc + 0.5) * weight[x+i][y+j];
					}
				{
					int i = 0, j = 0;
					ccx -= (x + i - xc + 0.5) * weight[x+i][y+j];
					ccy -= (y + j - yc + 0.5) * weight[x+i][y+j];						
				}
				{
					int i = 0, j = K-1;
					ccx -= (x + i - xc + 0.5) * weight[x+i][y+j];
					ccy -= (y + j - yc + 0.5) * weight[x+i][y+j];						
				}
				{
					int i = K-1, j = 0;
					ccx -= (x + i - xc + 0.5) * weight[x+i][y+j];
					ccy -= (y + j - yc + 0.5) * weight[x+i][y+j];						
				}
				{
					int i = K-1, j = K-1;
					ccx -= (x + i - xc + 0.5) * weight[x+i][y+j];
					ccy -= (y + j - yc + 0.5) * weight[x+i][y+j];						
				}
				

				if( abs(ccx) < 1e-6 && abs(ccy) < 1e-6 ) 
				{
					printf("%d", K);
					return;
				}
			}

	printf("IMPOSSIBLE", time);
}

int main()
{
	//string fname = "./test/B-example.in";
	string fname = "./test/B-small-attempt0.in";
	//string fname = "./test/B-large.in";
	
	freopen(fname.c_str(),"r",stdin);freopen((fname+".out").c_str(),"w",stdout);

	int analizeCase = -1;
	
	int T;
	scanf("%d", &T);
	for(int tCase = 1; tCase <= T; tCase++) {
		printf("Case #%d: ", tCase);
		readCase();
		if(analizeCase < 0 || analizeCase == tCase) solve();
		printf("\n");
		fflush(stdout);
		fprintf(stderr, "Done %d %%     \r", 100 * tCase / T );
	}
	return 0;
}

