#include<stdio.h>
#include<math.h>

int n;
double x[50], y[50], r[50];

void input()
{
    int i;
    scanf("%d", &n);
    for(i=0; i<n; i++) scanf("%lf%lf%lf", &x[i], &y[i], &r[i]);
}

double dis(int i, int j)
{
    return sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]));
}

double solve()
{
    double s1, s2, s3, ret, tmp;
    
    s1=(dis(0, 1)+r[0]+r[1])/2;
    tmp=r[2];
    if(tmp>s1) s1=tmp;
    
    s2=(dis(0, 2)+r[0]+r[2])/2;
    tmp=r[1];
    if(tmp>s2) s2=tmp;

    s3=(dis(1, 2)+r[1]+r[2])/2;
    tmp=r[0];
    if(tmp>s3) s3=tmp;
    
    ret=s1;
    if(s2<ret) ret=s2;
    if(s3<ret) ret=s3;
    
    return ret;
}

int main()
{
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);
    
    int ct, cc;
    double ans;
    
    scanf("%d", &ct);
    for(cc=1; cc<=ct; cc++){
        input();
        if(n==1) ans=r[0];
        if(n==2){
            ans=r[0];
            if(r[1]>ans) ans=r[1];
        }
        else ans=solve();
        
        printf("Case #%d: %lf\n", cc, ans);
    }
    
    return 0;
}
