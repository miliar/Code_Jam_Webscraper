#include "assert.h"
#include "ctype.h"
#include "float.h"
#include "math.h"
#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "stdarg.h"
#include "time.h"
#include "algorithm"
#include "numeric"
#include "functional"
#include "utility"
#include "bitset"
#include "vector"
#include "list"
#include "set"
#include "map"
#include "queue"
#include "stack"
#include "string"
#include "sstream"
#include "iostream"
#define inf 0x3f3f3f3f
using namespace std;

#define all(v) (v).begin(), (v).end()
typedef long long i64;
template <class T> void make_unique(T& v) {sort(all(v)); v.resize(unique(all(v)) - v.begin());}

int memo[1000][1000];
int f(vector<int> &bag, int i, int w, int a, int b){
    if(i+w == bag.size())
        if(a==b && i>0 && w>0)
            return 0;
        else
            return -1;
    int &best = memo[i][w];
    int t0 = f(bag,i,w+1,a,b^bag[i+w]);
    int t1 = f(bag,i+1,w,a^bag[i+w],b);
    if(t0 > -1) t0 += bag[i+w];
    best = max(t0,t1);
    return best;
}

int main(){
    int t;
    scanf("%d",&t);
    for(int cases=0;cases<t;cases++){
        int n;
        scanf("%d",&n);
        vector<int> bag(n);
        for(int i=0;i<n;i++){
            scanf("%d",&bag[i]);
        }
        int res = f(bag,0,0,0,0);
        if(res != -1) printf("Case #%d: %d\n",cases+1,res);
        else printf("Case #%d: NO\n",cases+1);
    }
    return 0;
}