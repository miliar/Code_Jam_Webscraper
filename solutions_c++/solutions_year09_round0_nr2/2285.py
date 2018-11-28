// SPOJ_Practice.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"




/*
ID: Poncholo
PROG: beads
LANG: C++
*/

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <string>

using namespace std;

#define LIMIT   ('z')
int dx[]={ 0, -1,  1,  0};
int dy[]={-1,  0,  0,  1};
enum direction{NORTH, WEST, EAST, SOUTH};

int main() {
    ofstream fout ("B-large.out");//stdout
    ifstream fin ("B-large.in");//stdin
	int T,H,W;
	int tabl[100][100];
	char arr[100][100];
	
//	fflush(fin);
	fin>>T;						//Case #X:
	//fout<<T<<endl;
	int X=1;
		
	while(T-->0){
		char actual='a';
		memset(arr,0,100*100);
		fin>>H>>W;
		for(int i=0;i<H;++i){
			for(int j=0;j<W;++j){
				fin>>tabl[i][j];
				arr[i][j]=0;
			}
		}
		vector<int> neigh_dir[100][100];
		for(int i=0;i<H;++i){
			for(int j=0;j<W;++j){
				bool found=false;
				int best_height=10002;
				int best_dir;
				for(int dir=NORTH;dir<4;++dir){
					int neighX=j+dx[dir];
					int neighY=i+dy[dir];
					if(neighX<0 || neighX>=W || neighY<0 || neighY>=H)continue;
					if(tabl[neighY][neighX]<tabl[i][j]){
						found=true;
						if(tabl[neighY][neighX]<best_height){
							best_height=tabl[neighY][neighX];
							best_dir=dir;
						}						
					}
				}
				if(found==true){
					neigh_dir[i][j].push_back(best_dir);
					neigh_dir[i+dy[best_dir]][j+dx[best_dir]].push_back(3-best_dir);
				}
			}
		}
		int startX=101,startY=101;
		//Now Flood Fill

		vector<int>act_X,act_Y;
		for(int i=0;i<H;++i){
			for(int j=0;j<W;++j){
				if(arr[i][j]==0){
					arr[i][j]=actual++;
					act_X.push_back(j);
					act_Y.push_back(i);
					while((int)act_X.size()>0){
						vector<int>temp_X,temp_Y;
						for(int k=0;k<(int)act_X.size();++k){
							int actX=act_X[k];
							int actY=act_Y[k];
							for(int m=0;m<(int)neigh_dir[actY][actX].size();++m){								
								int dir=neigh_dir[actY][actX][m];
								int nX=actX+dx[dir],nY=actY+dy[dir];
								if(arr[nY][nX]==0){//unvisited node
									arr[nY][nX]=arr[i][j];
									temp_X.push_back(nX);
									temp_Y.push_back(nY);
								}
							}
						}
						act_X=temp_X;
						act_Y=temp_Y;
					}
				}
				if(actual==LIMIT){
					startX=j;
					startY=i;
					i=H,j=W;
				}
			}
		}
		for(int i=startY;i<H;++i){
			for(int j=startX;j<W;++j){
				if(arr[i][j]==0){
					arr[i][j]=actual;
				}
			}
		}
		fout<<"Case #"<<X<<":"<<endl;

		for(int i=0;i<H;++i){
			fout<<arr[i][0];
			for(int j=1;j<W;++j){
				fout<<" "<<arr[i][j];
			}
			fout<<endl;
		}
		++X;
	}
	//fin>>str;
	//fin.getline(str1,100);

	return 0;
}
