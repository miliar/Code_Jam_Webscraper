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

string toStr(int n){
    ostringstream os;
    os<<n;
    return os.str();
}

bool canMake( int a,int b ){

    string aa,bb;
    aa = toStr(a);
    bb = toStr(b);

    if( aa.size() != bb.size() )
        return false;

    for(int i = 0;i<=aa.size();++i)
        if( aa.substr(i) + aa.substr(0,i) == bb )
            return true;

    return false;

}

int main(){

    freopen("Csmall.txt","r",stdin);
    freopen("Csmall_Out.txt","w",stdout);
    int t;
    S1(t);

    for(int ca = 1;ca<=t;++ca){

        int A,B;
        S2(A,B);

        int res = 0;
        for(int a = A;a<=B;++a)
            for(int b = a+1;b<=B;++b)
                if( canMake(a,b) )
                    ++res;

        printf("Case #%d: %d\n",ca,res);

    }

	return 0;

}
