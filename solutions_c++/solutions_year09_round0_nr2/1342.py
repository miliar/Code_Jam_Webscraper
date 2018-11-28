#include <iostream>
#include <vector>
#include <string>

using namespace std;


bool valid(int i, int j, int n, int m) {
  if (i<0) return false;
  if (j<0) return false;
  if (i>=n) return false;
  if (j>=m) return false;
  return true;
}
void DFS(int i, int j, vector<string> &map, vector<vector<int> >&elev, char &c) {
  int n = map.size();
  int m = map[0].length();

  if (map[i][j]!=' ') return;
  map[i][j] = '1';
  

  // North
  char min = ' ';
  int mine = 10001;
  if (valid(i-1,j,n,m)) {
    if (elev[i-1][j] < mine) {
      min='N';
      mine = elev[i-1][j];
    }
  }
  if (valid(i,j-1,n,m)) {
    if (elev[i][j-1] < mine) {
      min='W';
      mine = elev[i][j-1];
    }
  }
  if (valid(i,j+1,n,m)) {
    if (elev[i][j+1] < mine) {
      min='E';
      mine = elev[i][j+1];
    }
  }
  if (valid(i+1,j,n,m)) {
    if (elev[i+1][j] < mine) {
      min='S';
      mine = elev[i+1][j];
    }
  }

  
  if (elev[i][j] > mine) {
    
    switch(min) {
    case 'N': 
      DFS(i-1,j,map, elev,c);
      return;
    case 'W':
      DFS(i,j-1,map, elev,c);
      return;
    case 'E':
      DFS(i,j+1,map, elev,c);
      return;
    case 'S':
      DFS(i+1,j,map, elev,c);
      return;
    }
  }
  
  map[i][j] = c;
  c++;
  // Sink
  return;
}
char Find_Sink(int i, int j, vector<string> &map, vector<vector<int> >&elev) {
  int n = map.size();
  int m = map[0].length();

  if ((map[i][j]>='a')&&(map[i][j]<='z')) return map[i][j];
  
  

  // North
  char min = ' ';
  int mine = 10001;
  if (valid(i-1,j,n,m)) {
    if (elev[i-1][j] < mine) {
      min='N';
      mine = elev[i-1][j];
    }
  }
  if (valid(i,j-1,n,m)) {
    if (elev[i][j-1] < mine) {
      min='W';
      mine = elev[i][j-1];
    }
  }
  if (valid(i,j+1,n,m)) {
    if (elev[i][j+1] < mine) {
      min='E';
      mine = elev[i][j+1];
    }
  }
  if (valid(i+1,j,n,m)) {
    if (elev[i+1][j] < mine) {
      min='S';
      mine = elev[i+1][j];
    }
  }

  
  if (elev[i][j] > mine) {
    
    switch(min) {
    case 'N': 
      map[i][j]=Find_Sink(i-1,j,map, elev);
      return map[i][j];
    case 'W':
      map[i][j]=Find_Sink(i,j-1,map, elev);
      return map[i][j];
    case 'E':
      map[i][j]=Find_Sink(i,j+1,map, elev);
      return map[i][j];
    case 'S':
      map[i][j]=Find_Sink(i+1,j,map, elev);
      return map[i][j];
    }
  }
  
  //map[i][j] = c;
  //c++;
  // Sink
  return map[i][j];
}

void print_map(vector<string> &map) {
  for (int i=0;i<map.size();i++) {
    for (int j=0;j<map[i].length();j++) {
      if (j==0) {
	cout << map[i][j];
      } else {
	cout << " " << map[i][j];
      }
    }
    cout << endl;
  }
}

int main() {
  int N;
  int H,W;
  cin >> N;
  vector<string> map;
  vector<vector<int> >elevs;

  for (int i1=0;i1<N;i1++) {

    cin >> H >> W;
    elevs.resize(H+1);
    map.resize(H);
    for (int j=0;j<H;j++) {
      elevs[j].resize(W+1);
      map[j]="";
      for (int k=0;k<W;k++) {
	map[j]+=' ';
      }
    }
    for (int i=0;i<H;i++) {
      for (int j=0;j<W;j++) {
	cin >> elevs[i][j];
      }
    }
    
    char c = 'a';
    for (int i=0;i<H;i++) {
      for (int j=0;j<W;j++) {
	if (map[i][j]==' ') {
	  DFS(i,j,map,elevs,c);
	  //c++;
	}
      }
    }
    //print_map(map);
    for (int i=0;i<H;i++) {
      for (int j=0;j<W;j++) {
	if (map[i][j]=='1') {
	  Find_Sink(i,j,map,elevs);
	  //c++;
	}
      }
    }



    cout << "Case #" << i1+1 << ":" << endl;
    print_map(map);
  }
}
