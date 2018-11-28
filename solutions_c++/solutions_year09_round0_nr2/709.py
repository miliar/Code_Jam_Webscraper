#include<iostream>
#include<cstring>
#include<fstream>
#include<vector>
using namespace std;
int map[100][100];
char rtn[100][100];
int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};
vector <int> xs;
vector<int> ys;

char next;
int ca,r,c;
char compute(int x, int y){
	while(true){
		if(rtn[x][y])
			break;
		xs.push_back(x);
		ys.push_back(y);
		int alt=map[x][y];
		int nnx=-1;
		int nny=-1;
		int min=alt;
		for(int i=0; i<4; ++i){
			int nx=x+dx[i];
			int ny=y+dy[i];
			if(nx>=0 && ny>=0 && nx<r && ny<c && map[nx][ny]<min){
				min=map[nx][ny];
				nnx=nx;
				nny=ny;
			}
		}
		if(nnx==-1)
			break;
		x=nnx;
		y=nny;
	}
	if(rtn[x][y]){
		return rtn[x][y];
	}else{
		char r=next++;
		return r;
	}
}


int main(){
	ifstream fin("B.in");
	ofstream fout("B.out");
	


	fin>>ca;
	for(int cas=1; cas<=ca; ++cas){
		fin>>r>>c;
		next='a';
		for(int i=0; i<r; ++i){
			for(int j=0; j<c; ++j){
				fin>>map[i][j];
				rtn[i][j]=0;
			}
		}
		for(int i=0; i<r; ++i){
			for(int j=0; j<c; ++j){
				if(!rtn[i][j]){
					xs.clear();
					ys.clear();
					char c=compute(i,j);
					for(int i=0; i<xs.size(); ++i){
						rtn[xs[i]][ys[i]]=c;
					}
				}
			}
		}
		fout<<"Case #"<<cas<<":"<<endl;
		for(int i=0; i<r; ++i){
			for(int j=0; j<c; ++j){
				if(j) fout<<" ";
				fout<<rtn[i][j];
			}
			fout<<endl;
		}
	}
}
