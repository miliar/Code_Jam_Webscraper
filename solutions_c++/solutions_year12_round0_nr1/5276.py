#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

const double eps=1e-8;

#define MEM(a) memset(a,0,sizeof(a));
#define FOR(n) for(int i=0;i<n;i++)

char m[500],input[200];

int main()
{
    //freopen("A-small-attempt1.in","r",stdin);
    //freopen("b.out","w",stdout);
    m['e']='o';    m['j']='u';    m['p']='r';
    m[' ']=' ';    m['m']='l';    m['y']='a';
    m['s']='n';    m['l']='g';    m['c']='e';
    m['k']='i';    m['d']='s';    m['x']='m';
    m['v']='p';    m['n']='b';    m['r']='t';
    m['i']='d';    m['b']='h';    m['t']='w';
    m['a']='y';    m['h']='x';    m['w']='f';
    m['f']='c';    m['o']='k';    m['u']='j';
    m['g']='v';    m['q']='z';    m['z']='q';
    int t,cnt=0,len;
    scanf("%d",&t);
    getchar();
    while(t--)
    {
        cnt++;
        gets(input);
        len=strlen(input);
        printf("Case #%d: ",cnt);
        FOR(len)
        {
            printf("%c",m[input[i]]);
        }
        printf("\n");
    }
    return 0;
}
