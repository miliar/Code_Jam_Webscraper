#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cstring>
#include <boost/foreach.hpp>

using namespace std;
using namespace boost;

int MAP[100][100];

int main()
{
	int caseN;
	int W, H, R, a, b;
	scanf("%d", &caseN);
	for(int cc=0; cc<caseN;cc++){
		scanf("%d%d%d", &H, &W, &R);
		memset( MAP, 0, sizeof(MAP));
		for(int i=0;i<R;i++){
			scanf("%d%d", &a, &b);
			MAP[a-1][b-1] = -1;
		}
		MAP[0][0] = 1;
		for(int i=0;i<H;i++){
			for(int j=0;j<W;j++){
				if(MAP[i][j] == -1)
					continue;
				if( i-2 >= 0 && j - 1 >=0 && MAP[i-2][j-1] != -1)
					MAP[i][j] += MAP[i-2][j-1];
				if( i-1 >= 0 && j - 2 >=0 && MAP[i-1][j-2] != -1)
					MAP[i][j] += MAP[i-1][j-2];
				MAP[i][j] %= 10007;
			}
		}
		printf("Case #%d: %d\n", cc+1, MAP[H-1][W-1]);
	}
	return 0;
}
