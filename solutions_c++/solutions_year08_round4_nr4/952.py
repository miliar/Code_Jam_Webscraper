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

int k, P[32];
string S2, S;
void main()
{
#ifndef _DEBUG
	const string file_name = "D-small-attempt0";
	freopen((file_name + ".in").c_str(), "r", stdin);
	freopen((file_name + ".out").c_str(), "w", stdout);
#endif
	int nn;
	cin >> nn;
	for (int jj = 1; jj <= nn; jj++)
	{
		cin >> k >> S2;
		int ans = -1;
		for (int i = 0; i < k; i++)
		{
			P[i] = i;
		}
		do 
		{
			S.resize(S2.size());
			
			for (int i = 0; i < S2.size(); i++)
			{
				S[i] = S2[P[i % k] + k * (i / k)];
			}
			int s = 0;
			s = unique(S.begin(), S.end()) - S.begin();
			if (ans == -1 || s < ans)
			{
				ans = s;
			}
		} while (next_permutation(P, P + k));
		cout << "Case #" << jj << ": ";
		cout << ans;
		cout << '\n';
	}

}
