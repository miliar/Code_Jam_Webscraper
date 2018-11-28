#include <vector>
#include <list>
#include <map>
#include <set>
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

#define maxP 1000000
#define SQRT 1000

bool notprime[maxP+1];
long long n;

void init(){
    int i,j;
    for(i=2;i<=SQRT;i++){
        if(notprime[i]==0){
            for(j=i*i;j<=maxP;j=j+i){
                notprime[j]=true;
            }
        }
    }
}

int main(){
    freopen("C-large(1).in","r",stdin);
    freopen("C-large(1).out","w",stdout);
    int cas,Te=1;
    init();
    scanf("%d",&cas);
    while( cas-- ){
        scanf("%I64d",&n);
        if(n==1){
            printf("Case #%d: %I64d\n",Te++,0);
            continue;
        }
        long long s=1,i,j,x;
        for(i=2;i*i<=n;i++){
            if(notprime[i]==0){
                x=i*i;
                for(j=0;x<=n;j++){
                    x=x*i;
                }
                s=s+j;
            }
        }
		printf("Case #%d: %I64d\n",Te++,s);
    }
    return 0;
}
