#include <iostream>
#include <fstream>

using namespace std;

void search(int i, int j);

const int dir[4][2]={{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int height, width, map[100][100], basin[100][100], numBasins;
bool visited[100][100];

int main() {
	ofstream fout ("googleqr2.out");
	ifstream fin ("googleqr2.in");
	int numMaps;
	fin>>numMaps;
	for(int mapNum=0; mapNum<numMaps; mapNum++){
		fin>>height>>width;
		numBasins=0;
		for(int i=0; i<height; i++)
			for(int j=0; j<width; j++){
				fin>>map[i][j];
				visited[i][j]=false;
			}
		for(int i=0; i<height; i++)
			for(int j=0; j<width; j++)
				if(!visited[i][j])
					search(i, j);
		fout<<"Case #"<<mapNum+1<<":"<<endl;
		for(int i=0; i<height; i++){
			for(int j=0; j<width; j++){
				fout<<(char)('a'+basin[i][j]);
				if(j<width-1)
					fout<<" ";
			}
			fout<<endl;
		}
	}
	return 0;
}

void search(int i, int j){
	if(visited[i][j])
		return;
	visited[i][j]=true;
	int nextI, nextJ, lowest=map[i][j];
	for(int n=0; n<4; n++)
		if(i+dir[n][0]>=0 && i+dir[n][0]<height && j+dir[n][1]>=0 && j+dir[n][1]<width && lowest>map[i+dir[n][0]][j+dir[n][1]]){
			lowest=map[i+dir[n][0]][j+dir[n][1]];
			nextI=i+dir[n][0];
			nextJ=j+dir[n][1];
		}
	if(lowest==map[i][j]){
		basin[i][j]=numBasins;
		numBasins++;
	}
	else{
		search(nextI, nextJ);
		basin[i][j]=basin[nextI][nextJ];
	}
}
