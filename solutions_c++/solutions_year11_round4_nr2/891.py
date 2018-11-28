#include <algorithm>
#include <iostream>
#include <sstream>
#include <string.h>
#include <string>
#include <queue>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <vector>
#include <map>
#include <math.h>
#include <stdio.h>
using namespace std;

int main(){
    int T;
    scanf("%d",&T);
    for (int x1=0;x1<T;x1++){
        int c,r,d;
        char s[15][15];
        scanf("%d %d %d",&r,&c,&d);
        for (int i=0;i<r;i++) scanf("%s",s[i]);

        bool b=false;
        int res;
        for (int k=min(c,r);k>=3;k--){
            //printf("%d\n",k);
            for (int i=0;i<r-k+1;i++){
            for (int j=0;j<c-k+1;j++){
                int numx=0;
                int numy=0;
                for (int x=i;x<i+k;x++)
                for (int y=j;y<j+k;y++){
                    if (x==i&&y==j) continue;
                    if (x==i&&y==j+k-1) continue;
                    if (x==i+k-1&&y==j) continue;
                    if (x==i+k-1&&y==j+k-1) continue;
                    if (k%2==1){
                        numx=numx+(d+s[x][y]-'0')*(i+k/2-x);
                        numy=numy+(d+s[x][y]-'0')*(j+k/2-y);
                       }
                    if (k%2==0){
                        numx=numx+(d+s[x][y]-'0')*(2*i+k-1-2*x);
                        numy=numy+(d+s[x][y]-'0')*(2*j+k-1-2*y);
                        }
                    }
                //if (i==1&&j==1) printf("%d %d %d\n",k,numx,numy);
                if (numx==0&&numy==0) {res=k; b=true; break;}
                }
                if (b) break;
                }
            if (b) break;
            }
        if (!b) printf("Case #%d: IMPOSSIBLE\n",x1+1); else printf("Case #%d: %d\n",x1+1,res);
        }

    return 0;
    }
