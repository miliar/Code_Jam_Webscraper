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

string a = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
string b = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

char Map(char c){

    for(int i = 0;i<a.size();++i)if( a[i] == c )
        return b[i];

    if( c == 'q' )
        return 'z';
    return 'q';

}

int main(){

    freopen("A.txt","r",stdin);
    freopen("A_Out.txt","w",stdout);
    int t;
    S1(t);
    scanf("%*c");

    char inpt[105];
    for(int ca = 1;ca<=t;++ca){

        gets(inpt);
        printf("Case #%d: ",ca);
        for(int i = 0;inpt[i];++i)
            printf("%c",Map(inpt[i]));
        puts("");

    }

	return 0;

}
