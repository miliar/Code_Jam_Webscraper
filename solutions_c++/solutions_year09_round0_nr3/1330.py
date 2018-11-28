#include <string>

#include <iostream>
#include <iomanip>
using namespace std;

string wel = "welcome to code jam";

int C[501][50];


int main() {

  int N;
  cin >> N;

  string temp;
  string X;
  string Z;
  Z = wel;
  getline(cin,temp);

  for (int i1=0;i1<N;i1++) {
    //
    
    getline(cin,X);
    

    for (int i=0;i<=X.length();i++) {
      for (int j=0;j<=Z.length();j++) {
	if (i<j) 
	  C[i][j] = 0;
	else if ((i==0)||(j==0)) 
	  C[i][j] = 0;
	else if (j==1) {
	  int k=0;
	  for (int l=0;l<i;l++) {
	    if (Z[0]==X[l]) k++;
	  }
	  C[i][j] = k % 10000;
	} else {
	  if (X[i-1]==Z[j-1]) {
	    C[i][j] = (C[i-1][j]+C[i-1][j-1])%10000;
	  } else {
	    C[i][j] = C[i-1][j];
	  }
	}
      }
    }
    cout << "Case #"<<i1+1<<": " << setfill('0') << setw(4) << C[X.length()][Z.length()] << endl;
  }
}
	
