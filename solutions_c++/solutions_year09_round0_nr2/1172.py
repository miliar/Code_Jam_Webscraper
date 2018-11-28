// GCJ.cpp : Defines the entry point for the console application.

#include <stdio.h>

int p[10002];
//int rank[10000];
int pCell[10002];

void MakeSet(int x){
  p[x] = x;
//  rank[x] = 0;
}

void Link(int x, int y){
  if(pCell[x] >= pCell[y]){
    p[x] = y;
  }else{
    p[y] = x;
  }

/*  if(rank[x] > rank[y]){
    p[y] = x;
  }else{
    p[x] = y;
    if(rank[x] == rank[y])
      rank[y]++;
  }
*/
}

int FindSet(int x){
  if(x != p[x])
    p[x] = FindSet(p[x]);
  return p[x];
}

void Union(int x, int y){
  Link(FindSet(x), FindSet(y));
}

void Water()
{
  int T;
  int i, k;
  int H, W;

  scanf("%d", &T);
  for(i = 0; i < T; i++){
    scanf("%d", &H);
    scanf("%d", &W);

    for(k = 0; k < 10000; k++)
      p[k] = 0; // init rank[k] =

    pCell[10001] = 10001;

    int row, col;
    for(row = 0; row < H; row++){
      for(col = 0; col < W; col++){
        scanf("%d", &pCell[row*W + col]);
        MakeSet(row*W + col);
      }
    }

    for(row = 0; row < H; row++){
      for(col = 0; col < W; col++){
        int aim = 10001; //= row*W + col;
        if(row+1<H && pCell[(row+1)*W + col] <= pCell[aim]){ // south
          aim = (row+1)*W + col;
        }
        if(col+1 < W && pCell[row*W + col+1] <= pCell[aim]){ // east
            aim = row*W + col+1;
        }
        if(col-1 >= 0 && pCell[row*W + col-1] <= pCell[aim]){ // west
            aim = row*W + col-1;
        }
        if(row-1>=0 && pCell[(row-1)*W + col] <= pCell[aim]){ //North
           aim = (row-1)*W + col;
        }
        if(pCell[aim] < pCell[row*W + col])
          Union(row*W + col, aim);
      }
    }

    char pLabel[10000];
    for(k = 0; k < 10000; k++){
      pLabel[k] = 0;
    }
    
    pLabel[0] = 'a';
    int root = FindSet(0);
    pLabel[root] = 'a';
    char cur_max_lable = 'a';

    for(row = 0; row < H; row++){
      for(col = 0; col < W; col++){
        root = FindSet(row*W + col);
        if(0 == pLabel[root]){
          ++cur_max_lable;
          pLabel[row*W + col] = cur_max_lable;
          pLabel[root] = cur_max_lable;
        }
        else
         pLabel[row*W + col] = pLabel[root];
      }
    }// for H

    printf("Case #%d:\n", i+1);
    for(row = 0; row < H; row++){
      for(col = 0; col < W-1; col++){
        printf("%c ", pLabel[row*W + col]);
      }
      printf("%c\n", pLabel[row*W + col]);
    }

  }// for T
}

int main()
{
  Water();
  return 0;
}

