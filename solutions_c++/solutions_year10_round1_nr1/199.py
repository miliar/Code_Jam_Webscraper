/*
 *  A.cpp
 *  
 *
 *  Created by Pro.hessam on ۸۹/۳/۱.
 *  Copyright 2010 __MyCompanyName__. All rights reserved.
 *
 */

#include <iostream>

using namespace std;

const int move_x[]= {0, 1, 1, 1, 0, -1, -1, -1}, move_y[]= {1, 1, 0, -1, -1, -1, 0, 1};
const int MaxN= 50 + 3;
int n, k;
int g[MaxN][MaxN];

inline bool avl(int x, int y){
	return x>=0 && y>=0 && x<n && y<n;
}
/********************************/
inline bool nice(int x, int y, int dx, int dy){
	int fine= 1;
	while(avl(x+dx, y+dy) && g[x][y]==g[x+dx][y+dy]){
		x+= dx;
		y+= dy;
		fine++;
	}
	return (fine>=k);
}
/********************************/
int main(){
	int test;
	cin >> test;
	for (int t=1 ; t<=test ; t++){
		cin >> n >> k;
		for (int i=0 ; i<n ; i++){
			for (int j=0 ; j<n ; j++){
				char ch;
				scanf(" %c", &ch);
				if (ch == 'R')
					g[i][j]= 1;
				else if (ch == 'B')
					g[i][j]= 2;
				else
					g[i][j]= 0;
			}
			int cnt= n;
			for (int j=n-1 ; j>=0 ; j--)
				if (g[i][j])
					swap(g[i][j], g[i][--cnt]);
		}
		bool rwin= false, bwin= false;
		for (int i=0 ; i<n ; i++)
			for (int j=0 ; j<n ; j++)
				if (g[i][j]==1 && !rwin){
					for (int d=0 ; d<8 ; d++)
						if (nice(i, j, move_x[d], move_y[d])){
							rwin= true;
							break;
						}
				}else if (g[i][j]==2 && !bwin){
					for (int d=0 ; d<8 ; d++)
						if (nice(i, j, move_x[d], move_y[d])){
							bwin= true;
							break;
						}
				}
		printf("Case #%d: ", t);
		if (rwin && bwin)
			cout << "Both" << endl;
		else if (rwin && !bwin)
			cout << "Red" << endl;
		else if (!rwin && bwin)
			cout << "Blue" << endl;
		else if (!rwin && !bwin)
			cout << "Neither" << endl;
		
	}
	
	return 0;
}

