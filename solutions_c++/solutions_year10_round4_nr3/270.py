/*
 *  C.cpp
 *  
 *
 *  Created by Pro.hessam on ۸۹/۳/۱۵.
 *  Copyright 2010 __MyCompanyName__. All rights reserved.
 *
 */

#include <iostream>

using namespace std;

const int MaxN= 100 + 3;
int n;
int g[MaxN][MaxN], m[MaxN][MaxN];


inline void cp(int a[][MaxN], int b[][MaxN]){
	for (int i=0 ; i<MaxN ; i++)
		for (int j=0 ; j<MaxN ; j++)
			b[i][j]= a[i][j];
}
/*******************************/
int main(){
	int test;
	cin >> test;
	for (int t=1 ; t<=test; t++){
		cin >> n;
		memset(g, 0, sizeof g);
		for (int i=0 ; i<n ; i++){
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			if (x1 > x2)
				swap(x1, x2);
			if (y1 > y2)
				swap(y1, y2);
			for (int r=x1 ; r<=x2 ; r++)
				for (int c=y1 ; c<=y2 ; c++)
					g[r][c]= true;
		}
		for (int i=0 ; i<MaxN ; i++)
			for (int j=0 ; j<MaxN ; j++)
				m[i][j]= g[i][j];
		bool flag= true;
		int res= 0;
		while(flag){
			flag= false;
			res++;
			for (int i=1 ; i<=100 ; i++)
				for (int j=0 ; j<=100 ; j++){
					if (g[i][j] == g[i-1][j+1])
						m[i][j+1]= g[i][j];
					if (g[i][j]){
						flag= true;
					}
				}
			for (int i=0 ; i<MaxN ; i++)
				for (int j=0 ; j<MaxN ; j++)
					g[i][j]= m[i][j];
		}
		res--;
		printf("Case #%d: %d\n",t, res);
	}
	return 0;
}

