#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	int tt = T;
	while(T--)
	{
		int N, S, p, ret=0;
		scanf("%d %d %d", &N, &S, &p);
		int t[N], trip[N][3];
		for(int i=0; i<N; ++i)
		{
			scanf("%d", &t[i]);
			trip[i][0] = trip[i][1] = trip[i][2] = t[i] / 3;
			if(t[i] % 3 == 1)
				++trip[i][0];
			else if(t[i] % 3 == 2)
			{
				++trip[i][0];
				++trip[i][1];
			}

			if(S != 0 && trip[i][0] == p - 1)
			{
				if(trip[i][0] == trip[i][1] && trip[i][1] > 0)
				{
					++trip[i][0];
					--trip[i][1];
				}
				if(trip[i][0] >= p)
					--S;
			}
			if(trip[i][0] >= p)
				++ret;
		}
		cout<<"Case #"<<tt-T<<": "<<ret<<endl;
	}
	
	return 0;
}
