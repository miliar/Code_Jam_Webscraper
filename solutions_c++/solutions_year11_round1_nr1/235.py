#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>

using namespace std;

#define FOREACH(it,c) for( __typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++) 
#define DOW(i,b,a) for( int i=(b),_a=(a);i>=_a;i--)
#define REP(i,n) FOR(i,0,(n)-1)
#define DEP(i,n) DOW(i,(n)-1,0)
#define all(a) (a).begin() , (a).end()

typedef vector<int> VI ;
typedef vector<string> VS ;
template<class T> inline int size(const T&c) { return c.size(); }  

bool isPossible;
long long n, nTest;
long long Ln, Rn, Mn;
long long A, B, C, D;
long cl1, cl2;

long long gcd(long long x, long long y)
{
    if (x==0 || y==0) return x+y; else return gcd(y, x%y);
}

main()
{
    cin>>nTest;
    REP(kk, nTest)
    {
        cin>>n>>A>>C;
        B=D=100;
        long long x=gcd(A, B);
        A/=x; B/=x;
        cl1=B-A;
        x=gcd(C, D);
        C/=x; D/=x;
        cl2=D-C;        
        cout<<"Case #"<<kk+1<<": ";
        if (B>n || (cl2==0 && cl1!=0) || (C==0 && A!=0)) {cout<<"Broken"<<endl; continue;}
        cout<<"Possible"<<endl;
    }
    return 0;
}   