#include <vector>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <list>
#include <ctime>
#include <string>
#include <cassert>

using namespace std;

//----------------------zjut_DD for Topcoder-------------------------------
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
#define PB push_back
#define MP make_pair
#define ff first
#define ss second
#define two(w) (1<<(w))
#define test(x,w) (x&two(w))
#define sz(v) (int)v.size()
#define all(c) c.begin(),c.end() 
#define clr(buf,val) memset(buf,val,sizeof(buf))
#define rep(i,l,r) for(int i=(l);i<(r);i++)
#define repv(i,v)  for(int i=0;i<(int)v.size();i++)
#define repi(it,c) for(typeof(c.begin()) it=c.begin();it!=c.end();++it)
//------------------------------------------------------------------------

#define maxn 11000


int toInt(string s){
	int ret=0;
	repv(i, s) ret=ret*10+s[i]-'0';
	return ret;
}

int main(){
	freopen("D:\\Ñ¸À×ÏÂÔØ\\C-large.in", "r", stdin);
	freopen("D:\\Ñ¸À×ÏÂÔØ\\C-large.out", "w", stdout);
	
	int cas, Te=1; cin>>cas;
	while( cas-- ){
		int A, B, ans=0;
		cin>>A>>B;
		for(int n=A;n<=B;n++){
			char ch[15];
			sprintf(ch, "%d", n);
			string s=ch;
			set<int> st;
			rep(i, 1, sz(s) ){
				int m=toInt(s.substr(i)+s.substr(0,i));
				if( m>n && m<=B ) st.insert(m);
			}
			ans+=sz(st);
		}
		printf("Case #%d: %d\n", Te++, ans);
	}
}


























