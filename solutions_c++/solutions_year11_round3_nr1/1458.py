#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
  int T;
  int R,C,i,j,k;
  int ans;
  vector<vector <char> > a;
  char c;
  string s;
  int NO;
  cin >> T;
  for(i=0;i<T;i++){
    cin >> R;
    cin >> C;
    a.resize(R);
    for(j=0;j<R;j++){ 
      for(k=0;k<C;k++){
	cin >> c;
	a[j].push_back(c);
      }
    }   
    NO =0;
    for(j=0;j<R;j++){
      for(k=0;k<C;k++){
	if(a[j][k]=='#'){
	  if(j==R-1 || k == C-1){
	    NO=1;
	  }
	  else{
	    if(a[j][k+1]== '#' && a[j+1][k+1]== '#' && a[j+1][k]== '#'){
	      a[j][k] = '/';
	      a[j][k+1] = '\\';
	      a[j+1][k] = '\\';
	      a[j+1][k+1] = '/';
	    }
	    else{
	      NO=1;
	    }
	  }
	}
      }
    }
    if(NO==1){
      cout << "Case #" << i+1 << ":" << endl;
      cout << "Impossible" << endl;
    }
    else{
      cout << "Case #" << i+1 << ":" << endl;
      for(j=0;j<R;j++){
	for(k=0;k<C;k++){
	  cout << a[j][k];
	}
	cout << endl;
      }  
    }
    for(j=0;j<R;j++){
      a[j].clear();
    }
    a.clear();
  }
  return 0;
}