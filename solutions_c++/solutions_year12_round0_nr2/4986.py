#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
  int T;
  cin>>T;
  for (int t=1;t<=T;t++){
    int N,S,p;
    int tot=0;
    cin>>N>>S>>p;
    int t1=max(3*p-2,p);
    int t2=max(3*p-4,p);
    for (int j=0;j<N;j++){
      int k;
      cin>>k;
      if (k>=t1) tot++;
      else if (k>=t2)
	if (S){
	  S--;
	  tot++;
	}
    }
    cout<<"Case #"<<t<<": "<<tot<<endl;
  }
}
