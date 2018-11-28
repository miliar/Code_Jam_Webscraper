#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>

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
#define FOR(i,n) for(i=0;i<(n);i++)

using namespace std;

void main2() {
    int i,n,t,sum=0;
    cin>>n;
    FOR(i,n)
    {
        cin>>t;
        if(t!=i+1) sum++;
    }
    cout<<sum<<endl;
}

int main() {
    int c,cases;
    cin>>cases;
    FOR(c,cases) {
        cout<<"Case #"<<c+1<<": ";

        main2();
    }
    return 0;
}
