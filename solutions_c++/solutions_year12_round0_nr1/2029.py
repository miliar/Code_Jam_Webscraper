//#pragma comment(linker,"/STACK:16777216") /*16Mb*/
//#pragma comment(linker,"/STACK:33554432") /*32Mb*/
#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<numeric>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<memory>
#include<string>
#include<vector>
#include<cctype>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

typedef unsigned long long      ui64;
typedef long long               i64;
typedef	vector<int>             VI;
typedef	vector<bool>            VB;
typedef	vector<VI>              VVI;
typedef	vector<string>          VS;
typedef	pair<int,int>           PII;
typedef map<string,int>         MSI;
typedef set<int>                SI;
typedef set<string>             SS;
typedef map<int,int>            MII;
typedef	pair<double,double>     PDD;

#define PB                      push_back
#define MP                      make_pair
#define X                       first
#define Y                       second
#define FOR(i, a, b)            for(int i = (a); i < (b); ++i)
#define RFOR(i, a, b)           for(int i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b)             memset(a, b, sizeof(a))
#define SZ(a)                   int((a).size())
#define ALL(a)                  (a).begin(), (a).end()
#define RALL(a)                 (a).rbegin(), (a).rend()
#define INF                     (2000000000)

int r[26];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	string s[] = {	"ejp mysljylc kd kxveddknmc re jsicpdrysi", 
					"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
					"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string s2[] = {	"our language is impossible to understand", 
					"there are twenty six factorial possibilities",
					"so it is okay if you want to just give up"};
	
	FOR(i,0,3) {
		string Q = s[i];
		string R = s2[i];
		FOR(j,0,SZ(Q)) {
			if(Q[j]==' ') continue;
			r[Q[j]-'a'] = R[j];
		}
	}

	r['q'-'a'] = 'z';
	r['z'-'a'] = 16+'a';
	/*
	FOR(i,0,26) {
		FOR(j,i+1,26)
			if( r[i]==r[j] )
				cout << "SHIG";
	}
	FOR(i,0,26) {
		cout << i << " " << (char)(i+'a') << " " << (int) (r[i]-'a') << endl;
	}
	*/
	int t;
	cin >> t;
	getline(cin,s[0]);
	FOR(test,0,t) {
		printf("Case #%d: ",test+1);
		string str;
		getline(cin,str);
		FOR(i,0,SZ(str)) {
			if( str[i]==' ') 
				cout << " ";
			else
				cout << ((char) r[str[i]-'a']);
		}
		cout << endl;
	}
    return 0;
}