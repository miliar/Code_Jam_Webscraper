#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cctype>
#include <cmath>

#include <algorithm>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <cstring>
#include <string>
#include <set>
#include <map>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define mp make_pair
#define pb push_back

typedef long long ll;

int main()
{
  freopen("c.in", "r", stdin);
  freopen("c.out", "w", stdout);
  int n;
  scanf("%d\n", &n);
  string fraze = "welcome to code jam";
  int frlen = fraze.length();
  int mod = 10000;
  char str[600];

  int table[600][20];
  forn(tests, n)
  {
     gets(str);
//     printf("%s\n", str);
     int m = strlen(str);
     forn(i, m+2)
       forn(j, 20)
         table[i][j] = 0;
     forn(i, m+2)
       table[i][0]  = 1;

     forn(i, m)
       forn(j, frlen)
         if (str[i] == fraze[j])
           table[i+1][j+1] = (table[i][j+1]+table[i][j]) %mod;
         else
           table[i+1][j+1] = (table[i][j+1]) %mod;
    int st = table[m][frlen];
    stringstream ans;
    ans<<st;
    string ttt = ans.str();
	while (ttt.length()<4) ttt = '0'+ttt;
	cout<<"Case #"<<tests+1<<": "<<ttt<<endl;
    //printf("Case #%d: %d\n", tests+1, table[m][frlen]);         	         
  }
  return 0;
}

