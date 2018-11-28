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

const int S=128;
bool prison[100000];
int a[S];
int b[S];
int c;
int p,q;
unsigned int inf = -1;

int swap(int *arr, int i, int j) {
    int tmp=arr[i];
    arr[i]=arr[j];
    arr[j]=tmp;
}

int bribe() {
    int rc=0;
    memset(prison,false,sizeof(prison));
    prison[0]=true;
    prison[p+1]=true;
    for(int i=0;i<q;i++) {
        prison[b[i]] = true;
        int pl=b[i]-1;
        int pr=b[i]+1;
        while(!prison[pl--]) {
            rc++;
        }
        while(!prison[pr++]) {
            rc++;
        }
    }
    return rc;
}

int solve() {
    scanf("%d %d\n",&p,&q);
    for(int i=0;i<q;i++) {
        scanf("%d",&a[i]);
    }
    char dummy[10];
    gets(dummy);


    if(q==1) return p-1;

    int x;
    unsigned int min = inf;
    int as[S];
    for(int i=0;i<q;i++) {
        as[i] = i+1;
    }
    do {
        for (int i=0;i<q;i++) {
            b[i] = a[as[i]-1];
        }
        x = bribe();
        if(x < min) min=x;

    } while(next_permutation(as,as+q));
    /*for(int i=0;i<q;i++) {
        for(int j=q-1;j>i;j--) {
            swap(a,i,j);
            x = bribe();
            swap(a,i,j);
            if(x < min) min=x;
        }
    }*/
    
    return min;
}

int main(int argc, char** argv) {
    freopen("../res/C-small-attempt2.in","r",stdin);freopen("../res/C-small-attempt2.out","w",stdout);
    //freopen("../res/C-large.in","r",stdin);freopen("../res/C-large.out","w",stdout);
    //freopen("../res/C.in","r",stdin);freopen("../res/C.out","w",stdout);

    scanf("%d\n",&c);
    
    for(int i=1;i<=c;i++) {
        double rc=solve();
        printf("Case #%d: %.0f\n",i,rc);
    }
    return 0;
}

