#include <iostream>
#include <vector>
#include <string>

using namespace std;
int lab;
int n,h,w;

vector<vector<int> > m;
vector<string> res;

bool ok(int x, int y){
  if ((x>=0)and(x<h)){
    if ((y>=0)and(y<w)){
      return true;
    }
  }return false;
}

char label(int x, int y){
  int minim = 1000000;
  int px[4]={-1,0,0,1};
  int py[4]={0,-1,1,0};
  /*for(int j = 0; j < h; ++j){
      for(int k = 0; k < w; ++k){
        if (k) cout << ' ';
        cout << res[j][k] << m[j][k];
      }
      cout << endl;
    }
    system("PAUSE");
  */
  
  if (res[x][y]!='#') return res[x][y];
  
  for(int i = 0; i < 4; ++i){
    if (ok(x+px[i],y+py[i])){
      minim=min(minim,m[x+px[i]][y+py[i]]);
    }
  }
  //cout << x << "," << y << "minim " << minim << endl;
  //Es sink?
  if (minim>=m[x][y]){
    //cout << x << "," << y << "es sink" << lab << endl;
    res[x][y]='a'+lab++;
    return res[x][y];
  }
  //cap on va?
  for(int i = 0; i < 4; ++i){
    if (ok(x+px[i],y+py[i])){
      if (m[x+px[i]][y+py[i]]==minim){
        return label(x+px[i],y+py[i]);
      }
    }
  }
  return '@';
}


int main(){
  cin >> n;
  for(int i =0; i < n; ++i){
    m.resize(0); res.resize(0);
    cin >> h >> w;
    m.resize(h); res.resize(h);
    for(int j = 0; j < h; ++j){
      m[j].resize(w); res[j].resize(w,'#');
      for(int k = 0; k < w; ++k){
        cin >> m[j][k];
      }
    }
    lab=0;
    for(int j = 0; j < h; ++j){
      for(int k = 0; k < w; ++k){
        res[j][k]=label(j,k);
      }
    }
    if (i) cout << endl;
    cout << "Case #" << i+1 << ":" << endl;
    for(int j = 0; j < h; ++j){
      for(int k = 0; k < w; ++k){
        if (k) cout << ' ';
        cout << res[j][k];// << m[j][k];
      }
      if (j<h-1) cout << endl;
    }
  }
}
