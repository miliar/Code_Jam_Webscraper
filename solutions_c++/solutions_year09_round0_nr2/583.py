#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <map>
#include <algorithm>

#define For(i,n) for(int i=0;i<(n);i++)
#define For1(i,n) for(int i=1;i<=(n);i++)

using namespace std;

int DAT[110][110];
int RES[110][110];
int* STK[10010];

//sinc,n,w,e,s:01234
bool st(int a, int ad, int b, int bd){
  if(a<b) return true;
  if(a==b && ad < bd) return true;
  return false;
}

int trace(int h,int w,int ind){
  int dir;
  int sti=0;
  while((dir=RES[h][w])>0){
    STK[sti]=&RES[h][w];
    sti++;
    switch(dir){
      case 1:
        h--;
        break;
      case 2:
        w--;
        break;
      case 3:
        w++;
        break;
      case 4:
        h++;
        break;
    }
  }
  if(RES[h][w]==0){ //new sink
    for(int i=0;i<sti;i++){
      *(STK[i]) = ind;
    }
    RES[h][w] = ind;
    return ind-1;
  }
  // existing index
  for(int i=0;i<sti;i++){
    *(STK[i]) = RES[h][w];
  }
  return ind;
}

int main(){
  int CN, H, W;
  cin >> CN;
  For1(CI,CN){
    memset(DAT,0,sizeof(DAT));
    memset(RES,0,sizeof(RES));
    memset(STK,0,sizeof(STK));
    cin >> H >> W;
    For(h,H){
      For(w,W){
        cin >> DAT[h][w];
      }
    }
    For(h,H){
      For(w,W){
        int min=DAT[h][w];
        int mind=0;
        if(h>0){
          //north
          if(st(DAT[h-1][w], 1, min, mind)){
            min=DAT[h-1][w];
            mind=1;
          }
        }
        if(w>0){
          //west
          if(st(DAT[h][w-1], 2, min, mind)){
            min=DAT[h][w-1];
            mind=2;
          }
        }
        if(w<W-1){
          //east
          if(st(DAT[h][w+1], 3, min, mind)){
            min=DAT[h][w+1];
            mind=3;
          }
        }
        if(h<H-1){
          //south
          if(st(DAT[h+1][w], 4, min, mind)){
            min=DAT[h+1][w];
            mind=4;
          }
        }
        RES[h][w]=mind;
      }
    }
    int ind=-1;//'a'
    For(h,H){
      For(w,W){
        ind = trace(h,w,ind);
      }
    }

    cout << "Case #" << CI << ":" << endl;
    For(h,H){
      For(w,W-1){
        cout.put('a'-RES[h][w]-1) << " ";
      }
      cout.put('a'-RES[h][W-1]-1) << endl;
    }
  }
}
