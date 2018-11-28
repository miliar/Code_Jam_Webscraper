// Run file as cat ./input.in | ./a.out  > out.txt
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
  int T;
  int N,i,j;
  int d,g;
  int ans;
  long long int a;
  int temp;
  cin >> T;
  for(i=0;i<T;i++){
    ans =0;
    cin >> a;
    if(a > 100){
      N=200;
    }
    if(a < 300){
      N= a;
    }
    cin >> d;
    cin >> g;
    if(g ==100 && d == 100){
      ans = 1;
    }
    if(g < 100){
      for(j=1;j<N+1;j++){
	temp =  d*j;
	if(temp % 100 == 0){
	  ans = 1;	  
	}
      }
    }    
    if(g ==100 && d == 0){
      ans = 0;
    }    
    if(g == 0 && d > 0){
      ans = 0;
    }
    if(ans ==1)
      cout << "Case #" << i+1 << ": Possible" << endl;    
    if(ans ==0)
      cout << "Case #" << i+1 << ": Broken" << endl;    
  }
  return 0;
}