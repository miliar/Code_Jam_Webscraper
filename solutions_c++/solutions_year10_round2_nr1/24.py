
//Tomasz Kulczyński
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <numeric>
#include <cmath>
#include <cstdlib>
using namespace std;

#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef double D;
typedef long double ld;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
int cond = 1;
#define db(x) {if(cond){cerr << __LINE__ << " " << #x << " " << x << endl; } }
#define dbv(x) {if(cond){cerr << __LINE__ << " " << #x << ": "; FORE(__i,x) cerr << *__i << " "; cerr << endl;} }

bool lt(string a, string b)
{
    return a.size() < b.size();
}

string s[113];
char buf[113];
map<string,int> ma[51013];

void test()
{
    int n,m;
    scanf("%d %d",&n,&m);
    REP(i,51013) ma[i].clear();
    REP(i,n) 
    {
        scanf("%s",buf);
        s[i] = buf;
    }
    sort(s,s+n,lt);
    int nr = 1;
    REP(i,n)
    {
        string x;
        s[i] += '/';
        int g = 0;
        for(int j = 1; j<SIZE(s[i]); j++) 
            if(s[i][j]=='/') 
            {
                if(!ma[g].count(x))
                    ma[g][x] = nr++;
                g = ma[g][x];
                x="";
            }
            else x += s[i][j];
    }
    int ret = 0;
    REP(i,m) 
    {
        scanf("%s",buf);
        buf[strlen(buf)+1] = 0;
        buf[strlen(buf)] = '/';
        string x;
        int g = 0;
        for(int j = 1; buf[j]; j++) 
            if(buf[j]=='/') 
            {
                if(!ma[g].count(x))
                    ma[g][x] = nr++, ret++;
                g = ma[g][x];
                x="";
            }
            else x += buf[j];
    }
    if(nr>50000) puts("DUPA");
    printf("%d\n",ret);
}

int main()
{
    int dd,cas;
    scanf("%d",&dd);
    FOR(cas,1,dd)
    {
        printf("Case #%d: ",cas);
        test();
    }
    return 0;
}
