#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<cmath>
#include<queue>
#include<stack>

using namespace std;

int main(){
  int tn;
  cin >> tn;

  for(int tc = 1; tc<=tn; tc++){
    int h,w;
    cin >> h >> w;
    
    vector<string> tab;
    for(int i=0; i<h; i++){
      string tmp; cin >> tmp;
      tab.push_back(tmp);
    }

    for(int i=0; i<h-1; i++){
      for(int j=0; j<w-1; j++){
	if(tab[i][j] == '#' &&
	   tab[i][j+1] == '#' &&
	   tab[i+1][j] == '#' &&
	   tab[i+1][j+1] == '#' ){
	  tab[i][j] = tab[i+1][j+1] = '/';
	  tab[i][j+1] = tab[i+1][j] = '\\';
	}
      }
    }
    bool flg = true;
    for(int i=0; i<h; i++){
      for(int j=0; j<w; j++){
	if(tab[i][j] == '#')flg = false;
      }
    }
    cout << "Case #" << tc << ":" << endl;
    if(flg){
      for(int i=0; i<h; i++){
	cout << tab[i] << endl;;
      }
    }
    else {
      cout << "Impossible" << endl;
    }
  }
  return 0;
}
