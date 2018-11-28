#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

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

char buf[1024*1024];

int main() {
	freopen("C:\\Projects\\GCJ\\input", "rt", stdin);
	freopen("C:\\Projects\\GCJ\\output.txt", "wt", stdout);

	gets(buf);
	int c = atoi(buf);
	for (int z=0;z<c;z++)
	{
		int n, A, B, C, D, x0, y0, M;
		scanf("%d%d%d%d%d%d%d%d", &n, &A, &B, &C, &D, &x0, &y0, &M);

		vector<long long> x,y;
		x.push_back(x0);
		y.push_back(y0);
		long long a=x0, b=y0;
		int i;
		int count[9] = {0};
		count[a%3 + 3*(b%3)]++;
		for (i=0;i<n-1;i++)
		{
			a = (((A % M) * a%M)%M + B%M)%M;
			b = (((C % M) * b%M)%M + D%M)%M;

			//cout << a << " " << b << endl;
			int temp=a%3 + 3*(b%3);
			count[temp]++;
		}

		//for (i=0;i<9;i++)
		//	cout << count[i] << endl;
		long long res = 0;
		for (i=0;i<9;i++)
		{
			for (int j=i;j<9;j++)
			{
				for (int k=j;k<9;k++)
				{
					int xs = i%3 + j%3 + k%3;
					int ys = i/3 + j/3 + k/3;

					if (xs %3 == 0 && ys%3==0)
					{
						int val = 0;

						if (i == j && j==k)
						{
							val = count[i];
							res += ((long long)val * (val-1) * (val-2))/6;
							continue;
						}
						if (i == j || j == k || k == i)
						{
							if (i==j)
							{
								val = count[i];
								res += ((long long)val * (val-1) * count[k])/2;
								continue;
							}
							if (k==j)
							{
								val = count[k];
								res += ((long long)val * (val-1) * count[i])/2;
								continue;
							}
							if (i==k)
							{
								val = count[i];
								res += ((long long)val * (val-1) * count[j])/2;
								continue;
							}
						}

						res += (long long)count[i] * count[j] * count[k];
					}
				}
			}
		}

		cout << "Case #" << (z+1) << ": " << res << endl;
	}

	exit(0);
}
