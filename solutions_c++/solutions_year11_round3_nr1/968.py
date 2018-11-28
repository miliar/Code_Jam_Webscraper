#include<iostream>
#include<vector>
using namespace std;

typedef vector<char> Vc;
typedef vector<Vc> Mc;

void pinta(Mc &m) {
  for(int i = 0; i < m.size(); ++i) {
    for(int j = 0; j < m[i].size(); ++j) {
      if(m[i][j] == '#' and 
	m[i][j+1] == '#' and
	m[i+1][j] == '#' and 
	m[i+1][j+1] == '#') {
	  m[i][j] = '/';
	  m[i][j+1] = '\\';
	  m[i+1][j] = '\\';
	  m[i+1][j+1] = '/';
	  pinta(m);
      }
    }
  }
}

int main() {
  int tcas;
  cin >> tcas;
  for(int cas = 0; cas < tcas; ++cas) {
    int r,c;
    cin >> r >> c;
    Mc m(r+2,Vc(c+2,'.'));
    for(int i = 1; i+1 < m.size() ; ++i) {
      for(int j = 1; j+1 < m[i].size(); ++j) cin >> m[i][j];
    }
    pinta(m);
    bool mal = false;
    for(int i = 1; i+1 < m.size() ; ++i) {
      for(int j = 1; j+1 < m[i].size(); ++j) if(m[i][j] == '#') mal = true;
    }
    cout << "Case #"<< cas+1 << ":" << endl;
    if(mal) {
      cout << "Impossible" << endl;
    }
    else {
      for(int i = 1; i+1 < m.size() ; ++i) {
	for(int j = 1; j+1 < m[i].size(); ++j) cout << m[i][j];
	cout << endl;
      }
    }
  }
}