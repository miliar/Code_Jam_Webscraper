
//CODER: Adolfo Ccanto Ad...
#include<iostream>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<algorithm>
#include<sstream>
#include<stack>
#include<math.h>
#include<string>

#define F(i,a,b) for(int i=a;i<b;i++)
#define all(x) x.begin(),x.end()
#define pb push_back
#define pii pair<int,int>

#define FE(it,sto) for(typeof(sto.begin())it=sto.begin();it!=sto.end();++it)


using namespace std;
long long gcd(long long a,long long b){
  if(!b)return a;
  return gcd(b,a%b);     
}



char ollanta[100][100];
int n;

pii wp[100];
long double owp[100];
long double oowp[100];

pii WP(int ind){
  int uno=0,t=0;   
  F(i,0,n)     
  { if(ollanta[ind][i]=='1')uno++;
    if(ollanta[ind][i]!='.')t++;
  }
  
  if(t==0)return pii(0,0);
  
  return pii(uno,t);
}

long double OWP(int ind){
  long double r=0;
  long double pt=0;   
  F(i,0,n)     
   if(ollanta[ind][i]!='.'){ 
     pii t=wp[i];
     int tot=t.second;
     int win=t.first;
    if(ollanta[i][ind]=='1')win--;
    if(tot!=0)tot--;
    if(tot!=0)
     r+=win/(long double)tot;
    
     pt++;
   }
   if(pt==0)return 0;
   return r/pt;
}


long double OOWP(int ind){
  long double r=0;
  long double pt=0;   
  F(i,0,n)     
   if(ollanta[ind][i]!='.'){ 
     r+=owp[i];
     pt++;
   }
   if(pt==0)return 0;
   return r/pt;
}



int main(){
    freopen("A-large.in","r",stdin);
    freopen("data.ou","w",stdout);
    
    int casos;
    cin>>casos;
    F(t,1,casos+1){
      cout<<"Case #"<<t<<":"<<endl;     
       cin>>n;
       F(i,0,n)F(j,0,n)cin>>ollanta[i][j];
      F(i,0,n)
       wp[i]=WP(i);
      
       
      F(i,0,n)
       owp[i]=OWP(i);
       
      F(i,0,n)
       oowp[i]=OOWP(i);
       
      F(i,0,n){
        long double r=0.5*owp[i]+0.25*oowp[i];       
        if(wp[i].second!=0)       
        r+=0.25*wp[i].first/(long double)wp[i].second;
        cout<<r<<endl;
      }
    }

}
