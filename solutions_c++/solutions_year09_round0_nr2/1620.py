#include<iostream>
#include<string>
#include<fstream>
using namespace std;

ifstream fin("B-large.in");
ofstream fout("bout.txt");

int alt[101][101];
char res[101][101];
char c;

int dir[4][2] = {{-1,0}, {0, -1}, {0, 1}, {1, 0}};
int H, W;

char dfs(int x, int y){
	int xi = -1, yi = -1, r = alt[x][y];
	if(res[x][y]!='\0') return res[x][y];
	for(int i=0; i<4; i++){
		int xx = x+dir[i][0], yy = y+dir[i][1];
		if(xx>=H || xx<0 || yy>=W || yy<0) continue;
		if(alt[xx][yy]<r){
			r = alt[xx][yy];  xi = xx, yi = yy;
		}
	}
	if(xi<0){
		res[x][y] = c; c++;
	}else{
		res[x][y] = dfs(xi, yi);
	}
	return res[x][y];
}

int main(){
	int N;  fin>>N;
	for(int i=1; i<=N; i++){
		  fin>>H>>W;
		memset(res, 0, sizeof(res));
		for(int x=0; x<H; x++)
			for(int y=0; y<W; y++) fin>>alt[x][y];
		c = 'a';
		for(int x=0; x<H; x++)
			for(int y=0; y<W; y++) if(res[x][y]=='\0'){
				dfs(x,y);
			}
			fout<<"Case #"<<i<<":"<<endl;
			for(int x=0; x<H; x++){
				for(int y=0; y<W; y++){
					if(y>0) fout<<" ";
					fout<<res[x][y];
				}
				fout<<endl;
			}
	}
}