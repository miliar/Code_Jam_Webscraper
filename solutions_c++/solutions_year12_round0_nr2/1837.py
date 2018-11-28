#include<iostream>
#include<vector>

using namespace std;

int f1(int q){
  if (q==0) return 0;
  else return (q-1)/3+1;
}

int f2(int q){
  if (q<2) return q;
  else return (q-2)/3+2;
}

int main(){
  int T,N,S,p;
  cin>>T;
  for (int t=0;t<T;t++){
    cin>>N>>S>>p;
    int svar=0;
    for (int i=0;i<N;i++){
      int q; cin>>q;
      if (f1(q)>=p) svar++;
      else{
	if (S>0){
	  if (f2(q)>=p){
	    svar++;
	    S--;
	  }
	}
      }
      
    }
    cout<<"Case #"<<t+1<<": "<<svar<<endl;
  }
  return 0;
}
