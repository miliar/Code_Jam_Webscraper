#include <stdio.h>
#include <algorithm>
#include <math.h>

using namespace std;

double x[5],y[5];
double r[5];
int cp,tn;
int n;
double ans;
double dis(int p1,int p2){
       return sqrt((x[p1]-x[p2])*(x[p1]-x[p2])+(y[p1]-y[p2])*(y[p1]-y[p2]));
}
int main(){
    int i;
    freopen("D.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&tn);
    for (cp=1;cp<=tn;cp++){
        scanf("%d",&n);
        for (i=0;i<n;i++) scanf("%lf %lf %lf",x+i,y+i,r+i);
        ans=0;
        if (n==1) ans=r[0];else
        if (n==2) ans=max(r[0],r[1]);else{
           ans=max(r[0],(dis(1,2)+r[1]+r[2])/2);
           ans=min(ans,max(r[1],(dis(0,2)+r[0]+r[2])/2));
           ans=min(ans,max(r[2],(dis(0,1)+r[0]+r[1])/2));
        }
        printf("Case #%d: %.6lf\n",cp,ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
