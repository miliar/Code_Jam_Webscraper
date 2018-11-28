#include<iostream>
#define max(a,b) (a>b)?a:b
using namespace std;
 
int les[100];
int main(){
  int casos,n;
  cin>>casos;
  for(int t=1;t<=casos;t++){
    cin>>n;
    for(int i=0;i<n;i++){
     cin>>les[i];
    }
    long long baby=-1;
    for(int i=0; i<(1<<n); i++){
       long long ad1=0,ad2=0;
       long long c1=0,c2=0;
       int x=0,y=0;
       for(int j=0; j<n; j++){
          if(i&(1<<j))ad1=ad1^les[j],c1+=les[j],x++;
          else ad2=ad2^les[j], c2+=les[j],y++;
       }
       if(ad1==ad2&&x>0&&y>0){
          if(c1>baby)baby=c1;
          if(c2>baby)baby=c2;
          
       }
     }
    if(baby==-1)cout<<"Case #"<<t<<": NO"<<endl;
    else cout<<"Case #"<<t<<": "<<baby<<endl;
  }
}