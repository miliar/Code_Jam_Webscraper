#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
using namespace std;

const int dir[4][2]={{-1,0},{0,-1},{0,1},{-1,0}};
ifstream fin;
ofstream fout;
int H,W,T;
int alt[100][100];
struct position {
	int x,y;
	position(int x=0,int y=0):x(x),y(y){};
	bool operator==(const position&a)const{return x==a.x&&y==a.y;}
}mark[100][100];
char S[100][100];
vector<position>pos;
bool compalt(const position&a,const position&b) {
	return alt[a.x][a.y]!=alt[b.x][b.y]?alt[a.x][a.y]<alt[b.x][b.y]:(a.x!=b.x?a.x<b.x:a.y<b.y);
}
bool inside(const position&a){return a.x>=0&&a.x<H&&a.y>=0&&a.y<W;}
int main() {
	fin.open("B.in"); fout.open("B.out");
	fin>>T;
	int cnt=0;
	while(T--) {
		pos.clear();
		fin>>H>>W;
		for(int i=0;i<H;++i)
		for(int j=0;j<W;++j) {
			fin>>alt[i][j];
			pos.push_back(position(i,j));
		}
		sort(pos.begin(),pos.end(),compalt);
		char current='a';
		for(vector<position>::iterator it=pos.begin();it!=pos.end();++it){
			int x=it->x,y=it->y;
			mark[x][y]=position(x,y);
			for(int i=0;i<4;++i) {
				position tmp=position(x+dir[i][0],y+dir[i][1]);
				if(inside(tmp)&&alt[tmp.x][tmp.y]<alt[mark[x][y].x][mark[x][y].y]) mark[x][y]=tmp;
			}
			if(mark[x][y]==position(x,y)) S[x][y]=current++;
			else S[x][y]=S[mark[x][y].x][mark[x][y].y];
		}
		fout<<"Case #"<<++cnt<<":"<<endl;
		for(int i=0;i<H;++i)
		for(int j=0;j<W;++j) {
			fout<<S[i][j];
			if(j==W-1)fout<<endl;else fout<<" ";
		}
	}
}
