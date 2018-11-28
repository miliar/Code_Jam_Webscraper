
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

// ...

int n;
long long r,k;
long long A[1000];
int t;


using namespace std;

int main(){
cin>>t;


for(int fisi=0;fisi<t;fisi++)
{ cin>>r>>k>>n;
  for(int j=0;j<n;j++)cin>>A[j];
  vector<pii>V;
  long long patron=-1;
  int pos=-1,SPEEDY;
  long long AD=0,UNMSM=0;
  int p=0;
  int actual=-1;
  for(SPEEDY=1;pos==-1&&SPEEDY<=r;SPEEDY++){
 
   
    long long c=0;
    actual=p;
    while(c+A[p]<=k){
      c+=A[p];
      p=(p+1)%n;
      if(p==actual)break;
    }
    UNMSM+=c;
    long long X=c;
    int Y=p;
    for(int q=0;q<V.size();q++)
     if(V[q].first==X&&V[q].second==Y){
       pos=q;
       UNMSM-=c;
       SPEEDY--;
       break;                                
     }
     
                  
     if(pos==-1){
      V.push_back(pii(X,Y));            
     }  
     
  }
  SPEEDY--;
  
  if(pos==-1){
         
  cout<<"Case #"<<fisi+1<<": "<<UNMSM<<endl;
  }
  else{
   long long L=(long long)(V.size())-pos;
   long long resta=r-SPEEDY;
   for(int q=pos;q<V.size();q++)AD+=V[q].first;
   UNMSM=UNMSM+resta/L*AD;
    for(int q=pos;q<pos+resta%L;q++)UNMSM+=V[q].first;
   cout<<"Case #"<<fisi+1<<": "<<UNMSM<<endl;
  }
 }
}
