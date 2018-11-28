
#include<string>
#include<vector>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<utility>
#include <fstream>

using namespace std;

const long inf = 100000;

int T, H, W;
vector<vector<int> > map;
vector<vector<char> > labels;

bool whereToGoMin(int i, int j, int& nextI, int& nextJ, bool useLabel =true){
  int n,w,e,s;
  if (i > 0) n = map[i-1][j];
  else n = inf;
  if (j<W-1) e = map[i][j+1];
  else e = inf;
  if (j>0) w = map[i][j-1];
  else w = inf;
  if (i<H-1) s = map[i+1][j];
  else s = inf;

  int minval = min(n,min(w,min(e,s)));
  if (minval >= map[i][j])
    return false;
  if (n == minval){
    nextI = i-1;
    nextJ=j;
  }
  else if (w == minval){
    nextI = i;
    nextJ=j-1;
  }
  else if (e == minval){
    nextI = i;
    nextJ=j+1;
  }   
  else if (s == minval){
    nextI = i+1;
    nextJ=j;
  }
  if (useLabel)
    labels[nextI][nextJ] = labels[i][j];

  return true;

}

void findAllUp(int i, int j){
  int ni, nj;
  if (i > 0 &&  labels[i-1][j] ==' ' &&  map[i-1][j] > map[i][j]) {
    bool ok = whereToGoMin(i-1,j,ni,nj, false);
    if (ok && i==ni && j==nj)
    {
      labels[i-1][j] = labels[i][j];
      findAllUp(i-1,j);
    }
  }

  if (j<W-1  &&  labels[i][j+1] ==' ' &&  map[i][j+1] > map[i][j]) {
    bool ok = whereToGoMin(i,j+1,ni,nj, false);
    if (ok && i==ni && j==nj)
    {
      labels[i][j+1] = labels[i][j];
      findAllUp(i,j+1);
    }
  }
  if (j>0  &&  labels[i][j-1] ==' ' &&  map[i][j-1] > map[i][j]) {
    bool ok = whereToGoMin(i,j-1,ni,nj, false);
    if (ok && i==ni && j==nj)
    {
      labels[i][j-1] = labels[i][j];
      findAllUp(i,j-1);
    }
  }
  if (i<H-1  &&  labels[i+1][j] ==' '  &&  map[i+1][j] > map[i][j]) {
    bool ok = whereToGoMin(i+1,j,ni,nj, false);
    if (ok && i==ni && j==nj)
    {
      labels[i+1][j] = labels[i][j];
      findAllUp(i+1,j);
    }
  }

}

int main(){


  ifstream f("B-large.in");
  ofstream r("result.out");
  f>>T;
  for (int z=0; z<T; z++){
    char bazin = 'a';
    f>>H>>W;
    map.resize(H);
    labels.resize(H);
    for (int j=0; j<H; j++){
      map[j].resize(W);
      labels[j].resize(W);
    }
    for (int i=0; i<H; i++){
      for (int j=0; j<W; j++){
        f>>map[i][j];
        labels[i][j] = ' ';
      }
    }

    for (int i=0; i<H; i++){
      for (int j=0; j<W; j++){
        if (labels[i][j] == ' '){
          //labels[i][j] = bazin;
          int nextI=i, nextJ=j;
          while (whereToGoMin(nextI,nextJ,nextI, nextJ,false)){}
          labels[nextI][nextJ]=bazin;

          findAllUp(nextI, nextJ);
          bazin++;
        }
      }
    }
    r<<"Case #"<<z+1<<":"<<endl;
    for (int i=0; i<H; i++){
      for (int j=0; j<W; j++){
        r<<labels[i][j]<<" ";
      }
      r<<endl;
    }
  }


  f.close();
  r.close();
  return 0;
}

