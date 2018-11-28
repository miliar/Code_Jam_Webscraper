/*
    ID:
    PROG:
    LANG:C++
*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <string>
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
#include <cstring>
using namespace std;

int a[700][700],T,r,c,d,ans;
//int w1[500][500][500],w2[500][500][500];
//int ct1[500][500][500],ct2[500][500][500];
char st[1000];
double m,tx,ty;
int main(){
    freopen("b-small-0.in","r",stdin);
    freopen("b-small-0.out","w",stdout);
    scanf("%d",&T);
    for(int cs=1;cs<=T;++cs){
        scanf("%d%d%d",&r,&c,&d);
        ans=0;
        for(int i=0;i<r;++i){
            scanf("%s",st);
            for(int j=0;j<c;++j)a[i][j]=st[j]-'0';
        }
        for(int l=3;l<=c;++l)
        for(int i=0;i<r;++i)
            for(int j=0;j<c;++j)
                {
                    if(i+l>r || j+l>c)break;
                    double x=0,y=0,z=0;
                    for(int u=0;u<l;++u)
                        for(int v=0;v<l;++v)
                        if(!((u==0&& v==0) || (u==0&&v==l-1)
                             || (u==l-1&&v==0) || (u==l-1&&v==l-1))){
                            x+=a[i+u][j+v]*(i+u);
                            y+=a[i+u][j+v]*(j+v);
                            z+=a[i+u][j+v];
                            //if(i+u==4 && j+v==4)cout<<"fool";
                        }
                    if(z==0 ||abs(x/z-(i+double(l-1)/2))<1e-7
                       && abs(y/z-(j+double(l-1)/2))<1e-7)
                       ans=l;
                }
        /*for(int i=0;i<r;++i)
            for(int j=0;j<c;++j){
                w1[i][j][0]=0;
                for(int l=1;l<=c-j;++l){
                    w1[i][j][l]=w1[i][j][l-1]+a[i][j+l-1];
                    ct1[i][j][l]=(ct1[i][j][l-1]*w1[i][j][l-1]+a[i][j+l-1]*j);
                }
            }
        for(int i=0;i<r;++i)
            for(int j=0;j<c;++j){
                w2[i][j][0]=0;
                for(int l=1;l<=r-j;++l){
                    w2[i][j][l]=w2[i][j][l-1]+a[i+l-1][j];
                    ct2[i][j][l]=(ct2[i][j][l-1]*w2[i][j][l-1]+a[i+l-1][j]*i);
                }
            }
        for(int x0=1;x0<r-1;++x0)
            for(int y0=1;y0<c-1;++y0){

            }*/


        printf("Case #%d: ",cs);
        if(ans<3)printf("IMPOSSIBLE");
            else printf("%d",ans);
        printf("\n");
    }
    //system("pause");
    return 0;
}
