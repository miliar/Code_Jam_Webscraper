#include <iostream>
#include <string>
using namespace std;
int main(){
  int t;
  cin >> t;
  for (int kk = 1;kk<=t;++kk){
    cout<< "Case #"<<kk<<":\n";
    int r,c;
    cin >> r >> c;
    char a[55][55];
    string s;
    getline (cin,s);
    for (int i = 0; i< r; ++i){
      getline (cin,s);
      for (int j = 0; j<c;++j){
	a[i][j] = s[j];
      }
    }
    for (int i = 0; i < r-1; ++i){
      for (int j = 0; j <c-1; ++j){
	if (a[i][j]=='#' && a[i][j+1]=='#' && a[i+1][j]=='#' && a[i+1][j+1]=='#')
	  {
	    a[i][j] = a[i+1][j+1]='/';
	    a[i+1][j] = a[i][j+1] = '\\';
	  }
      }      
    } 
      
    for (int i = 0; i < r; ++i)
      for (int j = 0; j < c;++j)
	if (a[i][j]=='#'){
	  cout << "Impossible\n";
	  goto hi;
	}
    for (int i = 0; i < r; ++i){
      for (int j = 0; j < c; ++j)
	cout << a[i][j];
      cout <<endl;
      
    }
  hi:;
  }
}
