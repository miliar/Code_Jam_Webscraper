#include<iostream>
#include<vector>
#include<string>
#include<stack>

using namespace std;

int main(){
  int T,t=1;
  cin>>T;
  int C,D,N;
  string ctmp;
  while(T--){
    string c="",d="",n="";
    cin>>C;
    if (C>0){
      for (int k=0;k<C;k++){
	cin>>ctmp;
	c+=ctmp;
      }
    }
    cin>>D;
    if (D>0)
      for (int k=0;k<D;k++){
	cin>>ctmp;
	d+=ctmp;
      }
    cin>>N>>n;
    vector<char> V;
    for (int i=0;i<N;i++){
      V.push_back(n[i]);
      int k=V.size()-1;
      if (k>0){
	for (int j=0;j<C;j++){
	  if ((V[k]==c[3*j] && V[k-1]==c[3*j+1]) ||
	      (V[k]==c[3*j+1] && V[k-1]==c[3*j])){
	    V[k-1]=c[3*j+2];
	    V.pop_back();
	    if (V.size()==1) break;
	    j=-1;
	  }
	}
      }
      k=V.size()-1;
      if (k>0){
	for (int j=0;j<D;j++){
	  if (V[k]==d[2*j]){
	    for (int a=0;a<k;a++){
	      if (V[a]==d[2*j+1]){
		V.resize(0);
		goto end;
	      }
	    }
	  }
	  if (V[k]==d[2*j+1]){
	    for (int a=0;a<k;a++){
	      if (V[a]==d[2*j]){
		V.resize(0);
		goto end;
	      }
	    }
	  }
	}
      }
    end:
      int askdfj;
    }
    cout<<"Case #"<<t++<<": [";
    for (int i=0;i<V.size();i++){
      cout<<V[i];
      if (i<V.size()-1)
	cout<<", ";
    }
    cout<<"]"<<endl;
  }
}
      

      
