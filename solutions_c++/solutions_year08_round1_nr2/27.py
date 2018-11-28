#include <iostream>
#include <cstdlib>
#include <cassert>

using namespace std;

void fail(int caseno){
  printf("Case #%d: IMPOSSIBLE\n", caseno);
}

void solve(int caseno){
  int n,m;
  cin >> n >> m;

  int **matrix = new int*[m];
  for(int i=0; i<m; ++i){
    matrix[i] = new int[n];
    for(int j=0; j<n; ++j){
      matrix[i][j] = 0;
    }
  }

  int *flavors = new int[m]; // count of # flavors liked by each still remaining 
  for(int i=0; i<m; ++i){
    flavors[i] = 0;
  }
  
  int *malted = new int[m]; // which people like at least one malted drink?

  bool *killed = new bool[n]; // which of the flavors are forced malted? 

  for(int i=0; i<m; ++i){
    malted[i] = 0;
  }
  for(int i=0; i<n; ++i){
    killed[i] = false;
  }

  // 1 = unmalted 2 = malted
  int t;
  for(int i=0; i<m; ++i){
    cin >> t;
    flavors[i] = t;
    for(int j=0; j<t; ++j){
      int flav, pref;
      cin >> flav >> pref;
      matrix[i][flav-1] = pref+1;
      if(pref == 1)
	malted[i] = flav;
    }
  }

  bool flag = true;
  while(flag){
    flag = false;
    for(int i=0; i<m; ++i){
      if(flavors[i] == 0){
	fail(caseno);
	return;
      }
      if(flavors[i] == 1 && (malted[i] > 0) && !killed[malted[i]-1]){
	// search for desired flavor:
	int flav = malted[i]-1; 
	assert(flav >= 0);
	
	killed[flav]=true;
	flag = true;

	// kill unmalted preferences
	for(int k=0; k<m; ++k){

	  if(matrix[k][flav] == 1){
	    flavors[k]--;
	    assert(flavors[k] >= 0);
	    if(flavors[k] == 0){
	      fail(caseno);
	      return;
	    }
	    matrix[k][flav] = 0;
	  }

	}
      }
    }
  }  
  printf("Case #%d: ",caseno);
  for(int i=0; i<n; ++i){
    if(killed[i]){
      cout << 1;
    }
    else
      cout << 0;
    if(i < n-1)
      cout << " ";
  }
  cout << endl;
}

int main(){
  int n;
  cin >> n;
  for (int i=0; i<n; ++i)
    solve(i+1);
  return 0;
}
