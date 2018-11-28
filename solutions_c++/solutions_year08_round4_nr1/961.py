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

struct node
{
	int value;
	int operate;
	int changable;
	node()
	{
		value=-1;
		operate=-1;
		changable=0;
	}
};

#define MAXV 1000000
int ans[10010][2];

inline int _or(int &a, int&b)
{
	if(a || b)
		return 1;
	else
		return 0;
}

inline int _and(int &a, int&b)
{
	if(a && b)
		return 1;
	else
		return 0;
}

int main()
{
#ifdef FILE_INPUT
	ifstream file_in;
	ofstream file_out;
	file_in.open(L"in.txt");
	file_out.open(L"out.txt");
#endif

	is_>>zcnt;
	for(int zi=1; zi<=zcnt; zi++)
	{
		vector<node> vn;
		node nadd;
		int M,V;
		is_>>M>>V;
		for(int i=0; i<=M; i++)
			ans[i][0]=ans[i][1]=MAXV;
		vn.push_back(nadd);
		for(int i=1; i<=(M-1)/2;i++)
		{
			node nadd;
			is_>>nadd.operate>>nadd.changable;
			vn.push_back(nadd);
		}
		for(int i=(M-1)/2+1;i<=M;i++)
		{
			node nadd;
			is_>>nadd.value;
			ans[i][0]=ans[i][1]=0;
			vn.push_back(nadd);
		}
		for(int i=M;i>1;i-=2)
		{
			int parent=i/2;
			if(vn[parent].operate == 0)		//1-AND  0-OR
			{
				for(int j=0; j<2; j++)
					for(int k=0; k<2; k++)
					{
						int v1,v2;
						if(vn[i].value>=0)
							v1=vn[i].value;
						else
							v1=j;
						if(vn[i-1].value>=0)
							v2=vn[i-1].value;
						else
							v2=k;

						int cv=ans[i][v1]+ans[i-1][v2];
						int or_v	=_or(v1, v2);
						int and_v	=_and(v1, v2);
						if(cv < ans[parent][or_v])
							ans[parent][or_v] = cv;
						if(cv+1 < ans[parent][and_v] && vn[parent].changable)
							ans[parent][and_v] = cv+1;
					}

			}else
			{
				for(int j=0; j<2; j++)
					for(int k=0; k<2; k++)
					{
						int v1,v2;
						if(vn[i].value>=0)
							v1=vn[i].value;
						else
							v1=j;
						if(vn[i-1].value>=0)
							v2=vn[i-1].value;
						else
							v2=k;

						int cv=ans[i][v1]+ans[i-1][v2];
						int or_v	=_or(v1, v2);
						int and_v	=_and(v1, v2);
						if(cv+1 < ans[parent][or_v] && vn[parent].changable)
							ans[parent][or_v] = cv+1;
						if(cv < ans[parent][and_v])
							ans[parent][and_v] = cv;
					}
			}
		}
		if(ans[1][V]<MAXV)
			os_<<"Case #"<<zi<<": "<<ans[1][V]<<endl;
		else
			os_<<"Case #"<<zi<<": IMPOSSIBLE"<<endl;
	}


#ifdef FILE_INPUT
	file_in.close();
	file_out.close();
#endif
	return 0;
}