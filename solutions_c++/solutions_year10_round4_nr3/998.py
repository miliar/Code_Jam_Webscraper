#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <time.h>
#include <vector>
#include <time.h>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <stdio.h>
#define all(c) c.begin(), c.end() 
#define PI 3.141592653
#define PAUSE system("pause")
#define FOR(i,j) for(int i=0;i<j;i++)
#define VI vector<int> 
#define VS vector<string>
#define MAX(i,j) i>j? i:j
#define SZ(i) i.size()
using namespace std;

ifstream input("C:/Users/Yeqi SUN/Desktop/C-small-attempt1.in");
ofstream output("C:/Users/Yeqi SUN/Desktop/test.out");

		int grid[200][200][2];
		double life[200][200];


void main(){
	int C,R,x1,y1,x2,y2;
	input >> C;
	FOR(i,C){

		FOR(j,200){
			FOR(k, 200){
				FOR(t,2)
					grid[j][k][t] = 0;
			}
		}
		input >> R;
		FOR(j,R){
			input >> x1 >> y1 >> x2 >> y2;
			for(int m=x1; m<=x2;m++ ){
				for(int n=y1; n<=y2;n++){
					grid[m][n][0] = 1;
				}
			}
		}
		int s = 0;
		int cnt = 1;
		while(1){
			int flag = 0;
			FOR(j,200){
				FOR(k, 200){
					if (j==0 || k ==0)
						grid[j][k][1-s] = 0;
					if( grid[j-1][k][s] == 1 && grid[j][k-1][s] == 1){
						grid[j][k][1-s] = 1;
						flag = 1;
					}else{
						if ( grid[j-1][k][s] == 1 || grid[j][k-1][s] == 1){
							if (grid[j][k][s] == 1){
								grid[j][k][1-s] = 1;
								flag = 1;
							}
							else
								grid[j][k][1-s] = 0;
						}else
							grid[j][k][1-s] = 0;
						
					}
				}
			}
			if(flag ==0)
				break;
			cnt++;
			s = 1-s; 

		}
		output << "Case #" << i+1 << ": " << cnt << endl;




	}







	PAUSE;
}