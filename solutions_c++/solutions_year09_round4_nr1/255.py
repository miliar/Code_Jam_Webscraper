#include <iostream>
using namespace std;

int main(){
  int t;
  cin >> t;
  string a[50];
  int b[50];
  int cnas = 0;
  while (t--){
    cout << "Case #"<<++cnas<<": ";
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i){
      cin >> a[i];
      b[i] = -1;
      for (int j = 0; j < n; ++j)
	if (a[i][j]=='1')
	  b[i] = j;
    }
    int ans = 0;
    for (int i = 0; i < n; ++i)
      if (b[i]>i){
	for (int j = i+1; j < n; ++j)
	  if (b[j]<=i){
	    //	    cout << i <<" "<< j <<endl;
	    
	    int x = b[j];
	    //	    cout << x <<endl;
	    
	    for (int k = j; k > i; --k)
	      b[k] = b[k-1];
	    b[i] = x;
	    ans+=(j-i);
	    //    for (int m = 0;m < n; ++m)
	    //	      cout << b[m]<<" ";
	    //	    cout << endl;
	    
	    break;
	  }
      }
    cout << ans <<endl;
  }  
}
