#include <algorithm> 
#include <string> 
#include <set> 
#include <map> 
#include <vector> 
#include <queue> 
#include <iostream> 
#include <iterator> 
#include <sstream> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <numeric>
#include <list>
 
using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n) 
#define pb push_back 
#define sz size() 

#define ALL(c) (c).begin(), (c).end() 
#define SORT(c) sort(ALL(c))
#define UNIQUE(v) SORT(v),v.erase(unique(v.begin(),v.end()),v.end())
#define INF 2147483647
#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
#define MP(a,b)	 make_pair((a), (b))
#define X first
#define Y second
#define CLR(a,v) memset((a),(v),sizeof(a)) 

typedef pair<int,int> II;
typedef vector<int> VI;
typedef vector<VI > VVI;
typedef vector<II > VII;
template<typename T>
void outV(const vector<T>& v){cout<<endl;REP(i,v.sz)cout<<v[i]<<" ";cout<<endl;}
template<typename T>
void outVV(const vector<vector<T> >& v){cout<<endl;REP(i,v.sz){REP(j, v[i].sz)cout<<v[i][j]<<" ";cout<<endl;}cout<<endl;}
void outVII(const VII& v){cout<<endl;REP(i,v.sz)cout<<"("<<v[i].first<<", "<<v[i].second<<") ";cout<<endl;}
int gcd(int a,int b){return a==0 ? b : gcd(b%a, a);}


int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin>>T;
	REP(test, T)
	{
		int k;
		string str;
		cin>>k>>str;

		int res = 10000000;

		vector<int> v;
		REP(i,k)
			v.pb(i + 1);
		do
		{
			string s;
			for (int pos = 0; pos < str.sz; pos += k)
			{
				REP(i, k)
					s += str[pos + v[i] - 1];
			}
			int gr = 1;
			for (int i = 1; i < s.sz; i++)
			{
				if (s[i] == s[i-1])continue;
				gr++;
			}
			if (gr < res)
				res = gr;

		}while (next_permutation(ALL(v)));

		cout<<"Case #"<<test+1<<": ";
		cout<<res<<endl;
	}

	return 0;
}
