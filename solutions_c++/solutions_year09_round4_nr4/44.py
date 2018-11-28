#include<cstdio>
#include<bitset>
#include<iostream>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
using namespace std;
int n,x[110],y[110],r[110];
typedef pair<long double,long double> p2;
vector<p2> intersection(int x0,int y0,long double r0,int x1,int y1,long double r1){
  bool s=0;
  if(x1==x0){
    s=1;
    swap(x0,y0);
    swap(x1,y1);
  }
  long double A=2*(x1-x0),B=2*(y1-y0),C=r0*r0-r1*r1-x0*x0-y0*y0+x1*x1+y1*y1;
#define EPS 1e-6
  assert(fabs(A)>EPS);
  B/=-A;
  C/=A;
  // x=By+C
  // (By+C-x0)^2+(y-y0)^2=r0^2
  // B^2 y^2 + 2(c-x0)By + (c-x0)^2 + y^2 - 2y y0 + y0^2 = r0^2
  long double a=1+B*B,b=2*(C-x0)*B-2*y0,c=(C-x0)*(C-x0)+y0*y0-r0*r0;
  long double delta=b*b-4*a*c;
  vector<p2> t;
  if(delta<0)return t;
  assert(delta+EPS > 0);
  delta=sqrt(max((long double)0.0,delta));
  long double y=(-b-delta)/2/a;
  t.push_back(p2(B*y+C,y));
  y=(-b+delta)/2/a;
  t.push_back(p2(B*y+C,y));
  for(int i=0;i<t.size();i++){
    assert((x0-t[i].first)*(x0-t[i].first)+(y0-t[i].second)*(y0-t[i].second)<r0*r0+EPS);
    assert((x1-t[i].first)*(x1-t[i].first)+(y1-t[i].second)*(y1-t[i].second)<r1*r1+EPS);
  }
  if(s)for(int i=0;i<t.size();i++)swap(t[i].first,t[i].second);
  return t;
}
vector<bitset<50> > q;
void ok(long double sx,long double sy,long double R){
  q.push_back(bitset<50>());
  for(int i=0;i<n;i++)if((x[i]-sx)*(x[i]-sx)+(y[i]-sy)*(y[i]-sy)<(R-r[i])*(R-r[i])+EPS)q.back()[i]=1;
  assert(q.back().count());
}
bool ok(long double R){
  q.clear();
  for(int i=0;i<n;i++)ok(x[i]+R-r[i],y[i],R);
  for(int i=0;i<n;i++)for(int j=0;j<i;j++){
    vector<p2> t=intersection(x[i],y[i],R-r[i],x[j],y[j],R-r[j]);
    for(int k=0;k<t.size();k++)ok(t[k].first,t[k].second,R); 
  }
//  cout<<q.size()<<endl;
//  for(int i=0;i<q.size();i++)cout<<q[i].to_string<char,char_traits<char>,allocator<char> >()<<endl;
  for(int i=0;i<q.size();i++)for(int j=0;j<=i;j++)if((q[i]|q[j]).count()==n)return true;
  return false;
}
main(){
//  vector<p2> z=intersection(0,0,10,0,14,5);
//  for(int i=0;i<z.size();i++)cout<<z[i].first<<","<<z[i].second<<endl;
//  return 0;
  int t;scanf("%d",&t);for(int tt=1;tt<=t;tt++){
    scanf("%d",&n);
    for(int i=0;i<n;i++)scanf("%d %d %d",&x[i],&y[i],&r[i]);
//    ok(5);
//    return 0;  
    long double from=0,to=10000;
    for(int i=0;i<n;i++)from>?=r[i];
    for(int z=0;z<40;z++){
      long double middle=(from+to)/2;
      if(ok(middle))to=middle;else from=middle;
    }
    printf("Case #%d: %.7lf\n",tt,(double)from);
  }
}

//lubiegeometrielubiegeometrielubiegeometrielubiegeometrie
