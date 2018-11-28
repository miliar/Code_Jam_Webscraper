#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <limits>
#include <map>
#include <cmath>
#include <numeric>
#include <stdio.h>
using namespace std;

#define pb push_back
#define REP(i,n) for(int i=0; i<(n); ++i)   
#define ALL(X) (X).begin(),(X).end()
#define present(c,x) ((c).find(x) != (c).end())
typedef long long ll;
template<class T>inline int sz(T& x){return (int)x.size();}
int stoi(string a){int len=sz(a);if(len==1)return a[0]-'0';return a[len-1]-'0'+10*stoi(a.substr(0,len-1));}
template<class T>inline string tostring(T& i){ostringstream oss; oss << i; return oss.str();}
template <class T> void make_unique(T& v){sort(ALL(v)); v.resize(unique(ALL(v)) - v.begin());}

void MakeEnd(int val,char * str)
{
	string num = tostring(val);
	for(int i=0;i<4;i++)
		str[i] = '0';
	memcpy(str + 4 - sz(num),num.c_str(),sz(num));
	int k =1;
}

string getLine()
{
	string ret;
	while(true)
	{
		char c = getc(stdin);
		if(c == '\n')
		{
			break;
		}
		else
		{
			ret += c;
		}
	}
	return ret;
}

int getNum()
{
	string str = getLine();
	return stoi(str);
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test; test = getNum();
	int table[101][101];
	int map[101][101];
	const char * ori = "welcome to code jam";
	const int mod = 10000;
	for(int tt=1;tt<=test;tt++)
	{
		int dp[21][501]; memset(dp,0,sizeof(dp));
		string str = getLine();
		for(int j=0;j<sz(str);j++)
			dp[0][j] = 1;
		for(int i=1;i<=strlen(ori);i++)
			dp[i][0] = 0;
		for(int i=1;i<=strlen(ori);i++)
		{
			for(int j=1;j<=sz(str);j++)
			{
				dp[i][j] = dp[i][j-1];
				if(str[j-1] == ori[i-1])
				{
					dp[i][j] += dp[i-1][j-1];
				}
				dp[i][j] %= mod;
			}
		}
		char ans[10];
		memset(ans,0,sizeof(ans));
		MakeEnd(dp[19][sz(str)],ans);
		printf("Case #%d: %s\n",tt, ans);
	}
	return 0;
} 