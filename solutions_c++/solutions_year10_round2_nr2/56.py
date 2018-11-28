#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>

using namespace std;
int ntest;
int N,K,B,T;
int x[100],v[100];
int main(){
    freopen("B-large.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&ntest);
    for(int test=0; test<ntest; test++){
        printf("Case #%d: ",test+1);   
        scanf("%d %d %d %d",&N,&K,&B,&T);
        for(int i=0; i<N; i++)
            scanf("%d",&x[i]);
        for(int i=0; i<N; i++)
            scanf("%d",&v[i]);    
        int res=0;
        int c=0;
        for(int i=N-1; i>-1; i--){
            if(c==K) break;
            if(T*v[i]+x[i]>=B){ res+= N-1-i-c; c++; }            
        }        
        if(c<K) printf("IMPOSSIBLE\n");
        else printf("%d\n",res);
    }
    return 0;
}
