#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <ctype.h>
#include <bitset>
#include <assert.h>

using namespace std;

#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<(b); i++)
#define IFOR(i, a, b) for(int i=(a); i>=(b); i--)
#define FORD(i, a, b, c) for(int i=(a); i<(b); i+=(c))

#define SS ({int x;scanf("%d", &x);x;})
#define SI(x) ((int)x.size())
#define PB(x) push_back(x)
#define MP(a,b) make_pair(a, b)
#define SORT(a) sort(a.begin(),a.end())
#define ITER(it,a) for(typeof(a.begin()) it = a.begin(); it!=a.end(); it++)
#define ALL(a) a.begin(),a.end()
#define INF 1000000000
#define V vector
#define S string
#define FST first
#define SEC second

typedef V<int> VI;
typedef V<S> VS;
typedef long long LL;
typedef pair<int, int> PII;

int arr[300],a;

int main()
{
    //freopen("file.in","r",stdin);
    freopen("o.o","w",stdout);
    arr['a']='y';
arr['b']='n';
arr['c']='f';
arr['d']='i';
arr['e']='c';
arr['f']='w';
arr['g']='l';
arr['h']='b';
arr['i']='k';
arr['j']='u';
arr['k']='o';arr['p']='v';
arr['l']='m';
arr['m']='x';
arr['n']='s';
arr['o']='e';
arr['q']='z';
arr['r']='p';
arr['s']='d';
arr['t']='r';
arr['u']='j';
arr['v']='g';
arr['w']='t';
arr['x']='h';
        arr['y']='a';
        arr['z']='q';
        //int t=SS;
        int t;
        cin>>t;
        cin.ignore();
        REP(cases,t)
        {
            char s[1000];
            gets(s);
            for(int i=0;s[i]!='\0';i++)
                if(s[i]!=' ')
                {
                    //s[i]=arr[s[i]];
                    //REP(m,300)
                    for( int m='a';m<='z';m++)
                        if(arr[m]==s[i]){
                        s[i]=m;break;}
                }
            printf("Case #%d: %s\n",cases+1,s);
        }
    return 0;
}
