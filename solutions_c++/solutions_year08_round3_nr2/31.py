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

string str;
long long mem[42][2][3][5][7];

long long go(int pos, int mod2, int mod3, int mod5, int mod7)
{
	if (mem[pos][mod2][mod3][mod5][mod7] != -1)
		return mem[pos][mod2][mod3][mod5][mod7];

	long long ret = 0;

	if (pos == str.sz)
	{
		if ((mod2 == 0) && (mod3 == 0) && (mod5 == 0) && (mod7 == 0))
			ret = 1;
		else
			ret = 0;
	}
	else
	{
		int tval = 0;
		int nm2 = tval % 2, nm3 = tval%3, nm5 = tval%5, nm7 = tval%7;
		for (int i = pos; i < str.sz; i++)
		{
			tval = str[i] - '0';
			nm2 = (nm2*10 + tval)%2;
			nm3 = (nm3*10 + tval)%3;
			nm5 = (nm5*10 + tval)%5;
			nm7 = (nm7*10 + tval)%7;
			int m2 = (mod2 - nm2 + 4) %2;
			int m3 = (mod3 - nm3 + 6) %3;
			int m5 = (mod5 - nm5 + 10) %5;
			int m7 = (mod7 - nm7 + 14) %7;
			ret += go(i+1, m2, m3, m5, m7);
	
			if (i != str.sz - 1)
			{
				m2 = (-mod2 + nm2 + 4) %2;
				m3 = (-mod3 + nm3 + 6) %3;
				m5 = (-mod5 + nm5 + 10) %5;	
				m7 = (-mod7 + nm7 + 14) %7;
				ret += go(i+1, m2, m3, m5, m7);	
			}
		}
	}

	mem[pos][mod2][mod3][mod5][mod7] = ret;
	return ret;
}

int main()
{
	freopen("input.in", "r", stdin);
	//freopen("C-small.in", "r", stdin);
	//freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;cin>>T;
	REP(test, T)
	{
		cin>>str;
		memset(mem, -1, sizeof(mem));
		long long ret = 0;

		REP(m2, 2)REP(m3,3)REP(m5,5)REP(m7,7)
			if (m2 == 0 || m3 == 0 || m5 == 0 || m7 == 0)
				ret += go(0,m2,m3,m5,m7);

		//ret /= 2;

		cout<<"Case #"<<test+1<<": "<<ret<<endl;
	}
	return 0;
}