//#pragma comment(linker, "/stack:1000000")

#include <ctime>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>

using namespace std;

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)

#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ABS(A) ((A) < 0 ? (-(A)) : (A))
#define ALL(V) V.begin(), V.end()
#define SIZE(V) (int)V.size()
#define pb push_back
#define mp make_pair
#define EPS 1e-7
#define Pi 3.14159265358979
#define FILL(a,v) memset(a,v,sizeof(a))

typedef long long Long;
typedef unsigned long long ULong;
typedef unsigned int Uint;
typedef unsigned char Uchar;
typedef vector <int> VI;
typedef pair <int, int> PII;

map<char, char> keys;
map<char, char> fkeys;

string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
string s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
string s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

string r1 = "our language is impossible to understand";
string r2 = "there are twenty six factorial possibilities";
string r3 = "so it is okay if you want to just give up";

void proc(string s, string r)
{
	REP(i, s.length())
		//if(r[i] != ' ')
		{
			//keys[r[i]] = s[i];
			keys[s[i]] = r[i];
		}
}

int main(int argc, char** argv)
{
	ios_base::sync_with_stdio(false);
	proc(s1, r1);
	proc(s2, r2);
	proc(s3, r3);
	keys['z'] = 'q';
	keys['q'] = 'z';
	string s;
	int t;
	cin>>t;
	getline(cin,s);
	FOR(i,1,t+1)
	{
		getline(cin, s);
		REP(j, s.length())
			s[j] = keys[s[j]];
		printf("Case #%d: %s\n", i, s.c_str());
	}
	return 0;
}