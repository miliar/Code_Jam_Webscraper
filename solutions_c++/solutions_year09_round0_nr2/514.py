#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <fstream>
using namespace std;

#define RAW '0'

//ifstream fin("b.in");
//#define cin fin

int mapd[100][100];
char basin[100][100];
int H, W;
char sink = 'a';

char getBasin(int i, int j){
		if(basin[i][j]==RAW){
				int mini = i, minj = j, tx, ty, min = mapd[i][j];
				int dx[] = {-1, 0, 0, 1};
				int dy[] = {0, -1, 1, 0};
				for(int x = 0; x < 4; x ++){
						tx = i+dx[x], ty = j+dy[x];
						if(tx >= 0 && tx < H
										&& ty >=0 && ty < W
										&& mapd[tx][ty] < min){
								min = mapd[tx][ty];
								mini = tx;
								minj = ty;
						}
				}
				if(mini == i && minj == j){
						basin[i][j] = sink;
						sink ++;
				}
				else
						basin[i][j]=getBasin(mini,minj);
		}
		return basin[i][j];
}
void doit(){
		sink = 'a';
		for(int i = 0; i < H; i ++){
				for(int j = 0; j < W; j ++){
						basin[i][j]=getBasin(i,j);
				}
		}
		for(int i = 0; i < H; i ++){
				for(int j = 0; j < W; j ++){
						cout<<basin[i][j];
						if(j!=W-1)
								cout<<' ';
				}
				cout<<endl;
		}
}
int main(){
		int T;
		cin>>T;
		for(int i = 0; i < T; i ++){
				cin>>H>>W;
				for(int j = 0; j < H; j ++){
						for(int k = 0; k < W; k ++){
								cin>>mapd[j][k];
								basin[j][k] = RAW;
						}
				}
				cout<<"Case #"<<i+1<<':'<<endl;
				doit();
		}
		return 0;
}
