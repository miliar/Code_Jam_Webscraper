#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <bitset>
#include <numeric>
#include <algorithm>
#include <functional>
using namespace std;

#define PI 2*acos(0.0)
#define FOR(i,n) for(int i = 0;i<n;++i)
#define setbit(a,b) a|=(1<<b)
#define S1(a) scanf("%d",&a)
#define S2(a,b) scanf("%d %d",&a,&b)
#define S3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define C1(a) __builtin_popcount(a)
#define gcd(a,b) __gcd(a,b)
#define ALL(a) (a.begin(),a.end())

typedef long long LL;
typedef vector<int> vi;
const int INF = (1LL<<31)-1;

int d[10004],l[10004],D,N;

vector< pair<int,int> >v;


int main(){

    freopen("A-large.in","r",stdin);
    freopen("A-large_output.txt","w",stdout);

    int t;
    S1(t);

    for(int ca = 1;ca<=t;++ca){

        S1(N);
        for(int i = 0;i<N;++i)S2( d[i],l[i] );
        S1(D);

        string res[2] = {"NO","YES"};

        bool possible = false;
        v.clear();

        for(int i = N-1;i>=0;--i){

            int mn = INF;
            for(int j = 0;j<v.size();++j)if( (d[v[j].second]-d[i]) <= l[i] && (d[v[j].second]-d[i]) >= v[j].first )
                mn = min( mn , d[v[j].second]-d[i] );

            if( d[i]+l[i] >= D )
                mn = min( mn,D-d[i] );

            v.push_back( make_pair(mn,i) );

        }
        if( v[N-1].first <= d[0] )
            possible = true;

        printf("Case #%d: %s\n",ca,res[possible].c_str());

    }
    return 0;

}
