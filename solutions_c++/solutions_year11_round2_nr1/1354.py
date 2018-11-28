#include <iostream>

using namespace std;

main(){
  int t;
  cin >> t;
  for(int tc=0;tc<t;tc++){
    int n;
    cin >> n;
    char data[100][100];
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
	cin >> data[i][j];
      }
    }
    double wp[100];
    for(int i=0;i<n;i++){
      int nw=0, np=0;
      for(int j=0;j<n;j++){
	if(data[i][j]!='.') np++;
	if(data[i][j]=='1') nw++;
      }
      wp[i]=(double)nw/(double)np;
    }
    double owp[100];
    double twp[100];
    for(int i=0;i<n;i++){
      int np=0;
      for(int j=0;j<n;j++){
	if(i==j) continue;
	np=0;
	int nw=0;
	for(int k=0;k<n;k++){
	  if(i==k) continue;
	  if(data[j][k]!='.') np++;
	  if(data[j][k]=='1') nw++;
	}
	twp[j]=(double)nw/(double)np;
      }
      double sum=0.0;
      np=0;
      for(int j=0;j<n;j++){
	if(data[i][j]!='.'){
	  np++;
	  sum+=twp[j];
	}
      }
      owp[i]=sum/(double)np;
    }
    double oowp[100];
    for(int i=0;i<n;i++){
      int np=0;
      double sum=0.0;
      for(int j=0;j<n;j++){
	if(data[i][j]!='.'){
	  np++;
	  sum+=owp[j];
	}
      }
      oowp[i]=sum/(double)np;
    }
    cout << "Case #" << tc+1 << ":" << endl;
    for(int i=0;i<n;i++){
      printf("%.12f\n", 0.25*wp[i]+0.50*owp[i]+0.25*oowp[i]);
    }
  }
  return 0;
}
