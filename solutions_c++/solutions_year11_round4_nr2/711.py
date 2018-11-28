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
char mat[600][600];
int Rsum[600][600],Csum[600][600];
int main(){
    int tt,i,j,o,k,t;
    int R,C,D;
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    scanf("%d",&tt);
    for (int tcas = 1;tcas<=tt;tcas++){
        scanf("%d%d%d",&R,&C,&D);
        for (i=1;i<=R;i++)
            scanf("%s",mat[i]+1);
        for (i=1;i<=R;i++)
        Rsum[i][0] = 0;
        for (i=1;i<=R;i++)
            for (j=1;j<=C;j++)
                Rsum[i][j] = Rsum[i][j-1]+mat[i][j]-'0';
        for (j=1;j<=C;j++)
            Csum[0][j] = 0;
        for (j=1;j<=C;j++)
            for (i=1;i<=R;i++)
            Csum[i][j] = Csum[i-1][j]+mat[i][j]-'0';
        int res = 0;
        for (i=R;i>1;i--)
            for (j=C;j>1;j--){
                for (k=2;i-k>=1;k++)
                if (k%2==0){
                    if (k+1<=res) continue;
                    int up = 0;
                    for (t=i-k;t<=i;t++)
                        up+=(i-k/2-t)*(Rsum[t][j]-Rsum[t][j-k-1]);
                    up-=(i-k/2-(i-k))*(mat[i-k][j-k]-'0'+mat[i-k][j]-'0');
                    up-=(i-k/2-i)*(mat[i][j-k]-'0'+mat[i][j]-'0');
                    if (up!=0) continue;
                    up = 0;
                    for (t=j-k;t<=j;t++)
                        up+=(j-k/2-t)*(Csum[i][t]-Csum[i-k-1][t]);
                    up-=(i-k/2-(i-k))*(mat[i-k][j-k]-'0'+mat[i][j-k]-'0');
                    up-=(i-k/2-i)*(mat[i-k][j]-'0'+mat[i][j]-'0');
                    if (up!=0) continue;
                    res = max(res,k+1);
                    //printf("%d %d :%d\n",i,j,k);
                }else {
                    if (k+1<=res) continue;
                    int up = 0,mul = (k+1)/2;
                    for (t=i-k;t<=i;t++,mul==1?mul-=2:mul--)
                        up+=(mul)*(Rsum[t][j]-Rsum[t][j-k-1]);
                    up-=((k+1)/2)*(mat[i-k][j-k]-'0'+mat[i-k][j]-'0');
                    up-=(-(k+1)/2)*(mat[i][j-k]-'0'+mat[i][j]-'0');
                    if (up!=0) continue;
                    up = 0;mul = (k+1)/2;
                    for (t=j-k;t<=j;t++,mul==1?mul-=2:mul--)
                        up+=(mul)*(Csum[i][t]-Csum[i-k-1][t]);
                    up-=((k+1)/2)*(mat[i-k][j-k]-'0'+mat[i][j-k]-'0');
                    up-=(-(k+1)/2)*(mat[i-k][j]-'0'+mat[i][j]-'0');
                    if (up!=0) continue;
                    res = max(res,k+1);
                    //printf("%d %d :%d\n",i,j,k);
                    
                }
            }
        if (res==0) printf("Case #%d: IMPOSSIBLE\n",tcas);
        else printf("Case #%d: %d\n",tcas,res);
        
    }
    //while(1);
}
