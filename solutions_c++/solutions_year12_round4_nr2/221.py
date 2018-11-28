#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
using namespace std;
int tt,n,w,l,t,ok;
long long xx,yy;
double x,y;
double anx[2000],any[2000],px[2000],py[2000];
struct ar{double r;int num;} a[2000];
bool cmp(ar a,ar b){
    return (a.r>b.r);
}
int main(){
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    srand(time(NULL));
    cin>>t;
    fo(tt,1,t){
        cin>>n>>w>>l;
        fo(i,1,n) {
            scanf("%lf",&a[i].r);
            a[i].num=i;
        }
        sort(a+1,a+n+1,cmp);
        fo(i,1,n){
            ok=0;
            while (!ok){
                
                xx=rand();
                xx=xx*32767%w;
                x=xx/1.0;
                
                yy=rand();
                yy=yy*32767%l;
                y=yy/1.0;
                ok=1;
                fo(j,1,i-1){
                    if (sqrt((x-px[j])*(x-px[j])+(y-py[j])*(y-py[j]))<a[i].r+a[j].r)
                    {ok=0;break;}
                }
            }
            px[i]=x;
            py[i]=y;
        }
        printf("Case #");
        printf("%d",tt);
        printf(": ");
        fo(i,1,n) {
            anx[a[i].num]=px[i];
            any[a[i].num]=py[i];
        }
        fo(i,1,n) {
            printf("%.5lf %.5lf ",anx[i],any[i]);
        }
        cout<<endl;
    }
}
