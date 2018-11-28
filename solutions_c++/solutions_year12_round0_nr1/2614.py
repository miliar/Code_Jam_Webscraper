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


string s[]={
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

string t[]={
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"
};

int main(){
	freopen("D:\\Ñ¸À×ÏÂÔØ\\A-small-attempt2.in", "r", stdin);
	freopen("D:\\Ñ¸À×ÏÂÔØ\\A-small-attempt2.out", "w", stdout);
	map<char, char> mp;
	rep(i, 0, 3) repv(j, s[i]) if( s[i][j]>='a' && s[i][j]<='z' ){
		mp[ s[i][j] ] = t[i][j];
	}
	mp['q']='z';
	mp['z']='q';
	//bool vst1[126]={false};
	//bool vst2[126]={false};
	//repi(it, mp) vst1[it->ff]=vst2[it->ss]=true;
	//rep(i, 'a', 'z'+1) if( vst1[i]==false ) putchar(i);
	//rep(i, 'a', 'z'+1) if( vst2[i]==false ) putchar(i);
	//cout<<sz(mp)<<endl;
	int cas, Te=1; cin>>cas;
	string tmp;
	getline(cin, tmp);
	while( cas-- ){
		getline(cin, tmp);
		repv(i, tmp) if( tmp[i]!=' ') tmp[i]=mp[ tmp[i] ];
		printf("Case #%d: %s\n", Te++, tmp.c_str());
	}
}


























