#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>


/*
#include <cstdio>
#include <cstdlib>
#include <bitset>
#include <deque>
#include <queue>
#include <stack>
#include <valarray>
#include <vector>
#include <list>
#include <set> //set - multiset
#include <map> //map - multimap

#include <algorithm>
#include <functional>
#include <math.h>
#include <complex>
#include <numeric>
#include <limits>
#include <memory>
#include <utility>

#include <iomanip>
/**/
#define FOR(i, m, n) for (int i(m), _n(n); i<_n; ++i)
#define FORd(i, m, n) for (int i=(m), _n=(n); i>_n; --i)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

using namespace std;

int main(int argc, char *argv[])
{
	int T,H,W;
	unsigned int M [102][102];
	short int dH [102][102];
	short int dW [102][102];
	char R [102][102];
	vector < pair < unsigned short int, unsigned short int > > q;
	q.reserve(10204);
	cin >> T;
	FOR(i,0,T)
	{
		cin >> H >> W;
		FOR(h,1,H+1)
		{
			FOR(w,1,W+1)
				cin >> M[h][w];
			M[h][0] = M[h][1];
			M[h][W+1] = M[h][W];
		}
		FOR(w,1,W+1)
		{
			M[0][w] = M[1][w];
			M[H+1][w] = M[H][w];
		}

		FOR(h,1,H+1)
			FOR(w,1,W+1)
			{
				R[h][w] = 0;
				int mn = min ( min ( M[h][w-1] , M[h-1][w] ) , min ( M[h][w+1] , M[h+1][w] ) );
				if (mn >= M[h][w])
					dH[h][w]=dW[h][w]=0;
				else if(M[h-1][w] == mn)
				{
					dH[h][w] = -1;
					dW[h][w] = 0;
				}
				else if(M[h][w-1] == mn)
				{
					dH[h][w] = 0;
					dW[h][w] = -1;
				}
				else if(M[h][w+1] == mn)
				{
					dH[h][w] = 0;
					dW[h][w] = 1;
				}
				else //if(M[h+1][w] == mn)
				{
					dH[h][w] = 1;
					dW[h][w] = 0;
				}
			}

/*		FOR(h,1,H+1)
		{
			FOR(w,1,W+1)
				cout << "  " << dH[h][w] << dW[h][w];
            cout << endl;
		}//*/

		char cc = 'a';
		char tt;
		q.clear();
		FOR(h,1,H+1)
			FOR(w,1,W+1)
			{
				if (R[h][w] == 0)
				{
					unsigned short int dh = h;
					unsigned short int dw = w;
					unsigned short int t;
					while(dH[dh][dw] != dW[dh][dw])
					{
						if (R[dh][dw] != 0) break;
						q.push_back(make_pair(dh,dw));
						t = dh;
						dh += dH[t][dw];
						dw += dW[t][dw];
					}
					tt = cc;
					if (R[dh][dw] != 0) tt = R[dh][dw];
					else R[dh][dw] = tt;

					FOREACH(it,q)
					{
						R[(*it).first][(*it).second] = tt;
					}
/*		FOR(h,1,H+1)
		{
			FOR(w,1,W+1)
				cout << " " << ((R [h][w])?R [h][w]:'-');
            cout << endl;
		}//*/

					if ( tt == cc ) cc++;
					q.clear();
				}
			}

		cout << "Case #"<< i+1 << ":" << endl;

		FOR(h,1,H+1)
		{
			cout << R[h][1];
			FOR(w,2,W+1)
				cout << " " << R [h][w];
			cout << endl;
		}
	}
	return 0;
}
