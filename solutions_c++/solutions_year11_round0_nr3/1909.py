// This is a DP problem.

// Similar to set splitting...
// With two parts:

// Find the XOR sum of all the values:
// Divide this value by 2.  (If the XOR solution is odd, the answer
// is impossible.

// Use DP to find whether there exists a subset of the values that XOR
// sums to this value.

// If the answer is no --- return impossible.
// If the answer is YES,
//
// Use DP to find the maximum real value of any subset that XOR sums
// to that value.
/*
Define

C[i][j] = True if there exists a subset of 1..i that XOR sums to j.

        = C[i-1][j] or C[i-1][j XOR S[i] ]

  D[i][j] = max{C[i-1][j],C[i-1][j XOR S[i]] + S[i];

		C[i][j] = false if j!=0;
		D[0][j] = 0;

*/

#include <iostream>
#include <set>

#include <vector>
#include <cmath>

using namespace std;


int main() {

  int T;
  int maxvs[25];
  for (int i=0;i<25;i++) {
    maxvs[i]=(1<<i)-1;
  }
  cin >> T;

  for (int x1=0;x1<T;x1++) {
    int N;
    cin >> N;
    vector<int> vals;
    int xorsum=0;
    int l=0;
    for (int x2=0;x2<N;x2++) {
      
      int P;
      cin >> P;
      while (P>maxvs[l]) l++;
      vals.push_back(P);
      xorsum^=P;
    }
   if ((xorsum!=0)) {
      cout << "Case #" << x1+1 <<": NO" << endl;
    } else {

      vector<bool> C1;
      vector<int> D1;
      vector<bool> C2;
      vector<int> D2;
      int maxv = maxvs[l];
      //cout << maxv << endl; 
      C1.resize(maxv+1,false);
      D1.resize(maxv+1,0);
      C2.resize(maxv+1,false);
      D2.resize(maxv+1,0);
      C2[0]=true;
      D2[0]=0;
      //cout << xorsum << endl;

      for (int i=1;i<=N;i++) {
	C1=C2;
	D1=D2;
	for (int j=0;j<=maxv;j++) {
	  C2[j]=C1[j] || C1[j^vals[i-1]];
	  if ((C1[j]) && (C1[j^vals[i-1]]) ) {
	    D2[j]=max(D1[j],D1[j^vals[i-1]] + vals[i-1]);
	  } else {
	    if (C1[j]) {
	      D2[j]=D1[j];
	    } else {
	      if (C1[j^vals[i-1]]) {
		D2[j] = D1[j^vals[i-1]]+vals[i-1];
	      } else {
		D2[j]=0;
	      }
	    }
	  }
	}
	//cout << D2[3] << endl;
      }
      int maxo = 0;
      for (int j=1;j<=maxv;j++) {
	if (C2[j]) {
	  if (D2[j]>maxo) {
	    maxo=D2[j];
	  }
	}
      }
      cout << "Case #" << x1+1 <<": "<<maxo << endl;
      
      }
      }
      
}

    


