
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

int min0(int a) {
    if(a<=0)
        return 0;
    else
        return a;
}

//#define SMALL
#define LARGE
int main() {

#ifdef LARGE
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w+",stdout);
#endif
    
    int n;
    cin>>n;
    for(int i=1;i<=n;++i) {
        int a,b,c,d=0,e=0,f=0;
        cin>>a>>b>>c;
        int s[a];
        for(int j=0;j<a;++j)
            cin>>s[j];
        for(int j=0;j<a;++j) {
            if(s[j]>=c+2*min0(c-1))
                ++d;
            else if(s[j]==c+2*min0(c-2)||s[j]==c+min0(c-1)+min0(c-2))
                ++e;
        }
        if(e<b)
            f=d+e;
        else
            f=d+b;
        printf("Case #%d: %d \n",i,f);
    }
    return 0;
}
