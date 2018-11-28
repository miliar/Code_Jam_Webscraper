#include<iostream>
using namespace std;
struct pt
{
double x,y;
};
double square(pt a,pt b,pt c)
{
return (a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y));
}
bool inter(double a,double b,double c,double d)
{
return (max(a,b)>=min(c,d) && max(c,d)>=min(a,b));
}
bool intersect(pt a,pt b,pt c,pt d)
{
double s11=square(a,b,c),s12=square(a,b,d),s21=square(c,d,a),s22=square(c,d,b);
if (s11==0 && s12==0 && s21==0 && s22==0)
{
return (inter(a.x,b.x,c.x,d.x) && inter(a.y,b.y,c.y,d.y));
}
else
{
return ((s11*s12<=0) && (s21*s22<=0));
}
}
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int t,n,t2,i,j,k=0;
pt a[1005],b[1005];
cin>>t;
for(t2=1;t2<=t;t2++)
{
cin>>n;
for(i=1;i<=n;i++)
{
cin>>a[i].y>>b[i].y;
a[i].x=0;
b[i].x=100;
}
for(i=1;i<n;i++)
{
for(j=i+1;j<=n;j++)
{
if(intersect(a[i],b[i],a[j],b[j]))
{
k++;
}
}
}
cout<<"Case #"<<t2<<": "<<k<<endl;
k=0;
}
return 0;
}