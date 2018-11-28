
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

vector<int> P;
bool prime(int x)
{
	bool b = x & 1;
	for (int i = 0; b && i < P.size() && P[i] * P[i] <= x; i++)
	{
		b = x % P[i];
	}
	if (b)
		P.push_back(x);
	return b;
}
int a, b, p;
int ip;
bool gg(int i, int j)
{
	int m = min(i, j);
	for (int f = ip; P[f] <= m; f++)
	{
		if (i % P[f] == 0 && j % P[f] == 0)
		{
			return 1;
		}
	}
	return 0;
}
void main()
{
#ifndef _DEBUG
	const string file_name = "B-small-attempt0";
	freopen((file_name + ".in").c_str(), "r", stdin);
	freopen((file_name + ".out").c_str(), "w", stdout);
#endif
	P.push_back(2);
	for (int i = 3; i < 10000; i++)
	{
		prime(i);
	}
	int n;
	cin >> n;
	for (int jj = 1; jj <= n; jj++)
	{
		cin >> a >> b >> p;
		for (int i = 0; i < P.size(); i++)
		{
			if (P[i] >= p)
			{
				ip = i;
				break;
			}
		}
		vector<int> S(b + 1, 0);
		for (int i = a; i <= b; i++)
		{
			S[i] = i;
		}
		for (int i = a; i <= b; i++)
		{
			for (int j = i + 1; j <= b; j++)
			{
				int hi = S[i];
				int hj = S[j];
				if (hi != hj && gg(i, j))
				{
					for (int k = a; k <= b; k++)
					{
						if (S[k] == hi)
						{
							S[k] = hj;
						}
					}
				}
			}
		}
		S.erase(S.begin(), S.begin() + a);
		sort(S.begin(), S.end());
		int res = unique(S.begin(), S.end()) - S.begin();
		cout << "Case #" << jj << ": ";
		cout << res;
		cout << '\n';
	}

}
