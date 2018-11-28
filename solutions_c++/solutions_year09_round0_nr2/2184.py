#include <iostream>
#include <vector>
using namespace std;

#define INF 0x3f3f

int h, w;
vector< vector<short> > omap;
vector< vector<short> > bmap;
short travel[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
short cur = 0;

bool isValidCell(int r, int c){
  if (r >= 0 && r < h && c >= 0 && c < w)
    return true;
  return false;
}

short traceStream(int r, int c){
  if (bmap[r][c] != INF)
    return bmap[r][c];

  short lowest = INF;
  short lowestIndex = INF;
  for (int i = 0; i < 4; ++i){
    int tr = r + travel[i][0], tc = c + travel[i][1];
    int min = omap[r][c] > lowest ? lowest : omap[r][c];
    if (isValidCell(tr, tc) && omap[tr][tc] < min){
      lowest = omap[tr][tc];
      lowestIndex = i;
    }
  }
  
  if (lowest == INF){
    bmap[r][c] = cur++;
    return bmap[r][c];
  }
  return bmap[r][c] = traceStream(r + travel[lowestIndex][0], 
				  c + travel[lowestIndex][1]);
}

void produceMap(){
  for (int i = 0; i < h; ++i)
    for (int j = 0; j < w; ++j)
      traceStream(i, j);
}

void outputMap(){
  for (int i = 0; i < h; ++i){
    for (int j = 0; j < w; ++j){
      cout<<(char)(bmap[i][j] + (short)'a');
      if (j != w - 1)
	cout<<" ";
    }
    cout<<endl;
  }
}

int main(){
  int t;
  cin>>t;
  for (int k = 1; k <= t; ++k){
    cin>>h>>w;
    omap.resize(h);
    bmap.resize(h);
    for (int i = 0; i < h; ++i){
      omap[i].resize(w);
      bmap[i].resize(w);
      for (int j = 0; j < w; ++j){
	cin>>omap[i][j];
	bmap[i][j] = INF;
      }
    }
    
    produceMap();

    cout<<"Case #"<<k<<":"<<endl;
    outputMap();
    
    omap.clear();
    cur = 0;
  }
}
