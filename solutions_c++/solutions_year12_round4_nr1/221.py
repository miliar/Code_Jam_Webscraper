#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
#include<queue>



using namespace std;

int main(){
  int T; cin>>T;
  for (int tc=1;tc<=T;tc++){
    int N;
    cin>>N;
    vector<int> d, I,l;
    d=vector<int>(N,0);
    I=d;
    l=vector<int>(N,-1);
    for (int i=0;i<N;i++){
      cin>>d[i]>>I[i];
    }
    int D;
    cin>>D;
    l[0]=d[0];
    cout<<"Case #"<<tc<<": ";
    for (int i=0;i<N;i++){
      int k=i+1;
      if (l[i]==-1)
	break;
      while (k<N && d[k]-d[i]<=l[i]){
	if (l[k]!=-1){
	  k++;
	  continue;
	}
	l[k]=d[k]-d[i];
	if (I[k]<l[k]) l[k]=I[k];
	k++;
      }
    }
    for (int i=0;i<N;i++){
      if (d[i]+l[i]>=D){
	cout<<"YES"<<endl;
	break;
      }
      if (i+1==N){
	cout<<"NO"<<endl;
      }
    }
  }
  return 0;
}
