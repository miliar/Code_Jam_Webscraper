#define _CRT_RAND_S

#include <stdlib.h>
#include <stdio.h>
#include <time.h>


#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <bitset>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <map>
#include <set>

using namespace std;

typedef istringstream ISS;
typedef ostringstream OSS;
#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
typedef VT<VD> VVD;
typedef pair<int,int> PII;

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define FOR(i,a,b) for(int i=(int)a;i<=(int)b;++i)
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define MP make_pair

const int MAX_LENGTH = 100;

int main(int argc, char* argv[])
{

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T; cin >> T;


	for(int t = 1; t <= T; ++t)
	{
		int C; cin >> C;

		VVI f(MAX_LENGTH+1,VI(MAX_LENGTH+1));
		VVI f_next(MAX_LENGTH+1,VI(MAX_LENGTH+1));

		for(int c = 0; c < C; ++c)
		{
			int x1,y1,x2,y2;
			cin>>x1>>y1>>x2>>y2;
			for(int i = x1; i <= x2; ++i)
				for(int j = y1; j <= y2; ++j)
					f[i][j] = 1;
		}

		bool dead = 0;
		int s=0;
		for(;!dead; ++s)
		{
			bool has_alive = 0;
			for(int i = 0; i <= MAX_LENGTH; ++i)
			{
				for(int j = 0; j <= MAX_LENGTH; ++j)
				{
					f_next[i][j] = f[i][j];
					if (f_next[i][j])
					{
						if ((!i || f[i-1][j] == 0) && (!j || f[i][j-1] == 0))
							f_next[i][j] = 0;
					}
					else
					{
						if ((i && f[i-1][j] == 1) && (j && f[i][j-1] == 1))
							f_next[i][j] = 1;
					}

					if (f_next[i][j])
						has_alive = 1;
				}

			}

			if (!has_alive)
				dead = true;

			swap(f, f_next);

		}


		cerr << "Case #" << t << ": " << s << "\n";
		cout << "Case #" << t << ": " << s << "\n";

	}




	int Int;
	std::cin >> Int;
}
