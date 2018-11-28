#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <ctime>
#include <utility>
#include <climits>
#include <cfloat>

using namespace std;
#define readint(n) scanf("%d",&n);
#define readf(n) scanf("%f",&n);
#define readd(n) scanf("%lf",&n);
#define readstr(s) scanf("%s",&s);
int pabs(int n){return (n>0?n:-n);}

int main(){
    int t,n,s,p;
    readint(t);
    for(int ii=1;ii<=t;ii++){
        readint(n);
        readint(s);
        readint(p);
        
        int temp;
        int cnt=0,val=3*p;
        for(int i=0;i<n;i++){
            readint(temp);
            if(temp>=val-2){
                cnt++;
                continue;
            }
            else if(temp>=val-4 && s>0){
                if(temp==0 && p==1){continue;}
                s--;
                cnt++;
            }
        }
        printf("Case #%d: %d\n",ii,cnt);
    }
    return 0;
}
