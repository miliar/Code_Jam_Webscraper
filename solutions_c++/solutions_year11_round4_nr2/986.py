#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cassert>
#include <climits>
#include <cstdio>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

typedef pair<int, int>  pii;
typedef vector<int>     vi;
typedef long long       Long;

#define toStr(a)      (((stringstream&)((stringstream()<<(a)))).str())
#define FOR(i,a,b)    for (int i = (a); i < (b); i++)
#define foreach(it,c) for(typeof((c).begin()) it = (c).begin(); it! = (c).end(); it++)
#define all(a)        ((a).begin(), (a).end())
#define pb(a)         push_back(a)
#define mp            make_pair
#define X            first
#define Y            second

double eps = 1e-9;

Long vx[510][510];
Long vy[510][510];
Long mass[510][510];

Long Sx[510][510];
Long Sy[510][510];
Long Smass[510][510];

int R, C, D;

void p_sum(Long a[][510], Long b[][510]) 
{
	//initial conditions
	a[0][0] = b[0][0];
	FOR(j,1,C)
		a[0][j] = a[0][j-1] + b[0][j];
	FOR(i,1,R)
		a[i][0] = a[i-1][0] + b[i][0];

	//everything else
	FOR(i, 1, R)
		FOR(j, 1, C)
			a[i][j] = a[i][j-1] + a[i-1][j] - a[i-1][j-1] + b[i][j];
}

Long get(Long a[][510], int i, int j)
{
	if (i<0 || i>=R || j<0 || j>=C) return 0;
	return a[i][j];
}

Long sum(Long a[][510], int si, int sj, int n, Long v[][510])
{
	Long sq = get(a, si+n-1, sj+n-1) - get(a, si-1, sj+n-1) - get(a, si+n-1, sj-1) + get(a, si-1, sj-1);
	return sq - v[si][sj] - v[si][sj+n-1] - v[si+n-1][sj] - v[si+n-1][sj+n-1];
}

void print(Long a[][510], int n)
{
	FOR(i, 0, n)
	{
		FOR(j, 0, n)
			cout << setw(5) << a[i][j];
		cout << endl;
	}
	cout << endl;
}

int main()
{
	freopen("data.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T; cin >> T;
	
	for (int xxx=1; xxx<=T; xxx++)
	{
		cout << "Case #" << xxx << ": "; 
		cin >> R >> C >> D;

		FOR(i, 0, R) //fill initial arrays
		{
			string str;
			cin >> str;
			FOR(j, 0, C)
			{
				mass[i][j] = D + str[j] - '0';
				vx[i][j] = i*mass[i][j];
				vy[i][j] = j*mass[i][j];
			}
		}
		
		//compute partial sums
		p_sum(Sx, vx);
		p_sum(Sy, vy);
		p_sum(Smass, mass);

//		print(Sx, 3);
//		cout << endl << endl;
//		print(Sy, 3);
//
		int N = min(R, C);
		for (int n=N; n>=3; n--)
			for (int i=0; i+n-1<R; i++)
				for (int j=0; j+n-1<C; j++)
				{
					Long totMass = sum(Smass, i, j, n, mass);
					
					double cx = 1.*sum(Sx, i, j, n, vx)/totMass + .5;
					double cy = 1.*sum(Sy, i, j, n, vy)/totMass + .5;

					//printf("\ncx = %lld / %lld + .5\n", sum(Sx, i, j, n, vx), totMass);
					//printf("cy = %lld / %lld + .5\n", sum(Sy, i, j, n, vy), totMass);

					//if (n == 5)
					//	printf("%d, %d  -->  (%lf, %lf)\n", i, j, cx, cy);

					if (abs(cx - i - (n-2)/2. - 1) < eps && abs(cy - j - (n-2)/2. - 1) < eps)
					{
						cout << n << endl << flush;
						goto found;
					}
				}

		cout << "IMPOSSIBLE\n" << flush;
		continue;

		found:	;
		
	}
}