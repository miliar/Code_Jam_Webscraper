#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>

using namespace std;


int pos[101], who[101];
int T, P, N;
char R[3];
int lastP[2], lastT[2];
int main()
{
	freopen("A-large.out","w",stdout);
	freopen("A-large.in","r",stdin);
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++)
	{
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
		{
			scanf("%s", R);
			scanf("%d", &P);

			if (R[0] == 'O')
			{
				who[i] = 0;
			}
			else
			{
				who[i] = 1;
			}
			pos[i] = P;
		}

		lastP[0] = lastP[1] = 1;
		lastT[0] = lastT[1] = 0;

		int res = 0;
		for (int i = 0; i < N; i++)
		{
			int delta = max(0, abs(pos[i] - lastP[who[i]]) - res + lastT[who[i]]);
			res += delta + 1;
			lastT[who[i]] = res;
			lastP[who[i]] = pos[i];
		}
		printf("Case #%d: %d\n", cases, res);
	}
	
}