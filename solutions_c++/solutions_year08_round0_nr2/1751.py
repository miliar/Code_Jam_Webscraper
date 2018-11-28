// pro2.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
// pro1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

//#if defined (__GNUC__) && (__GNUC__ <= 2)
//#include <hash_map>
//#include <hash_set>
//#else
//#include <ext/hash_map>
//#include <ext/hash_set>
//using namespace __gnu_cxx;
//#endif
using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

const int maxn=101;
int turn,na,nb;
struct times
{
	int begin,end;
	//bool flag;
}ta[maxn],tb[maxn];
bool tbf[maxn],taf[maxn];

class crit
{
public:
	bool operator () (const times &a,const times &b)
	{
		return a.begin<b.begin;
	}
};
int main()
{
	//freopen("test.txt","r",stdin);
	freopen("B-small.in","r",stdin);
	freopen("B-small.out","w",stdout);
	/*freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);*/
	int N;
	cin>>N;
	string s;
	for(int cases=1;cases<=N;cases++)
	{
		cin>>turn;
		cin>>na>>nb;
		getline(cin,s);
		for(int i=0;i<na;i++)
		{
			getline(cin,s);
			int k=s.find(' ');
			string s1=s.substr(0,k);
			s1.erase(s1.find(':'),1);
			int bg=s2i(s1);
			string s2=s.substr(k+1);
			s2.erase(s2.find(':'),1);
			int ed=s2i(s2);
			ta[i].begin=bg;
			ta[i].end=ed;
			//ta[i].flag=0;
		}
		for(int i=0;i<nb;i++)
		{
			getline(cin,s);
			int k=s.find(' ');
			string s1=s.substr(0,k);
			s1.erase(s1.find(':'),1);
			int bg=s2i(s1);
			string s2=s.substr(k+1);
			s2.erase(s2.find(':'),1);
			int ed=s2i(s2);
			tb[i].begin=bg;
			tb[i].end=ed;
			//tb[flag]=1;
		}

		sort(ta,ta+na,crit());
		sort(tb,tb+nb,crit());
		memset(tbf,0,sizeof(tbf));
		memset(taf,0,sizeof(taf));
		int num=0;
		for(int i=0;i<na;i++)
		{
			bool flag=0;
			for(int j=0;j<nb;j++)
			{
				if(tb[j].end+turn<=ta[i].begin && !tbf[j]){tbf[j]=1;flag=1;break;}
			}
			if(!flag) num++;
		}
		int num2=0;
		for(int i=0;i<nb;i++)
		{
			bool flag=0;
			for(int j=0;j<na;j++)
			{
				if(ta[j].end+turn<=tb[i].begin && !taf[j]){taf[j]=1;flag=1;break;}
			}
			if(!flag) num2++;
		}



		cout<<"Case #"<<cases<<": "<<num<<" "<<num2<<endl;
	}
	return 0;
}


