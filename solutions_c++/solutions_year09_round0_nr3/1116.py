/*	SURENDRA KUMAR MEENA	*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <queue>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long int LL;
#define ALL(s) (s).begin(),(s).end()
#define R(i,m,n)	for(int i=m;i>=n;i--)
#define FF(i,m,n)	for(int i=m;i<n;i++)
#define F(i,n)	FF(i,0,n)
#define VI vector<int>
#define PB push_back
#define CLR(s,v) memset(s,v,sizeof(s))
string to_str(LL x){ ostringstream o;o<<x;return o.str();}
LL to_int(string s){ istringstream st(s); LL i;	st>>i;return i;}
#define FR(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)
typedef pair<int,int> PI;
#define MP(x,y) make_pair(x,y)
#define f first
#define s second
#define VP vector<PI>
#define S(t)	scanf("%d",&t)
string s;
const string cs="welcome to code jam";
const int len=19;
const int MOD=10000;
int l,mem[1000][50];
int fn(int i,int j){
	if(j==len)	return 1;
	if(i==l)	return 0;
	int &ret=mem[i][j];
	if(ret!=-1)	return ret;
	ret=0;
	if(s[i]==cs[j])	ret=fn(i+1,j+1);
	ret+=fn(i+1,j);
	return ret=ret%MOD;
}

int main(){
	int n;
	cin>>n;
	getline(cin,s);
	FF(cas,1,n+1){
		getline(cin,s);
		l=s.size();
		CLR(mem,-1);
		printf("Case #%d: %04d\n",cas,fn(0,0));
	}
	return 0;
}
