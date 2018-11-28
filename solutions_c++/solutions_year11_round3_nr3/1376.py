#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
  int T;
  int N,L,H,i,j,k;
  int temp;
  vector<int> a;
  int m;
  cin >> T;
  for(i=0;i<T;i++){
    cin >> N;
    cin >> L;
    cin >> H;
    for(j=0;j<N;j++){
      cin >> temp;
      a.push_back(temp);
    }
    for(j=L;j<H+2;j++){
      m=0;
      for(k=0;k<N;k++){
	if((j%a[k] ==0) || (a[k]%j ==0)){
	 m=m+1;
	}
      }
      if(m==N){
	break;
      }
    }
    if(j<H+1){
      cout << "Case #" << i+1 << ": " << j << endl;
    }
    else{
      cout << "Case #" << i+1 << ": NO" << endl;
    }
    a.clear();
  }
  return 0;
}