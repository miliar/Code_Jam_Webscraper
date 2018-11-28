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

int n, na, nb, t;

struct time2
{
	int t1, t2;
	time2(int t1 = 0, int t2 = 0): t1(t1), t2(t2) {}
};

vector<time2> Times;
time2 T2;
vector<bool> FromA;
vector<vector<int> > G;
vector<int> Mate;
vector<int> M;
vector<bool> Was;

bool DFS(int u)
{
	if (!Was[u])
	{
		Was[u] = 1;
		for (int i = 0; i < G[u].size(); i++)
		{
			int v = G[u][i];
			if (Mate[v] == -1 || DFS(Mate[v]))
			{
				Mate[v] = u;
				return 1;
			}
		}
	}
	return 0;
}
void main()
{
	const string file_name = "B-large";
	freopen((file_name + ".in").c_str(), "r", stdin);
	freopen((file_name + ".out").c_str(), "w", stdout);
	int nn;
	cin >> nn;
	for (int jj = 0; jj < nn; jj++)
	{
		cin >> t >> na >> nb;
		n = na + nb;
		Times.clear();
		FromA.clear();
		G.clear();
		M.clear();
		Mate.clear();
		for (int i = 0; i < n; i++)
		{
			int t1h, t1m, t2h, t2m;
			scanf("%d:%d %d:%d", &t1h, &t1m, &t2h, &t2m);
			FromA.push_back(i < na);
			Times.push_back(time2(t1h * 60 + t1m, t2h * 60 + t2m + t));
		}
		for (int i = 0; i < n; i++)
		{
			G.push_back(vector<int>());
			Mate.push_back(-1);
			M.push_back(-1);
			for (int j = 0; j < n; j++)
			{
				if (FromA[i] != FromA[j] && Times[i].t2 <= Times[j].t1)
				{
					G.back().push_back(j);
				}
			}
		}
		for (int i = 0; i < n; i++)
		{
			Was.clear();
			Was.resize(n, 0);
			DFS(i);
		}
		Was.clear();
		Was.resize(n, 0);
		int a1 = 0, a2 = 0;
		for (int i = 0; i < n; i++)
		{
			int p = i;
			int op = -1;
			while (p != -1 && !Was[p])
			{
				Was[p] = 1;
				op = p;
				p = Mate[p];
			}
			if (p == -1)
			{
				assert(op != -1);
				if (op < na)
				{
					a1++;
				}
				else
				{
					a2++;
				}
			}
		}
		cout << "Case #" << jj + 1 << ": " << a1 << " " << a2;
		cout << '\n';
	}
}
