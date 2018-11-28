#include<iostream>
#include<vector>

using namespace std;

int main(){

  int T;
  cin>>T;
  for (int t=1;t<=T;t++){
    int P;
    cin>>P;
    int N=1<<P;
    vector<vector<long long> > teams(N);
    for (int i=0;i<N;i++){
      teams[i].resize(12);
      for (int j=0;j<12;j++){
	teams[i][j]=2000000000;
      }
    }
    for (int i=0;i<N;i++){
      int a;
      cin>>a;
      for (int j=0;j<=a;j++){
	teams[i][j]=0;
      }
    }
    vector<vector<long long> > costs(P);
    for (int i=0;i<P;i++){
      costs[i].resize(N/(2<<i));
      for (int j=0;j<(N/(2<<i));j++){
	cin>>costs[i][j];
	//	cout<<i<<' '<<j<<' '<<costs[i][j]<<endl;
      }
    }
    int step=1;
    for (int loop=0;loop<P;loop++){
      for (int i=0;i*step<N;i+=2){
	for (int j=0;j<12;j++){
	  //	  cout<<i*step<<' '<<j<<' '<<teams[i*step][j]<<' '<<teams[(i+1)*step][j]<<endl;
	  teams[i*step][j] = min((long long)2000000000,min(teams[i*step][j+1]+teams[(i+1)*step][j+1],
						costs[loop][i/2]+teams[i*step][j]+teams[(i+1)*step][j]));
	  //	  cout<<i*step<<' '<<j<<' '<<teams[i*step][j]<<endl;//' '<<costs[loop][i]<<endl;
	}
      }
      step*=2;
    }
    long long best=2000000000;
    for (int i=0;i<10;i++){
      if (teams[0][i]>=0)
	best = min(best,teams[0][i]);
    }
    cout<<"Case #"<<t<<": "<<best<<endl;
  }
}
	
