#include<iostream>
#include<vector>
#include<algorithm>
#include<cassert>
using namespace std;


const int NOT_YET = INT_MAX-1;
int M;
int tbl[10000][2];
int val[10000];
int changeble[10000];

int solve(const int node, const int v){
  if(tbl[node][v] != NOT_YET) return tbl[node][v];

  int ret = -1;
  int v11 = solve(2*node, 1);
  int v12 = solve(2*node+1, 1);
  int v01 = solve(2*node, 0);
  int v02 = solve(2*node+1, 0);

  int pand, nand, por, nor;
  pand = nand = por = nor = 10001;

  if(v11 <= 10000 && v12 <= 10000){
    pand = v11 + v12;
    por = v11 + v12;
  }  
  if(v01 <= 10000 && v12 <= 10000){
    nand = min(nand, v12 + v01);
    por = min(por, v12 + v01);
  }
  if(v02 <= 10000 && v11 <= 10000){
    nand = min(nand, v11 + v02);
    por = min(por, v11 + v02);
  }
  if(v01 <= 10000 && v02 <= 10000){
    nand = min(nand, v01 + v02);
    nor = v01 + v02;
  }


  //  cout << node << " " << nand << endl;

  
  if(val[node] == 1){//and
    if(v == 1){
      ret = pand;
    }else{
      ret = nand;
    }
  }else{//or
    if(v == 1){
      ret = por;
    }else{
      ret = nor;
    }
  }
  if(changeble[node]){  
    if(val[node] == 0){//and
      if(v == 1){
	ret = min(ret, pand + 1);
      }else{
	ret = min(ret, nand + 1);
      }
    }else{//or
      if(v == 1){
	ret = min(ret, por + 1);
      }else{
	ret = min(ret, nor + 1);
      }
    }
  }

  return tbl[node][v] = ret;
}


int main(){
  int T; cin >> T;
  for(int t=0;t<T;++t){
    int V;
    int i;
    cin >> M >> V;
    
    for(i=1;i<=M;++i)
      tbl[i][0] = tbl[i][1] = NOT_YET;
    
    for(i=1;i<=(M-1)/2;++i){
      cin >> val[i] >> changeble[i];
    }
    //    for(int i=0;i<M;++i) cout << changeble[i] << endl;

    for(;i<=M;++i){
      int v; cin >> v;
      tbl[i][v] = 0;
      tbl[i][!v] = 10001;
      changeble[i] = 0;
    }

    int r = solve(1, V);
    if(r > 10000)
      cout << "Case #" << (t+1) << ": IMPOSSIBLE" << endl;
    else
      cout << "Case #" << (t+1) << ": " << r << endl;

    
  }
  
  
}
