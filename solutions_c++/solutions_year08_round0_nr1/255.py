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

int n, s, q;

VS SE, QQ;
string SS;
VI F, S;

typedef map<pair<int, int>, int> MAP;
MAP M;

int gg(int nq, int np)
{
	if (nq < 0)
	{
		return 0;
	}
	if (nq == q)
	{
		int mm = INF;
		for (int i = 0; i < s; i++)
		{
			mm = min(mm, gg(q - 1, i));
		}
		return mm;
	}

	MAP::iterator it = M.find(make_pair(nq, np));
	if (it != M.end())
	{
		return it->second;
	}
	int ind = find(SE.begin(), SE.end(), QQ[nq]) - SE.begin();
	assert(ind != SE.size());
	if (np == ind)
	{
		return INF;
	}
	int ans = INF;
	for (int i = 0; i < s; i++)
	{
		int nv = gg(nq - 1, i);
		if (i != np)
		{
			nv++;
		}
		ans = min(ans, nv);
	}
	M[make_pair(nq, np)] = ans;
	return ans;
}
void main()
{
	const string file_name = "A-large";
	freopen((file_name + ".in").c_str(), "r", stdin);
	freopen((file_name + ".out").c_str(), "w", stdout);
	getline(cin, SS);
	n = stringto<int>(SS);
	for (int jj = 0; jj < n; jj++)
	{
		getline(cin, SS);
		s = stringto<int>(SS);
		SE.resize(s);
		F.clear();
		F.clear();
		F.resize(s, 0);
		S.resize(s, 0);
		for (int i = 0; i < s; i++)
		{
			getline(cin, SE[i]);
		}
		getline(cin, SS);
		q = stringto<int>(SS);
		QQ.resize(q);
		for (int i = 0; i < q; i++)
		{
			getline(cin, QQ[i]);
		}
		/*for (int i = 0; i < q; i++)
		{
		int ind = find(SE.begin(), SE.end(), QQ[i]) - SE.begin();
		for (int j = 0; j < s; j++)
		{
		if (j == ind)
		{
		S[j] = INF;
		}
		else
		{
		int mm = INF;
		for (int k = 0; k < s; k++)
		{
		int nv = F[k];
		if (k != j)
		{
		nv++;
		}
		mm = min(mm, nv);
		}
		S[j] = mm;
		}
		}
		print(S, s);
		swap(F, S);
		}
		int mm = INF;
		for (int i = 0; i < s; i++)
		{
		mm = min(mm, S[i]);
		}*/
		M.clear();
		int mm = gg(q, 0);
		cout << "Case #" << jj + 1 << ": " << mm;
		if (jj + 1 < n)
		{
			cout << "\n";
		}
	}
}
