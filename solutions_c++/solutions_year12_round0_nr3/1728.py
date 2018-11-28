
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

int numd(int a) {
    int i=0;
    while(a) {
        a/=10;
        i++;
    }
    return i;
}

//#define SMALL
#define LARGE
int main() {
#ifdef SMALL
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w+",stdout);
#endif
#ifdef LARGE
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w+",stdout);
#endif
    
    int n;
    cin>>n;
    for(int i=1;i<=n;++i) {
        int a,b,c,d=0;
        cin>>a>>b;
        int db=numd(b);
        if(b<=9) {
        } else {
            for(int j1=a;j1<=b;++j1) {
                vector<int> v;
                for(int k=1;k<=db-1;++k) {
                    int j2=j1;
                    c=j2%int(pow(10.0,k));
                    j2=j2/pow(10.0,k)+c*pow(10.0,db-k);
                    if(j2>=a&&j2<=b&&j2!=j1) {
                        v.push_back(j2);
                        sort(v.begin(), v.end());
                        v.erase(unique(v.begin(), v.end()), v.end());
                    }
                }
                d+=v.size();
            }
        }
        printf("Case #%d: %d \n",i,d/2);
    }
    return 0;
}
