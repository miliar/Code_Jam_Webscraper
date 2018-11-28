#include <string>
#include <vector>
#include <map>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <set>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>
#include <complex>
#include <cstdio>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef complex<double> pnt;
typedef pair<int, int> pii;

#define RA(x) (x).begin(), (x).end()
#define FE(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int) (x).size())

#define MAXN 1001

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

class Seg
{
public:
	long long  B, E, w;
	bool operator<(const Seg& s) const
	{
		return B < s.B;
	}
} W[MAXN];

class Seg2
{
public:
	long long  B, E, w;
	bool operator<(const Seg2& s) const
	{
		return w < s.w;
	}
} W2[10*MAXN];

int main()
{
	long long t, T;

	long long X, S, R, N, i;
	double time;

	cin >> T;
	for (t = 0; t < T; ++t)
	{
		cout << "Case #" << t+1 << ": ";
		cin >> X >> S >> R >> time >> N;
		if (R < S)
			R = S;
		for (i = 0; i < N; ++i)
		{
			cin >> W[i].B >> W[i].E >> W[i].w;		
			W2[i].B = W[i].B;
			W2[i].E = W[i].E;
			W2[i].w = W[i].w;
		}
		sort(W, W+N);
		long long  prevTime = 0;
		long long  C = N;
		for (i = 0; i < N; ++i)
		{
			if (W[i].B > prevTime)
			{
				W2[C].B = prevTime;
				W2[C].E = W[i].B;
				W2[C++].w = 0;
			}
			prevTime = W[i].E;
		}
		if (W[N-1].E < X)
		{
			W2[C].B = W[N-1].E;
			W2[C].E = X;
			W2[C++].w = 0;
		}
		sort(W2, W2+C);
		double totalTime = 0;
		for (i = 0; i < C; ++i)
		{
			if (time > 0)
			{

				double timeForW = (W2[i].E-W2[i].B)/(double)(R+W2[i].w);
				if (timeForW > time)
				{
					totalTime += time + (W2[i].E-W2[i].B-time*(R+W2[i].w))/(double)(S+W2[i].w);
					time = 0;
				}
				else
				{
					time -= timeForW;
					totalTime += timeForW;
				}
			}
			else
			{
				totalTime += (W2[i].E-W2[i].B)/(double)(S+W2[i].w);
			}
		}
		printf("%.9lf\n", totalTime);
	}

    return 0;
}
