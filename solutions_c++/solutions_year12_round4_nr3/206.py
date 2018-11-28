#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
#include<queue>



using namespace std;

int main(){
  int T; cin>>T;
  for (int tc=1;tc<=T;tc++){
    int N; cin>>N;
    vector<int> x=vector<int>(N-1,0);
    for (int i=0;i<N-1;i++){
      cin>>x[i];
      x[i]=x[i]-1;
    }
    vector<int> y=vector<int> (N,-1);
    vector<bool> b=vector<bool>(N,false);
    int c=1;
    bool ja=true;
    int h=0;
    vector<int> sok=vector<int>(N-1,-1);
    vector<int> sokn=sok;
    while (h<N-1){
      y[h]=1000000000;
      c++;
      for (int i=h+1;i<x[h];i++){
	sok[i]=x[h];
	sokn[i]=1;
      }
      b[h]=true;
      h=x[h];
    }
    y[N-1]=1000000000;
    for (int i=0;i<N && c<N;i++){
      if (sokn[i]==1){
	h=i;
	break;
      }
    }

    while(ja && c<N){
      int i=h;
      if (i==N){
	i=0;
	while (b[i]) i++;
      }
      h=N;
      while (ja && i<N-1 && !b[i]){
	for (int j=i+1;j<x[i];j++){
	  if (b[j]){
	    ja=false;
	    break;
	  }
	  sok[j]=x[i];
	  sokn[j]++;
	  if (j<h) h=j;
	}
	b[i]=true;
	c++;
	y[i]=y[sok[i]]-sokn[i]*(sok[i]-i);
	i=x[i];
		
      }
    }
    cout<<"Case #"<<tc<<": ";
    if (ja){
      for (int i=0;i<N-1;i++){
	cout<<y[i]<<" ";
      }
      cout<<y[N-1]<<endl;
    }
    else{
      cout<<"Impossible"<<endl;
    }

  }
  return 0;
}
