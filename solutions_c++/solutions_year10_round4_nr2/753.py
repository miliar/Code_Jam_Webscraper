#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <list>
using namespace std;

#define	REP(i,n)	for(int (i) = 0; (i) < (n); (i)++)


int P;
int a[2050];
int match[12][2050];
bool should[12][2050];


int main(){
    int T,cas;
    int i,j;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    cin>>T;
    for(cas = 1;cas <=T;++cas){
        cin>>P;
        for(i=0;i<(1<<P);++i) cin>>a[i];
        for(i=0;i<P;++i) for(j=0;j<(1<<(P-i-1));++j) cin>>match[i][j];
        memset(should,0,sizeof(should));
        for(i=0;i<(1<<P);++i){
            int cur = i/2;
            for(j=0;j<P;++j){
                if(a[i]<=j){
                    should[j][cur] = true;
                }
                cur = cur/2;
            }
        }
        int res = 0;
        for(i=0;i<P;++i) for(j=0;j<(1<<(P-i-1));++j){
            if(should[i][j]) res+=match[i][j];
        }
        cout<<"Case #"<<cas<<": ";
        cout<<res<<endl;
        
    }
    return 0;
}
