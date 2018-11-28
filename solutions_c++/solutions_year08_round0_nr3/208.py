#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <complex>
using namespace std;
typedef complex<double> point;
#define eps 1e-8
#define cross(a,b) ((conj(a)*(b)).imag())
#define dot(a,b) ((conj(a)*(b)).X)
#define normalize(v) ((v)/length(v))
#define X real()
#define Y imag()
#define vect(a,b) (b)-(a)
#define length(V) (hypot((V).X,(V).Y))
#define PI 3.1415926535897932384626433832795
int comp(double a,double b)
{
    if(fabs(a-b)<eps)
        return 0;
    return a>b?1:-1;
}
bool pointOnRay(const point &A,const point &B,const point &P)
{
	if(length(P-A)<eps) return true;
	return fabs(length(normalize(B-A)-normalize(P-A)))<eps;
}
bool pointSeg(const point &p1,const point &p2,const point &P)
{
    return pointOnRay(p1,p2,P)&&pointOnRay(p2,p1,P);
}
double f,R,t,r,g;
double sum;
point ZERO(0,0);
bool lineCircleInter(const point &p0,const point &p1,point &res)
{
    point r1,r2;
    double a=dot(p1-p0,p1-p0);
    double b=2*dot(p1-p0,p0-ZERO);
    double c=dot(p0-ZERO,p0-ZERO)-R*R;
    double x=b*b-4*a*c;
    if(x<-eps)return false;
    if(x<0) x=0; 
    double t1=(-b+sqrt(x))/(2*a);
    double t2=(-b-sqrt(x))/(2*a);
    r1=p0+t1*(p1-p0);
    r2=p0+t2*(p1-p0);
    if(!pointSeg(p0,p1,r1) && !pointSeg(p0,p1,r2))
        return false;
    if(pointSeg(p0,p1,r1))
        res=r1;
    else
        res=r2;
    return true;
}
double getAng(point b,point c)
{
    point a=ZERO;
    point va,vb;
    va=vect(a,b);
    vb=vect(a,c);
    double ar1=dot(va,vb)/(length(va)*length(vb));
    double an=acos(ar1);
    if(comp(an,0)==-1)
        an+=2*PI;
    return an;
}
void calc(double X_,double Y_)
{
    for(double x=X_;comp(hypot(x,Y_),R)<0;x+=(g+r+2*f))
        for(double y=Y_;comp(hypot(x,y),R)<0;y+=(g+r+2*f))
        {
            if(comp(hypot(x+g,y+g),R)<=0)
                sum+=g*g;
            else
            {
                point a(x,y),b(x+g,y),c(x,y+g),d(x+g,y+g);
                point r1,r2;
                if(lineCircleInter(a,c,r1) && lineCircleInter(b,d,r2))
                {
                    double dd=fabs((cross(r1,r2)+cross(r2,b)+cross(b,a)+cross(a,r1))/2);
                    double ang=getAng(r2,r1);
                    double ar=(R*R*ang/2)-fabs((cross(r1,r2)+cross(r2,ZERO)+cross(ZERO,r1))/2);
                    sum+=(dd+ar);
                }
                else if(lineCircleInter(d,c,r1) && lineCircleInter(b,d,r2))
                {
                    double dd=fabs((cross(r1,r2)+cross(r2,b)+cross(b,a)+cross(a,c)+cross(c,r1))/2);
                    double ang=getAng(r2,r1);
                    double ar=(R*R*ang/2)-fabs((cross(r1,r2)+cross(r2,ZERO)+cross(ZERO,r1))/2);
                    sum+=(dd+ar);
                }
                else if(lineCircleInter(a,c,r1) && lineCircleInter(b,a,r2))
                {
                    double dd=fabs((cross(r1,r2)+cross(r2,a)+cross(a,r1))/2);
                    double ang=getAng(r2,r1);
                    double ar=(R*R*ang/2)-fabs((cross(r1,r2)+cross(r2,ZERO)+cross(ZERO,r1))/2);
                    sum+=(dd+ar);
                }
                else if(lineCircleInter(a,b,r1) && lineCircleInter(c,d,r2))
                {
                    double dd=fabs((cross(a,r1)+cross(r1,r2)+cross(r2,c)+cross(c,a))/2);
                    double ang=getAng(r2,r1);
                    double ar=(R*R*ang/2)-fabs((cross(r1,r2)+cross(r2,ZERO)+cross(ZERO,r1))/2);
                    sum+=(dd+ar);
                }
            }
        }
}
int main()
{
    //point A(0,0),B(5,0),C(5,5),D(0,5);
    //double dd=cross(A,D)+cross(D,C)+cross(C,B)+cross(B,A);
    //cout<<dd<<endl;
    //system("pause");
    freopen("C-large.in","rt",stdin);
    freopen("b.txt","wt",stdout);
    int N;
    scanf("%d",&N);
    for(int Z=0;Z<N;Z++)
    {
        scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
        double ar=R*R*PI;
        R-=(f+t);
        g-=2*f;
        r*=2;
        sum=0;
        if(comp(g,0)>0)
            calc(r/2+f,r/2+f);
        sum*=4;
        printf("Case #%d: %.6lf\n",Z+1,(ar-sum)/ar);
    }
    return 0;
}
