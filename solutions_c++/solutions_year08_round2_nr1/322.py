#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <cmath>
#include <cassert>
using namespace std;

const int INF = 1 << 30;
const double EPS = 1e-9; 
const double PI = acos(-1.0);

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
typedef long double LD;

template <class T> inline string tostring(T x){stringstream ss; ss << x; return ss.str();}
template <class T> inline T stringto(const string &x){T r; stringstream ss(x); ss >> r; return r;}
template <class FROM, class TO> inline TO cast(FROM x){return stringto<TO>(tostring(x));}
template <class T> inline int size(const T &x){return x.size();}
template <class T> void print(const T &M, int n){cout<<'{';for(int i=0;i<n;++i){cout<<M[i];if(i+1<n)cout<<',';}cout<<"}\n";}
template <class T> void print(const T &M, int n, int m){for(int i=0;i<n;++i)print(M[i], m);cout<<'\n';}
template <class T> void print(const vector<T> &M){print(M,M.size());}
template <class T> void split_pb(vector<T> &res, const string &C){res.push_back(stringto<T>(C));}
template <> void split_pb<string>(vector<string> &res, const string &C){res.push_back(C);}
template <class T> vector<T> split(const string &S, const string &D = " ,{}")
{
	vector<T> res;
	int i = 0;
	for(;;)
	{
		for(;i < S.size() && find(D.begin(), D.end(), S[i]) != D.end();i ++);
		if (i >= S.size()) break;
		string C;
		for (;i < S.size() && find(D.begin(), D.end(), S[i]) == D.end(); i ++) C.push_back(S[i]);
		split_pb<T>(res, C);
	}
	return res;
}

vector<LL> X, Y;
LL R[3][3], res, s;

int G[][3] = {{0, 0, 0}, {1, 1, 1}, {2, 2, 2}, {0, 1, 2}, {0, 2, 1}, {1, 0, 2}, {1, 2, 0}, {2, 0, 1}, {2, 1, 0}, };

void main()
{
#ifndef _DEBUG
	const string file_name = "A-large";
	freopen((file_name + ".in").c_str(), "r", stdin);
	freopen((file_name + ".out").c_str(), "w", stdout);
#endif
	int nn;
	cin >> nn;
	for (int jj = 1; jj <= nn; jj++)
	{
		X.clear(); Y.clear();
		res = 0;
		memset(R, 0, sizeof(R));
		LL n, A, B, C, D, X0, Y0, M;
		cin >> n >> A >> B >> C >> D >> X0 >> Y0 >> M;
		LL x = X0, y = Y0;
		for (int i = 0; i < n; i++)
		{
			X.push_back(x);
			Y.push_back(y);
			x = (A * x + B) % M;
			y = (C * y + D) % M;
		}
		for (int i = 0; i < X.size(); i++)
		{
			R[X[i] % 3][Y[i] % 3]++;
		}
		for (int ix = 0; ix < 9; ix++)
		{
			for (int iy = 0; iy < 9; iy++)
			{
				if (ix >= 3 || iy >= 3)
				{
					s = 1;
					for (int j = 0; j < 3; j++)
					{
						s *= R[G[ix][j]][G[iy][j]];
					}
				}
				else
				{
					s = 0;
					if (R[G[ix][0]][G[iy][0]] >= 2)
					{
						s = R[G[ix][0]][G[iy][0]];
						s = s * (s - 1) * (s - 2);
					}
				}
				res += s;
			}
		}
		res /= 6;
		cout << "Case #" << jj << ": ";
		cout << res;
		cout << '\n';
	}

}
