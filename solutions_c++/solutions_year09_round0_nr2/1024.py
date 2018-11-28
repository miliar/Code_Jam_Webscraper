/*
Problem

Geologists sometimes divide an area of land into different regions based on where rainfall flows down to. These regions are called drainage basins.

Given an elevation map (a 2-dimensional array of altitudes), label the map such that locations in the same drainage basin have the same label, subject to the following rules.

    * From each cell, water flows down to at most one of its 4 neighboring cells.
    * For each cell, if none of its 4 neighboring cells has a lower altitude than the current cell's, then the water does not flow, and the current cell is called a sink.
    * Otherwise, water flows from the current cell to the neighbor with the lowest altitude.
    * In case of a tie, water will choose the first direction with the lowest altitude from this list: North, West, East, South.

Every cell that drains directly or indirectly to the same sink is part of the same drainage basin. Each basin is labeled by a unique lower-case letter, in such a way that, when the rows of the map are concatenated from top to bottom, the resulting string is lexicographically smallest. (In particular, the basin of the most North-Western cell is always labeled 'a'.)

Input

The first line of the input file will contain the number of maps, T. T maps will follow, each starting with two integers on a line -- H and W -- the height and width of the map, in cells. The next H lines will each contain a row of the map, from north to south, each containing W integers, from west to east, specifying the altitudes of the cells.

Output

For each test case, output 1+H lines. The first line must be of the form

Case #X:

where X is the test case number, starting from 1. The next H lines must list the basin labels for each of the cells, in the same order as they appear in the input.

Limits

T ≤ 100;

Small dataset

1 ≤ H, W ≤ 10;
0 ≤ altitudes < 10.
There will be at most two basins.

Large dataset

1 ≤ H, W ≤ 100;
0 ≤ altitudes < 10,000.
There will be at most 26 basins.

Sample

Input
  	
Output
 
5
3 3
9 6 3
5 9 6
3 5 9
1 10
0 1 2 3 4 5 6 7 8 7
2 3
7 6 7
7 6 7
5 5
1 2 3 4 5
2 9 3 9 6
3 3 0 8 7
4 9 8 9 8
5 6 7 8 9
2 13
8 8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8 8
	Case #1:
a b b
a a b
a a a
Case #2:
a a a a a a a a a b
Case #3:
a a a
b b b
Case #4:
a a a a a
a a b b a
a b b b a
a b b b a
a a a a a
Case #5:
a b c d e f g h i j k l m
n o p q r s t u v w x y z
*/
#include<iostream>
using namespace std;
#define MAXALT 10000
int arr[102][102],prev[102][102];
char basin[102][102];
int T, H, W;
void mark(int pre, char col){
  if(pre == -1)
	return;
  basin[pre/(1+W)][pre%(1+W)] = col;
  mark(prev[pre/(1+W)][pre%(1+W)], col);
}

int sink(int val, int r, int c){
  if(arr[r-1][c] >= val && arr[r][c-1] >= val && arr[r][c+1] >= val && arr[r+1][c] >= val){
	//cout<<"Sink found at "<<r<<","<<c<<"; its prev is "<<prev[r][c]<<endl;
	return 1;
  }
  else
	return 0;
}
int main(){
  int i,k,m,n;
  int kase,minAlt, minR, minC,flag;
  
  char basinChar;
  scanf("%d",&T);
  for(kase=1;kase<=T;kase++){
	scanf("%d %d",&H,&W);
	for(i=0;i<=W+1;i++){
	  arr[0][i] = MAXALT;
	  arr[H+1][i] = MAXALT;
	  //basin[0][i] = 'A';
	  //prev[0][i] = -1;
	  //basin[1+H][i] = 'A';
	  //prev[1+H][i] = -1;
	}
	for(i=0;i<=H+1;i++){
	  arr[i][0] = MAXALT;
	  arr[i][W+1] = MAXALT;
	}
	for(i=1;i<=H;i++)
	  for(k=1;k<=W;k++){
		scanf("%d",&arr[i][k]);
		basin[i][k] = 0;
		prev[i][k] = -1;
	  }
	basinChar = 'a';  
	for(m=1;m<=H;m++){
	  for(n=1;n<=W;n++){
		if(basin[m][n])
		  continue;
		//cout<<"chk";
		//basin[i][k] = basinChar;
		flag = 0;
		i = m;
		k = n;
		while(!sink(arr[i][k], i, k)){
		  minAlt = arr[i-1][k];
		  minR = i-1;
		  minC = k;
		  if(arr[i][k-1] < minAlt){
			minAlt = arr[i][k-1];
			minR = i;
			minC = k-1;
		  }
		  if(arr[i][k+1] < minAlt){
			minAlt = arr[i][k+1];
			minR = i;
			minC = k+1;
		  }
		  if(arr[i+1][k] < minAlt){
			minAlt = arr[i+1][k];
			minR = i+1;
			minC = k;
		  }
		  prev[minR][minC] = i*(1+W) + k;
		  i = minR;
		  k = minC;
		  if(basin[i][k]){
			mark(prev[i][k], basin[i][k]);
			flag = 1;
			break;
		  }
		}
		if(!flag){
		  mark(i*(1+W) + k,basinChar);
		  basinChar++;
		}
	  }
	}
	printf("Case #%d:\n",kase);
	for(i=1;i<=H;i++){
	  for(k=1;k<=W;k++){
		//printf("%d,%c ",prev[i][k],basin[i][k]);
		printf("%c ",basin[i][k]);
	  }
	  printf("\n");
	}
  }
  return 0;
}
