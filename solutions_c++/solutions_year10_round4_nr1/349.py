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

int elegant[300][300];

int main(int argc, char* argv[])
{

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T; cin >> T;

	for(int t = 1; t <= T; ++t)
	{
		int K; cin >> K;

		VVI diamond(K, VI(K));
		for(int k = 0; k < K-1; ++k)
		{
			int i = k, j = 0;
			for(int m = 0; m <= k; ++m)
			{
				int d; cin >> d;
				diamond[i--][j++] = d;
			}
		}

		for(int k = 0; k < K; ++k)
		{
			int i = K-1, j = k;
			for(int m = 0; m < K-k; ++m)
			{
				int d; cin >> d;
				diamond[i--][j++] = d;
			}
		}


		int res = 0;
		bool elegant_found = false;

		for(int A = K; A <= 3*K+1 && !elegant_found; ++A)
		{
			for(int i = 0; i < A-K+1 && !elegant_found; ++i)
			{
				for(int j = 0; j < A-K+1 && !elegant_found; ++j)
				{
					memset(elegant, -1, sizeof(elegant));

					bool is_elegant = true;
					for(int ik = 0; ik < K && is_elegant; ++ik)
					{
						for(int jk = 0; jk < K && is_elegant; ++jk)
						{
							if (elegant[i+ik][j+jk] != -1 && elegant[i+ik][j+jk] != diamond[ik][jk])
								is_elegant = false;

							elegant[i+ik][j+jk] = diamond[ik][jk];

							// symm /

							if (elegant[A-1-(j+jk)][A-1-(i+ik)] != -1 && elegant[A-1-(j+jk)][A-1-(i+ik)] != diamond[ik][jk])
								is_elegant = false;

							elegant[A-1-(j+jk)][A-1-(i+ik)] = diamond[ik][jk];


							// symm \

							if (elegant[j+jk][i+ik] != -1 && elegant[j+jk][i+ik] != diamond[ik][jk])
								is_elegant = false;

							elegant[j+jk][i+ik] = diamond[ik][jk];


						}

					}
					

					if (is_elegant)
					{
						elegant_found = true;
						res = A*A-K*K;
					}
				}

			}

		}

		cerr << "Case #" << t << ": " << res << "\n";
		cout << "Case #" << t << ": " << res << "\n";

	}




	int Int;
	std::cin >> Int;
}
