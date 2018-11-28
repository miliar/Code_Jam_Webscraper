/*
Difficulty:
Type:
Logic:
Links:
*/

//{
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#define mp(a,b) make_pair(a,b)
#define pb push_back
#define vi vector<int>
#define vs vector<string>
#define ll long long
#define ull unsigned long long
#define GI(t) scanf("%d",&(t))
#define init(a,v) memset(a,v,sizeof(a))
#define forn(i,n) for(int i=0;i<(n);i++)
#define INT_MAX 2147483647
#define INT_MIN -2147483647
#define pi acos(-1.0)
//}

using namespace std;

//{Global Var Starts
const unsigned INF = 1<<30;
//}Global Var Ends
map<char,char> hmap;

int main ()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);

    hmap['a']='y';
    hmap['b']='h';
    hmap['c']='e';
    hmap['d']='s';
    hmap['e']='o';
    hmap['f']='c';
    hmap['g']='v';
    hmap['h']='x';
    hmap['i']='d';
    hmap['j']='u';
    hmap['k']='i';
    hmap['l']='g';
    hmap['m']='l';
    hmap['n']='b';
    hmap['o']='k';
    hmap['p']='r';
    hmap['q']='z';
    hmap['r']='t';
    hmap['s']='n';
    hmap['t']='w';
    hmap['u']='j';
    hmap['v']='p';
    hmap['w']='f';
    hmap['x']='m';
    hmap['y']='a';
    hmap['z']='q';
    hmap[' ']=' ';

    int testCase;
    string str;
    scanf("%d", &testCase);
    scanf("%*d");
    int i=1;
    while ( testCase-- ) {
     getline(cin,str);
     for(int j=0;str[j];j++)
      str[j]=hmap[str[j]];
     printf("Case #%d: ",i);
     cout<<str<<endl;
     i++;
   }

	return 0;
}
