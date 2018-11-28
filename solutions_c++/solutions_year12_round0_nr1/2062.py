#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <utility>
#include <math.h>
#include <cstdlib>
#include <memory.h>
#include <queue>

#define pb push_back
#define i64 long long
#define mp make_pair
#define pii pair <int,int>
#define vi vector <int>
#define vii vector <pii>
#define f first
#define s second
#define foran(i,a,b) for (int i=a;i<(int)b;i++)
#define forn(i,n) for (int i=0;i<(int)n;i++)
#define ford(i,n) for (int i=(int)n-1;i>=0;i--)

const double eps = 1e-9;
const int int_inf = 2000000000;
const i64 i64_inf = 1000000000000000000LL;
const double pi = acos(-1.0);
 
using namespace std;
bool let(char c) { return (c >= 'a' && c <= 'z'); }

char to[26] = 
 {'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
char t[26];


int main() {
//  freopen("input.txt","r",stdin);
//  freopen("output.txt","w",stdout);
  int tests; scanf("%d\n",&tests);
  for (int i='a'; i<='z'; i++) t[(int)to[i-'a']] = (char)i;
  
  for (int test=1; test<=tests; test++)
  {
	string s; getline(cin,s);
	printf("Case #%d: ",test);
	forn(j,s.length())
		if (let(s[j])) putchar(t[s[j]]); else putchar(s[j]);
	puts("");
  }
  
  return 0;
}