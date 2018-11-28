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
    int n,orderb[101];
    char orderp[101];
    int i,lasto,lastb,steps[101];
    cin>>n;
    lasto=0,lastb=0;
    steps[0]=0;
    orderb[0]=1;
    FOR(i,n) {
        int j=i+1;
        cin>>orderp[j]>>orderb[j];
        if(orderp[j]=='O')
        {
            steps[j]=abs(orderb[lasto]-orderb[j])+1+steps[lasto];
            if(steps[j]<=steps[j-1])
            {
                steps[j]=steps[j-1]+1;
            }
            lasto=j;
        }
        else {
            steps[j]=abs(orderb[lastb]-orderb[j])+1+steps[lastb];
            if(steps[j]<=steps[j-1])
            {
                steps[j]=steps[j-1]+1;
            }
            lastb=j;
        }
    }
    cout<<steps[n]<<endl;
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
