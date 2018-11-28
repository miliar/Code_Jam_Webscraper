#include <map>
#include <set>
#include <queue>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <ctime>
#include <string>
#include <vector>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <sstream>
using namespace std;

#define pb push_back
#define pi 2*acos(0.0)
#define inf 1000000000
#define all(c) (c).begin(), (c).end()

#define L(s) (int)((s).end()-(s).begin())
#define ll long long
#define fo(i,n) for(i=0;i<(n);++i)
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))

typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

const double eps = 1e-6;
vector<long long> dx, dy;
int n;
void sortIt()
{
	int i,j, temp;
	for (i=0; i<n-1; i++)
		for (j=i+1; j<n; j++)
		{
			if (dx[i]>dx[j])
			{
				temp = dx[i];  dx[i] = dx[j];  dx[j] = temp;
				temp = dy[i];  dy[i] = dy[j];  dy[j] = temp;
			}
		}
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int numCase;
	long long A, B, C, D, X, Y, x0, y0, M;

	long long sum = 0;
	float xx, yy;

	cin >> numCase;
	For(test, 1, numCase)
	{
		cin >> n >> A >> B >> C  >> D  >> x0 >> y0 >> M;
		X = x0; Y = y0;
		dx.clear();
		dy.clear();
		dx.pb(x0);
		dy.pb(y0);
		For(i, 1, n-1)
		{
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
//			cout << '<'<<X<<','<<Y<<'>' << endl;
			dx.pb(X);
			dy.pb(Y);
		}

		//sort(all(dx));
		sum = 0;
		for (int i=0; i<n-2; i++)
			for (int j=i+1; j<n-1; j++)
				for (int k=j+1; k<n; k++)
				{
					xx = 1.0*(dx[i]+dx[j]+dx[k])/3;
					yy = 1.0*(dy[i]+dy[j]+dy[k])/3;
//					cout << "---" << xx << ":" << yy << endl;
					if (((abs(xx-(int)xx))<eps) && (abs((yy-(int)yy)<eps)))
					{
						//cout << xx << ' ' << yy << endl;
						sum++;
					}
				}
		cout << "Case #" << test << ": "<< sum <<endl;
	}

	return 0;
}
