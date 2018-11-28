#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
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

typedef long long Long;
typedef unsigned long long uLong;
typedef unsigned int uint;

const double PI = acos(-1.0);
const double EPS = 1e-12;

#define FOR(i,a,b) for (int i=(int)(a); i<(int)(b); ++i)
#define two(X) (1<<(X))
#define twoL(X) (((Long)(1))<<(X))
#define bit(S,X) (((S)&two(X))!=0)
#define bitL(S,X) (((S)&twoL(X))!=0)

template<class T> string toStr(T n){ostringstream ss;ss<<n;ss.flush(); return ss.str();}
template<class T> string vtos(vector<T> a) { stringstream ss; for (int i=0; i<(int)a.size(); i++) { if (i > 0) ss << ", "; ss << a[i]; } return ss.str(); }

int toInt(string s){int n=0; istringstream ss(s); ss>>n; return n;}
Long toLong(string s){Long n=0; istringstream ss(s); ss>>n; return n;}

int N, L, W;
int radius[16];
double X[16];
double Y[16];
clock_t start;

double dist(double x1, double y1, double x2, double y2)
{
	return sqrt( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) );
}

bool intersects(int i, int j)
{
	double D = dist(X[i], Y[i], X[j], Y[j]);
	return D < radius[i] + radius[j];
}

bool dfs(int inx)
{
	if (inx >= N) return true;

	while (true)
	{
		if ((clock() - start) > 5*CLOCKS_PER_SEC)
			return false;

		X[inx] = (1.*rand()/RAND_MAX )*W; 
		Y[inx] = (1.*rand()/RAND_MAX )*L;
		//cerr << "Placing circle: " << inx << " at " << X[inx] << ", " << Y[inx] << endl;

		bool ok = true;
		FOR(i, 0, inx)
			if (intersects(inx, i))
			{
			//	cerr << "Nvm found intersection with " << i << endl;
				ok = false;
				break;
			}

		if (ok && dfs(inx+1)) 
		{
			//cerr << "great! done with circle " << inx << endl;
			break;
		}
	}

	return true;
}

void solve()
{
	cin >> N >> W >> L;
	FOR(i,0,N)
		cin >> radius[i];

	//sort(radius, radius+N);
	//reverse(radius, radius+N); 

	start = clock();
	bool ok = dfs(0);
	cerr << ok << " -- ";

	FOR(i,0,N)
	{
		assert(X[i] >= 0 && X[i] <= W && Y[i] >= 0 && Y[i] <= L);
		FOR(j,i+1,N)
			assert(intersects(i, j) == false);
	}

	FOR(i,0,N)
	{
		cout << " " << setprecision(10) << X[i] << " " << Y[i];
		cerr << " " << setprecision(10) << X[i] << " " << Y[i];
	}

	cout << endl << flush;
	cerr << endl << flush;
}

int main()
{
	srand ( time(NULL) );
	freopen("data.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	cin >> T;
	for (int x=1; x<=T; x++) 
	{
		printf("Case #%d:", x);
		cerr << x << ": ";
		solve();
	}

	return 0;
}
