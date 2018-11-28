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

const int S=102;
const int Q=1002;
int dp[Q][S];
string str[S],que[Q];
bool flag[Q];
int main()
{
	//freopen("test.txt","r",stdin);
	/*freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);*/
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int N;
	cin>>N;
	for(int cases=1;cases<=N;cases++)
	{

		int s,q;
		cin>>s;
		//cin>>q;
		string stmp;
		getline(cin,stmp);
		for(int i=0;i<s;i++)
		{
			getline(cin,str[i]);
			//cin>>stmp;
			//str[i]=stmp;
		}
		cin>>q;
		getline(cin,stmp);
		REP(i,q) 
			getline(cin,que[i]);

		for(int i=0;i<s;i++)
		{
			dp[0][i]=0;
		}

		for(int k=1;k<q;k++)
		{
			for(int m=0;m<s;m++)
			{
				if(que[k]!=str[m])
				{
					int minv=1000000,tmp;
					for(int j=0;j<s;j++)
					{
						//if(que[k-1]==str[j]) continue;
						if(que[k-1]!=str[j]){
						if(j!=m) tmp=dp[k-1][j]+1;
						else tmp=dp[k-1][j];
						minv=min(minv,tmp);}
					}
					dp[k][m]=minv;
				}
			}
		}

		int minv=1000000;
		if(q==0) minv=0;
		else
		for(int i=0;i<s;i++)
		{
			if(que[q-1]==str[i]) continue;
			minv=min(minv,dp[q-1][i]);
		}
		cout<<"Case #"<<cases<<": "<<minv<<endl;
	}
	return 0;
}

