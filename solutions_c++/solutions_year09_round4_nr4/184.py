#include<stdio.h>
#include<math.h>
int i,n,cases,t;
int a[10],b[10],r[10];
double r1,r2,r3,ans;
double getdis(int i,int j)
{
    return sqrt((a[i]-a[j])*(a[i]-a[j])+(b[i]-b[j])*(b[i]-b[j]));      
}
double max(double x,double y)
{
    if(x>y) return x;
    return y;
}
double min(double x,double y)
{
    if(x<y) return x;
    return y;
}
int main()
{
    //freopen("D-small-attempt0.in","r",stdin);
    //freopen("out.txt","w",stdout);
    scanf("%d",&cases);
    for(t=1;t<=cases;t++)
    {
    	scanf("%d",&n);
    	for(i=1;i<=n;i++)
        	scanf("%d%d%d",&a[i],&b[i],&r[i]);
        if(n==1) ans = r[1];
    	if(n==2) ans = max(r[1],r[2]);
    	r1=max(r[3],(getdis(1,2)+r[1]+r[2])/2);
    	r2=max(r[2],(getdis(1,3)+r[1]+r[3])/2);
    	r3=max(r[1],(getdis(2,3)+r[2]+r[3])/2);
    	ans = min(r1,min(r2,r3));
        printf("Case #%d: %.6lf\n",t,ans);
    }
    return 0;
}
