// Author: Adam Polak
#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <cmath>
#include <ctime>
#include <cstdlib>
using namespace std;
const int NIL = (-1);

#define REP(i,n) for(int i=0;i<(n);i++)
#define SIZE(c) ((int)((c).size()))

#define mp make_pair
#define st first
#define nd second
#define pb push_back

void scase(int case_num) {
    int n,a[50],s=0;
    char c[50];
    scanf("%d",&n);
    REP(i,n) {
        a[i]=-1;
        scanf("%s",c);
        REP(j,n) if (c[j]=='1') a[i]=j;
    }
    REP(i,n) {
        int k=i;
        while(a[k]>i) k++;
        while(k>i) {
            s++;
            swap(a[k-1],a[k]);
            k--;
        }
    }
    printf("Case #%d: %d\n",case_num,s);
}

int main() {
    int cases; 
    scanf("%d",&cases);
    //cin >> cases;
    REP(case_num,cases) 
        scase(case_num+1);
    return 0;
}

    
