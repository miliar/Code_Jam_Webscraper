#include <stdio.h>
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdio>
#include <sstream>
#include <ctype.h>
#include <math.h>

#define print(a) cout<< a <<endl
#define print2(a,b) cout<< a <<" "<< b <<endl
#define print3(a,b,c) cout<< a <<" "<< b <<" "<< c <<endl
#define pb push_back
#define popb pop_back
#define mem(name, x) memset(name, x, sizeof(name))
#define MAX 10010
#define PN 1200000
#define ll long long
#define rep(i,n) for(i=0;i<(int)(n);i++)
#define rep2(i,n) for(i=1; i<=(int)(n); i++)
#define SZ(x) (int)x.size()
#define PI (2*acos(0))
#define FST first
#define SND second
#define PQ priority_queue
#define LOG(x,BASE) (log10(x)/log10(BASE))
#define INFI 1<<30

using namespace std;

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    string input, output;
    int t, kase=0, i, j, k;
    vector <string> v1, v2;
    char x, y;
    map <char, char> mp;
    mp.clear(); v1.clear(); v2.clear();
    mp['z'] = 'q', mp['q'] = 'z';
    v1.pb("ejp mysljylc kd kxveddknmc re jsicpdrysi");
    v1.pb("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
    v1.pb("de kr kd eoya kw aej tysr re ujdr lkgc jv");
    v2.pb("our language is impossible to understand");
    v2.pb("there are twenty six factorial possibilities");
    v2.pb("so it is okay if you want to just give up");
    for(i=0; i<3; i++)
        for(j=0; j<v2[i].size(); j++)
        {
            x = v1[i][j]; y = v2[i][j];
            mp[x] = y;
        }
    scanf("%d ", &t);
    while(t--)
    {
        input.clear();
        getline(cin, input);
        printf("Case #%d: ", ++kase);
        for(i=0; i<input.size(); i++)
        {
            x = input[i];
            cout << mp[x];
        }
        printf("\n");
    }
    return 0;
}
