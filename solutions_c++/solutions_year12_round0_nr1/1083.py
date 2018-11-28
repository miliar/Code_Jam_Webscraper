/******* vinay saini (vin_74)  *******/
/********** IIIT Allahabad ***********/
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <string>
#include <bitset>
#include <cmath>
#include <list>
#include <cstdlib>
#include <map>
#include <cstring>
#include <set>
#include <stack>
#include <sstream>
#include <queue>
#include <ctime>

using namespace std;

#define debug(x) cout<<#x<<" = "<<x<<"\n"
#define   REP(i,n) for(int(i)=0;(i)<(n);(i)++)
#define  INF (1<<29)
#define         pb push_back
#define 	     sz size()
#define         mp make_pair
#define 	all(a) a.begin(),a.end()
#define fill(ar,val) memset(ar,val,sizeof ar)
#define       min(a,b) ((a)<(b)?(a):(b))
#define         max(a,b) ((a)>(b)?(a):(b))
#define FORE(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define xx first
#define yy second
typedef long long ll;
typedef pair<int,int>  pii;
typedef vector<string> vs;
ll s2i(string s) { istringstream iss(s); ll x;iss>>x; return x;}
string i2s(ll x) { ostringstream oss; oss<<x; return oss.str();}

char str[105];
int googlerese[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'}; 

void input()
{
	gets(str);
}

void solve()
{
	int n = strlen(str);
	REP(i,n) {
		if(str[i] != ' ') {
			str[i] = googlerese[str[i]-'a'];
		}
	}
}
/*
void gen_map()				//generate googlerese from examples
{
	int n = strlen(str);
	REP(i,n) {
		if(str[i]!=' ')	mapd[str2[i]-'a'] = str[i];
	}
}
*/
int main()
{
	int T;
	scanf("%d",&T);
	getchar();
	for (int case_num = 1; case_num <= T; case_num++) {
		input();
 		solve();
		printf("Case #%d: %s\n",case_num, str);
	}
	return 0;
}	
	
