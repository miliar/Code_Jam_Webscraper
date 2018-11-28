#include <iostream>
using namespace std;
inline int dist(int a,int b){return a>b?a-b:b-a;}
int main()
{
int t,n;
int w[2];
int c[2];
ios_base::sync_with_stdio(0);
cin >> t;
for(int cs=1;cs<=t;cs++)
{
cin>>n;
w[0]=w[1]=1;
c[0]=c[1]=0;
int k,d,rr=0;
char cc;
while(n--)
{
cin>>cc>>d;
k = cc=='O'? 0:1;
c[k] -= dist(w[k],d);
if(c[k]<1) {
c[1-k] -= c[k]; rr-=c[k]; c[k] = 1;}
c[k]=0;
c[1-k]++;
rr++;
w[k] = d;
}
cout << "Case #"<<cs<<": "<<rr<<endl;
}
return 0;
}
