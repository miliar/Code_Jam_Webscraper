#include <cstdio>
#include <vector>
#include <cmath>

using namespace std;

int main(){
int t;
scanf("%d",&t);
for(int tt=1;tt<=t;tt++){
int n,a;
long double d,ttt,aaa,aaaa;
scanf("%Lf %d %d",&d,&n,&a);
vector<long double> x;
vector<long double> t;
bool end = true;
for(int i=0;i<n;i++){scanf("%Lf %Lf",&aaa,&aaaa);if(end){t.push_back(aaa);x.push_back(aaaa);end=aaaa<d; }}
if(x[x.size()-1]>d && x.size()>1){


long double t1=t[t.size()-2];
long double x1=x[x.size()-2];
long double t2=t[t.size()-1];
long double x2=x[x.size()-1];
long double aa=(x1-x2)/(t1-t2);
long double bb=x1-aa*t1;
ttt=(d-bb)/aa;//arrival of other car


t[t.size()-1]=ttt;
x[x.size()-1]=d;
}else if(x.size()<2){x[0]=d;t[0]=0;}

printf("Case #%d:\n",tt);
for(int i=0;i<a;i++){
long double aa;
scanf("%Lf",&aa);
long double tt2=sqrtl(2*d/aa);//time to go
//
long double t0=0;
long double tttt;
for(int j=0;j<x.size();j++){
tttt=t[j]-sqrtl(2*x[j]/aa);
if(tttt>t0)t0=tttt;
}


//
printf("%.6Lf\n",t0+tt2);



}



}
return 0;
}
