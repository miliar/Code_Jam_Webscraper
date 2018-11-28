// Coder: Ad
#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<math.h>
#include<sstream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<list>
#include<deque>
#include<queue>
#include<numeric>
#define F(i,a,b) for(int i=a;i<b;++i)

#define pb push_back
#define all(x) x.begin(),x.end()
using namespace std;
string s;
long long d[20][501];
string patron;
int np,ns;

long long f(int x,int y){
 if(x==np)return 1;
 if(y==ns)return 0;

 long long &r=d[x][y];
 if(r!=-1)return r;
 r=0;
 if(s[y]==patron[x])
 { r+=f(x+1,y+1);
   r+=f(x,y+1);
 }
 else{
  r+=f(x,y+1);
 }
 return r;
}

int main(){
 int n;
 patron="welcome to code jam";
 np=patron.size();
 cin>>n;
 scanf("\n");
 F(i,1,n+1){
  getline(cin,s);
   ns=s.size();
  memset(d,-1,sizeof d);
  long long ad=f(0,0);
   stringstream in; in<<ad;
  string lesli;
  in>>lesli;
  int L=lesli.size();
  F(j,0,4-L)lesli="0"+lesli;
  cout<<"Case #"<<i<<": "<<lesli<<endl;
 }
}
