#include<iostream>
using namespace std;

int main(){
  int T,t=1;
  cin>>T;
  while(T--){
    int N,tmp,min=10000000,total=0,xorsum=0;
    cin>>N;
    for (int i=0;i<N;i++){
      cin>>tmp;
      if (min>tmp) min=tmp;
      total+=tmp;
      xorsum^=tmp;
    }
    if(xorsum==0)
      cout<<"Case #"<<t++<<": "<<total-min<<endl;
    else
      cout<<"Case #"<<t++<<": NO"<<endl;
  }
}
      

      
