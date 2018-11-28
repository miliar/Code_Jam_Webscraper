#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <fstream>

using namespace std;

typedef long long _ll;
typedef vector<int> _vi;
typedef vector<_ll> _vll;
typedef vector<string> _vs;
typedef istringstream _iss;
#define _a(v) (v).begin(),(v).end()
#define _e(x,y) (fabs((x)-(y))<1e-10)
#define _p push_back
#define _mp make_pair
#define _m(v) memset(v,0,sizeof(v));
#define _f(i,b,e) for(int i=b;i<e;i++)
#define _fl(i,n) for(int i=0;i<(n).length();i++)
#define _fs(i,n) for(int i=0;i<(n).size();i++)
#define _fe(t,i,n) for(t::iterator i=(n).begin();i!=(n).end();i++)
#define _fd(t,e) ((t).find(e)!=(t).end())
#define _s(x,y) {x+=y;y=x-y;x-=y;}
#define _st(x, y, t) {t _t_; _t_=x;x=y;y=_t_;}

#define FILE_INPUT

#ifdef FILE_INPUT
	#define is_ file_in
	#define os_ file_out
#else
	#define is_ cin
	#define os_ cout
#endif



int zcnt;
int pcnt;
int primes[1000];

#define SET_SIZE 1010   //并查集大小

class CSet
{
private:
	void Link(int a,int b)
	{
		if(rank[a]>rank[b])
			sbuff[b]=a;
		else if(rank[a]<rank[b])
			sbuff[a]=b;
		else
		{
			sbuff[a]=b;
			rank[b]++;
		}
	}
public:
	int sbuff[SET_SIZE];
	int rank[SET_SIZE];
	CSet()
	{
		for(long i=0;i<SET_SIZE;i++)
			Make_Set(i);
	}
	void Make_Set(int x)
	{
		sbuff[x] = x;
		rank[x] = 0;
	}
	int Find_Root(int x)
	{
		if(sbuff[x] != x)
		    sbuff[x]=Find_Root(sbuff[x]);
		return sbuff[x];
	}
	void Union_Set(int sa, int sb)
	{
		Link(Find_Root(sa),Find_Root(sb));
	}
};


void gp()
{
	pcnt=1;
	primes[0]=2;
	for(int i=3; i<1010; i++)
	{
		for(int j=0; j<pcnt; j++)
			if(i % primes[j]==0)
				goto next_i;
		primes[pcnt++] = i;
next_i:;
	}
}

int main()
{
#ifdef FILE_INPUT
	ifstream file_in;
	ofstream file_out;
	file_in.open(L"in.txt");
	file_out.open(L"out.txt");
#endif

	gp();

	is_>>zcnt;
	for(int zi=1; zi<=zcnt; zi++)
	{
		int A, B, P;
		int ans;
		int pos=0;
		CSet st;

		is_>>A>>B>>P;
		while(primes[pos] < P)
			pos++;
		while(primes[pos]<B && pos<pcnt)
		{
			int t=primes[pos]*2;
			while(t<=B)
			{
				st.Union_Set(primes[pos], t);
				t+=primes[pos];
			}
			pos++;
		}

		set<int> si;
		for(int i=A; i<=B; i++)
			si.insert(st.Find_Root(i));
		
		os_<<"Case #"<<zi<<": "<<si.size()<<endl;
	}

#ifdef FILE_INPUT
	file_in.close();
	file_out.close();
#endif
	return 0;
}