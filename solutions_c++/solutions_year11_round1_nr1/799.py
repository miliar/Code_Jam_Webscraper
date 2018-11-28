#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <string>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>

#define NAME_VAL(a) cerr<<#a<<" = "<<(a)<<endl;
#define SWAPi(a,b) { int t=a;a=b;b=t; }
#define SWAPd(a,b) { double t=a;a=b;b=t; }
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define FORab(i,a,b) for(i=(a);i<=(b);i++)
#define FOR(i,n) FORab(i,0,(n)-1)
#define FOR1(i,n) FORab(i,1,n)

using namespace std;

int table[102][2];

int gcd(int a,int b)
{
    if(a<b) { int t=a;a=b;b=t; }

    while(b>0)
    {
        int t=b;
        b=a%b;
        a=t;
    }
    return a;
}

void preprocess()
{
    int i,t;
    table[0][0]=1;
    table[0][1]=0;
    FOR1(i,100)
    {
        t=gcd(i,100);
        table[i][0]=100/t;
        table[i][1]=i/t;
    }
}

void main2(int c) {
    long long n;
    int pd,pg;
    cin>>n>>pd>>pg;
    int wd,wg,d,g;
    wd=table[pd][1];
    d=table[pd][0];
    if(wd<=n && d<=n && (pg!=100 || pd==100) && (pg!=0 || pd==0))
    {
        cout<<"Possible"<<endl;
    }
    else
    {
        cout<<"Broken"<<endl;
    }
}

int main() {
    int c,cases;
    preprocess();
    cin>>cases;
    FOR1(c,cases) {
        cout<<"Case #"<<c<<": ";
        main2(c);
    }
    return 0;
}
