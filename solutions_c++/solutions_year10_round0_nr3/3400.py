#include<iostream>
#include<vector>
#define pii pair<long,int>

using namespace std;


int main(){

int t;
cin>>t;
int n;
long long r,k;
long long a[1000];


for(int i=0;i<t;i++)
{ cin>>r>>k>>n;
  for(int j=0;j<n;j++)cin>>a[j];
  vector<pii>V;
  long long patron=-1;
  int pos=-1,vueltas;
  long long SUMA=0,total=0;
  int p=0;
  int actual=-1;
  for(vueltas=1;pos==-1&&vueltas<=r;vueltas++){
 
   
    long long c=0;
    actual=p;
    while(c+a[p]<=k){
      c+=a[p];
      p=(p+1)%n;
      if(p==actual)break;
    }
    total+=c;
    long long X=c;
    int Y=p;
    for(int q=0;q<V.size();q++)
     if(V[q].first==X&&V[q].second==Y){
       pos=q;
       total-=c;
       vueltas--;
       break;                                
     }
     
                  
     if(pos==-1){
      V.push_back(pii(X,Y));            
     }  
     
  }
  vueltas--;
  /*
  cout<<"VUEL "<<vueltas<<endl;
 cout<<"--- "<<total<<endl;
  */
  if(pos==-1){
         
  cout<<"Case #"<<i+1<<": "<<total<<endl;
  }
  else{
   long long L=(long long)(V.size())-pos;
  // cout<<"L "<<L<<endl;
   long long resta=r-vueltas;
   //cout<<"resta "<<resta<<endl;
   for(int q=pos;q<V.size();q++)SUMA+=V[q].first;
   total=total+resta/L*SUMA;
   //cout<<resta/L<<" "<<SUMA<<endl;
    for(int q=pos;q<pos+resta%L;q++)total+=V[q].first;
   cout<<"Case #"<<i+1<<": "<<total<<endl;
  }
 }
}
