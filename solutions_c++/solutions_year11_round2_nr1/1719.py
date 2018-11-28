#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <iomanip>
#define PI 3.14159265358979323846264338327950288
#define MOD 100003
using namespace std;

void cal() {
  int N;
  cin>>N;
  
  vector< vector<char> > res(N, vector<char>(N));
  for(int i = 0 ; i < N; i++) 
    for(int j = 0; j < N; j++)
      cin>>res[i][j];

  vector<int> OP(N);
  vector<double> WP(N), OWP(N), OOWP(N);
  vector<int> W(N), OW(N), OOW(N);
  for(int i = 0; i < N; i++) {
    OP[i] = 0; W[i] = 0; OW[i] = 0; OOW[i] = 0;
    OP[i] = 0; WP[i] = 0; OWP[i] = 0; OOWP[i] = 0;
  }

  for(int i = 0; i < N; i++) {
    for(int j = 0; j < N; j++) {
      if ( res[i][j] != '.' ) OP[i]++;
      if ( res[i][j] == '1' ) {
	WP[i]++;
	W[i]++;
      }
    }
    WP[i] /= OP[i];
    //    cout<<"i: "<<i<<" W: "<<W[i]<<" WP: "<<WP[i]<<endl;
    //    cout<<W[i]<<" "<<OP[i]<<endl;
  }
  cout<<endl;

  for(int i = 0; i < N; i++) {
    for(int j = 0; j < N; j++) {
      if ( res[i][j] != '.' ) {
	
	double temp = (double) ( W[j] - ((res[j][i] == '1') ? 1 : 0) ) / (OP[j]-1);
	OWP[i] += temp;
	//	cout<<"i: "<<i<<" j: "<<j<<" temp: "<<temp<<" OWP: "<<OWP[i]<<endl;
      }
    }
    OWP[i] /= OP[i];
    //    cout<<OWP[i]<<endl;
  }
  //  cout<<endl;

  for(int i = 0; i < N; i++) {
    for(int j = 0; j < N; j++) 
      if ( res[i][j] != '.') OOWP[i] += OWP[j];
    OOWP[i] /= OP[i];
    //    cout<<OOWP[i]<<endl;
  }
  
  vector<double> RPI(N);
  for(int i = 0; i < N; i++) {
    RPI[i] = WP[i] / 4 + OWP[i] / 2 + OOWP[i] / 4;
    cout<<fixed;
    cout.precision(12);
    cout<<RPI[i]<<endl;
  }
}

int main() {
  
  int T;
  cin>>T;
  for(int i = 1; i <= T; i++) {
    cout<<" Case #"<<i<<": ";
    cal();
    //    cout<<endl;
  }

  return 0;
}
