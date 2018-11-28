#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int data[1001];
int maxSum;

// sumSeanPat - sum of sean's candies in patrick's calculation
void calculate( int sumPat, int sumSeanPat, int sumSean, int index, int n) {
  if( index == n ) {
    if( sumPat != 0 && sumPat == sumSeanPat ) {
      if( sumSean > maxSum ) maxSum = sumSean;
    }
    return;
  }
  calculate( sumPat, sumSeanPat ^ data[index], sumSean + data[index], index+1, n);  
  calculate( sumPat ^ data[index], sumSeanPat, sumSean, index+1, n);

}
int main( int argc, char *argv[] ) {

  ifstream in(argv[1]);
  
  int t;
  int i,j;

  in >> t;
  for( i = 0; i < t; i++ ) {
    int n;
    in >> n;
    maxSum = -99999;
    for( j = 0; j < n; j++ ) {
      in >> data[j];
    }
    
    // BRUTE FORCE!
    calculate( 0, 0, 0, 0, n );
    cout << "Case #" << i+1 << ": ";
    if( maxSum == -99999 ) cout << "NO" << endl;
    else cout << maxSum << endl;
  }


}
