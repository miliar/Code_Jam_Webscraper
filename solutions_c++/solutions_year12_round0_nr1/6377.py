#include <string>
#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <numeric> 
#include <sstream> 
#include <iostream> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <queue> 
using namespace std ; 

typedef long long LL;
typedef vector<int> VI;

#define FOR(i,a,b) for(int i=(a); i<=(b); i++)
#define DOW(i,a,b) for(int i=(a); i>=(b); i--)
#define REP(i,n)   for(int i=0; i<(n); i++)
#define ALL(v) v.begin(),v.end()
#define MEMSET(v,h) memset(v,h,v.sizeof(v))
#define SZ(v) (int)v.size()
#define len(v) v.length()
#define PB push_back
#define MP make_pair
#define oo 1000000000

int Map[200];

void convert(string s1, string s2){
	REP(i,len(s1))
		if(s1[i] != ' '){
			Map[s1[i]-'a'] = s2[i]-'a';
		}
};

int main()
{
    freopen("test.txt", "r", stdin);
    freopen("testout.txt", "w", stdout);
	REP(i,100) Map[i] = -1;

	string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string s2 = "our language is impossible to understand";
	convert(s1,s2);
	s1 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	s2 = "there are twenty six factorial possibilities";
	convert(s1,s2);
	s1 = "de kr kd eoya kw aej tysr re ujdr lkgc jvzq";
	s2 = "so it is okay if you want to just give upqz";
	convert(s1,s2);

	int T;
	cin>>T;
	string s;
	getline(cin,s);
	REP(t,T){
		getline(cin,s);
		printf("Case #%d: ", t+1);
		REP(i,len(s)){
			if(s[i] == ' ') cout<<" ";
			else printf("%c",char(Map[s[i]-'a']+'a'));
		}
		cout<<endl;
	}
    return 0;
}
