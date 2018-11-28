#include <iostream>

using namespace std;

int main() {

  int t,n;

  int i,j,k;
  char data[100][100];
  double win[100],total[100];
  double wp[100],owp[100],oowp[100];
  cin >> t;
  for(i=0;i<t;i++){
    cin >> n;
    for(j=0;j<n;j++){
      total[j]=0;
      win[j]=0;
      for(k=0;k<n;k++){
	cin >> data[j][k];
	if( data[j][k] == '1' || data[j][k] == '0'){
	  total[j]++;
	  if( data[j][k] =='1' ) win[j]++;
	}
      }
      wp[j] = win[j]/total[j];
    }
    
    for(j=0;j<n;j++){
      double sum=0;
      for(k=0;k<n;k++){
	if( data[j][k] != '.' ){
	  if( data[j][k] == '0' ) {
	  sum = sum + ((win[k]-1)/(total[k]-1));
	  }else {
	    sum = sum + ((win[k])/(total[k]-1));
	  	 
	  }
	}
      }
      
      owp[j] = sum / total[j];
            
      
    }
    for(j=0;j<n;j++){
      double sum=0;
      for(k=0;k<n;k++){
	if( data[j][k]!='.'){
	  sum = sum + owp[k];
	}
      }
      oowp[j] = sum / total[j];
    }
    

    cout << "Case #" << i+1 << ":" << endl;
    for(j=0;j<n;j++){
      cout << (0.25*wp[j]) + (0.5*owp[j]) + (0.25*oowp[j]) << endl;
    }
  }
}
