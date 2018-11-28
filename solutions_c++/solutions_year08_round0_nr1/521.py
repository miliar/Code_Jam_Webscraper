#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<bitset>
#include<cstring>
#include<climits>
#include<deque>
#include<utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>

using namespace std;

#define rep(i,n) for(int  i=0;i<(int)(n);++i)
long double ZERO=0;
const long double INF=1/ZERO,EPSILON=1e-12;
#define all(c) (c).begin(),(c).end() 
#define rep2(i,a,b) for(int i=(a);i<=((int)b);++i)
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define sz(v) ((int)((v).size()))

int mem[1000][100];
vector<string> s,q;
int get(int i,int cs)
{
	if(i==q.size())
		return 0;
	if(mem[i][cs]!=-1)
		return mem[i][cs];
	int m=INT_MAX;
	if(q[i]==s[cs])
	{
		rep(j,s.size())
		{
			if(j==cs)continue;
			m=min(m,get(i+1,j)+1);
		}
	}
	else
		m=get(i+1,cs);
	return mem[i][cs]=m;
}
int main() {
	freopen("A-large.in","rt",stdin);
	freopen("A-small.txt","wt",stdout);
	int T;
	string str;
	getline(cin,str);
	stringstream ss;
	ss<<str<<" ";
	ss>>T;
	rep(t,T)
	{
		memset(mem,-1,sizeof mem);
		s.clear();
		q.clear();
		int x;
		getline(cin,str);
		ss<<str<<" ";
		ss>>x;
		while(x--)
		{
			getline(cin,str);
			s.push_back(str);
		}
		getline(cin,str);
		ss<<str<<" ";
		ss>>x;
		while(x--)
		{
			getline(cin,str);
			q.push_back(str);
		}
		int m=INT_MAX;
		rep(j,s.size())
			m=min(m,get(0,j));
		printf("Case #%d: %d\n",t+1,m);
	}
	return 0;
}
