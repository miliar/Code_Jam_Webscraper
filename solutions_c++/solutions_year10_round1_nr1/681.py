#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>

using namespace std;



int main(){
  int t,n,k;
  cin >> t;
  for(int id = 1; id <=t; id++){
    cout << "Case #" << id << ": ";
    cin >> n >> k;
    vector<string> tab;
    tab.clear(); tab.reserve(n);
    for(int i=0; i<n; i++){
      string str;
      cin >> str; 
      tab.push_back(str);
    }
    vector< vector<int> > rt(n,vector<int>(n,0));
    for(int i=0; i<n; i++){
      for(int j=0; j<n; j++){
	int ins = 0;
	if(tab[i][j] == 'R')ins = 1;
	else if(tab[i][j] == 'B')ins = 2;

	rt[j][n-1-i] = ins;
      }
    }

    for(int x=0; x<n; x++){
      int swp = n-1;
      for(int y=n-1; y>=0; y--){
	if(rt[y][x] != 0){
	  swap(rt[swp][x],rt[y][x]);
	  swp--;
	}
      }
    }
    /*
    for(int i=0; i<n; i++){
      for(int j=0; j<n; j++){
	if(rt[i][j] == 1)cout << "R";
	else if(rt[i][j] == 2)cout << "B";
	else cout << ".";
      }
      cout << endl;
    }
    */
    bool flgR = false;
    bool flgB = false;
    int countR;
    int countB;
    for(int y=0; y<n; y++){

      countR = 0;
      countB = 0;
      for(int x=0; x<n; x++){
	if(rt[y][x] == 1){
	  countR++;
	  countB = 0;
	}
	else if(rt[y][x] == 2){
	  countB++;
	  countR = 0;
	}
	else {
	  countR = 0;
	  countB = 0;
	}
	if(countB==k)flgB = true;
	if(countR==k)flgR = true;
      }
    }
    for(int x=0; x<n; x++){
      countR = 0;
      countB = 0;
      for(int y=0; y<n; y++){
	if(rt[y][x] == 1){
	  countR++;
	  countB = 0;
	}
	else if(rt[y][x] == 2){
	  countB++;
	  countR = 0;
	}
	else {
	  countR = 0;
	  countB = 0;
	}
	if(countB==k)flgB = true;
	if(countR==k)flgR = true;
      }
    }
    for(int y=n-1; y>=0; y--){

      countR = 0;
      countB = 0;
      for(int x=0,ny = y; ny<n && x < n; ny++,x++){
	if(rt[ny][x] == 1){
	  countR++;
	  countB = 0;
	}
	else if(rt[ny][x] == 2){
	  countB++;
	  countR = 0;
	}
	else {
	  countR = 0;
	  countB = 0;
	}
	if(countB==k)flgB = true;
	if(countR==k)flgR = true;
      }
    }
    for(int x=0; x<n; x++){

      countR = 0;
      countB = 0;
      for(int nx=x,y = 0; nx<n && y < n; nx++,y++){
	if(rt[y][nx] == 1){
	  countR++;
	  countB = 0;
	}
	else if(rt[y][nx] == 2){
	  countB++;
	  countR = 0;
	}
	else {
	  countR = 0;
	  countB = 0;
	}
	if(countB==k)flgB = true;
	if(countR==k)flgR = true;
      }
    }
    for(int y=n-1; y>=0; y--){
      countR = 0;
      countB = 0;
      for(int x=n-1,ny = y; ny<n && x>=0; ny++,x--){
	if(rt[ny][x] == 1){
	  countR++;
	  countB = 0;
	}
	else if(rt[ny][x] == 2){
	  countB++;
	  countR = 0;
	}
	else {
	  countR = 0;
	  countB = 0;
	}
	if(countB==k)flgB = true;
	if(countR==k)flgR = true;
      }
    }
    for(int x=n-1; x>=0; x--){
      countR = 0;
      countB = 0;
      for(int nx=x,y = 0; nx>=0 && y < n; nx--,y++){
	if(rt[y][nx] == 1){
	  countR++;
	  countB = 0;
	}
	else if(rt[y][nx] == 2){
	  countB++;
	  countR = 0;
	}
	else {
	  countR = 0;
	  countB = 0;
	}
	if(countB==k)flgB = true;
	if(countR==k)flgR = true;
      }
    }
    if(flgB && flgR)cout << "Both" << endl;
    else if(flgB)cout << "Blue" << endl;
    else if(flgR)cout << "Red" << endl;
    else cout << "Neither" << endl;
  }
  return 0;
}
