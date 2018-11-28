/* 
 * File:   main.cpp
 * Author: paid
 *
 * Created on September 11, 2009, 4:29 PM
 */


#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long LL;
const int S=100;
char a[S];
int c;


double solve() {
    double rc = 0;
    scanf("%s\n",a);

    map<char,int> m;
    int t=1;
    int n=1;
    for(int i=0;a[i]!='\0';i++) {
        if(m.find(a[i]) == m.end()) {
            if(t++ == 2) {
                m[a[i]] = 0;
            } else {
                m[a[i]] = n;
                n++;
            }
        }
    }
    int b=n;
    int k=1;
    int len=strlen(a);

    for(int i=len-1;i>=0;i--) {
        rc += m[a[i]] * k;
        k = k*b;
    }

    return rc;
}

int main(int argc, char** argv) {
    freopen("../res/A-small-attempt0.in","r",stdin);freopen("../res/A-small-attempt0.out","w",stdout);
    //freopen("../res/A.in","r",stdin);freopen("../res/A.out","w",stdout);

    scanf("%d\n",&c);
    
    for(int i=1;i<=c;i++) {
        double rc=solve();
        printf("Case #%d: %.0f\n",i,rc);
    }
    return 0;
}

