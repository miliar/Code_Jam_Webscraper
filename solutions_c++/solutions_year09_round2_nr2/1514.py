#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::string;
using std::sort;

int main() {

  int T;

  cin >> T;
  cin.ignore();

  string N;

  for (int i=0; i < T; ++i) {
    cin >> N;
    cin.ignore();

    int len=N.length();

    int D_i[10]; // holds 0-9; won't use 0
    int D_i2[10]; // holds 0-9; won't use 0
    for (int j=0; j<10; ++j){
      D_i[j]=0;
      D_i2[j]=0;
    }

    // count D_i for each i
    // (counting 0's doesn't hurt)
    for (int j=0; j<len; ++j) {
      D_i[N[j] - '0']++;
    }

    int last = N[len-1];
    bool fixable = false;  // we cannot fix it by swapping digits
    for (int j=len - 2; j>=0; --j) {
      if ( N[j] < last ) {
	fixable = true;	// can fix it by reordering among the digits [j, len-1]

	// count number of digits in [j, len-1]
	for (int k=j; k<len; ++k) {
	  D_i2[N[k] - '0']++;
	}
	// find the next largest single digit to replace N[j]
	for (int l=N[j]-'0'+1; l <= 9; ++l) {
	  if (D_i2[l] > 0) {
	    N[j] = l + '0';
	    --D_i2[l];
	    break;
	  }
	}
	int j2 = j+1;
	for (int l=0; l < 9; ++l) {
	  while (D_i2[l]-- > 0) {
	    N[j2++] = l + '0';
	  }
	}
	break;
      }
      last = N[j];
    }
    
    string N2 = N + "0";
    if ( fixable == false ) { 
      // we need to add a 0 and increase the number of digits
      D_i[0]++;
      // find the smallest digit, to put at the beginning
      for (int l=1; l <= 9; ++l) {
	if (D_i[l] > 0) {
	  N2[0] = l + '0';
	  --D_i[l];
	  break;
	}
      }
      int j = 1;
      for (int l=0; l < 9; ++l) {
	while (D_i[l]-- > 0) {
	  N2[j++] = l + '0';
	}
      }
    }

    if (fixable == true)
      cout << "Case #" << i+1 << ": " << N << endl;
    else
      cout << "Case #" << i+1 << ": " << N2 << endl;
  }

  return 0;
}
