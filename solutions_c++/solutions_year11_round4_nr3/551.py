#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main ()
{
  int T,N;
  int min,max;
  double res;
  int i,j;
  int a[] = {2,3,5,7,11,13,17,19,23,29,31};
  cin >> T;
  for(i=0;i<T;i++){
    cin >> N;
    min =0;
    max = 0;
    for(j=0;j<11;j++){
      if(N-a[j]>=0){
	 min = min+1;
      }
      res = log(double(N))/log(double(a[j]));
      max = max + floor(res);
    }
    if(N==1){
      max=min-1;
    }
    cout << "Case #"<< i+1 << ": " << max - min +1 << endl;  
  }
  return 0;
}