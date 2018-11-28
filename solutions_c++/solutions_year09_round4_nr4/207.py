#include<iostream>
#include<cmath>
using namespace std;

const double tol=1e-9;
struct pt { double x,y; };
double dot(const pt& a,const pt& b) { return a.x*b.x+a.y*b.y; }
double mag(const pt& a) { return sqrt(dot(a,a)); }
pt operator*(double d,pt a) { a.x*=d; a.y*=d; return a; }
pt operator/(pt a,double d) { a.x/=d; a.y/=d; return a; }
pt operator-(pt a,const pt& b) { a.x-=b.x; a.y-=b.y; return a; }
pt operator+(pt a,const pt& b) { a.x+=b.x; a.y+=b.y; return a; }
double dist(const pt& a,const pt& b) { return mag(a-b); }
struct circle { pt c; double r; };

circle cover(circle a,circle b)
{ double r=dist(a.c,b.c)/2+(a.r+b.r)/2;
  pt d=b.c-a.c;
  circle rv={a.c+(r-a.r)*(d/mag(d)),r};
  return rv;
}

double calc(circle arr[],int n)
{ if(n==1) return arr[0].r;
  if(n==2) return max(arr[0].r,arr[1].r);
  double d=max(arr[0].r,cover(arr[1],arr[2]).r);
  d=min(d,max(arr[1].r,cover(arr[0],arr[2]).r));
  d=min(d,max(arr[2].r,cover(arr[0],arr[1]).r));
  return d;
}

int main()
{
  int ci,cn;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  { circle arr[40];
    int n,i;
    cin>>n;
    for(i=0;i<n;++i) cin>>arr[i].c.x>>arr[i].c.y>>arr[i].r;
    cout<<"Case #"<<ci<<": "<<fixed<<calc(arr,n)<<endl;
  }
}

