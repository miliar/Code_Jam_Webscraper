#include <stdio.h>
#include <stdlib.h>
using namespace std;

typedef struct p{ int x;int y;}point;

int compare(const void *a,const void *b){
    point x = *(point *)a;
    point y = *(point *)b;
    return (y.y - x.y);
}

int d[10000][2];
point a[10000];
void solve(){
    int n;
    scanf("%d",&n);
    for (int i=0;i<n;i++) scanf("%d %d",&a[i].x,&a[i].y);
    for (int i=0;i<n;i++) { d[i][0] =0 ;  d[i][1] = 0;}
   // for (int i=0;i<n;i++) printf("%d %d\n",a[i].x,a[i].y);
    int stars = 0;
    qsort(a,n,sizeof(point),compare);
   // for (int i=0;i<n;i++) printf(" %d %d\n",a[i].x,a[i].y);
    while (1) {
        int flag =0;
        for (int i=0;i<n;i++) 
            if ( d[i][1] == 0 && a[i].y <= stars ) { /*printf("%d\n",a[i].y); */flag=1; d[i][1]=1; if ( d[i][0] == 1 ) stars++; else stars+=2;  }
      //  printf("STARS--->%d\n",stars); 
        if ( flag == 0)
        for (int i=0;i<n;i++)
            if ( d[i][0] == 0 &&  d[i][1] == 0 && a[i].x <= stars) { /*printf("%d\n",a[i].x);*/ flag=1;stars++;d[i][0]=1;goto nee;}
nee:
        if ( !flag ) { 
            int ff = 1;
            for (int i=0;i<n;i++) ff = ff & (d[i][1] == 1 );
            if ( !ff ) {
                            printf("Too Bad\n");return;
                        }
            ff = n;
            for (int i=0;i<n;i++) ff += (d[i][0] == 1 );
            printf("%d\n",ff);
            return;
           }

    }
}

int main(){
    int t;
    scanf("%d",&t);
    for (int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
