#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#define ALL(A)		(A).begin(),(A).end()
#define DUMP(A)    cout<<#A<<"="<<(A)<< endl
#define SIZE(A)    (int)((A).size())
using namespace std;
typedef long long ll;

int main(){
    int T;
    scanf("%d\n",&T);
    for(int ix=1;ix<=T;ix++){
        int C,R,D;
        scanf("%d %d %d\n",&C,&R,&D);
        vector<vector<int> > mas(C,vector<int>(R));
        for(int i=0;i<C;i++){
            for(int j=0;j<R;j++){
                char c;
                scanf("%c",&c);
                mas[i][j]=(int)c-'0';
            }
            scanf("\n");
        }
        int maxk=-1;
        for(int i=0;i<C;i++){
            for(int j=0;j<R;j++){
                for(int k=2;;k++){
                    ll cex=i*2+k,cey=j*2+k;
                    ll mox=0,moy=0;
                    if(i+k<C&&j+k<R){
                        for(int l=i;l<=i+k;l++){
                            for(int m=j;m<=j+k;m++){
                                if(!((l==i&&m==j)||(l==i&&m==j+k)||(l==i+k&&m==j)||(l==i+k&&m==j+k))){
                                    mox+=(l*2-cex)*mas[l][m];
                                    moy+=(m*2-cey)*mas[l][m];
                                }
                            }
                        }
                    }else break;
                    if(mox==0&&moy==0){
                        maxk=max(maxk,k+1);
                    }
                }
            }
        }
        printf("Case #%d: ",ix);
        if(maxk==-1) printf("IMPOSSIBLE\n");
        else printf("%d\n",maxk);
    }
}
