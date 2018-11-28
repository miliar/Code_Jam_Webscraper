#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
using namespace std;

typedef pair<int,int> pii;

ifstream fin("b.in");
ofstream fout("b.out");

int h,w;

int height[110][110];
int ind[110][110];
int used[110][110];

int mx[] = {-1,0,0,1};
int my[] = {0,-1,1,0};

int ch[30];

int main() {
	int t,T;
	int i,j,x,y,k,kk;
	fin>>T;
	for(t=1;t<=T;++t) {
		fin>>h>>w;
		for(i=0;i<h;++i) for(j=0;j<w;++j) fin>>height[i][j];
		int next = 0;
		for(i=0;i<h;++i) for(j=0;j<w;++j) {
			bool lowest = true;
			for(k=0;k<4;++k) {
				x = i + mx[k];
				y = j + my[k];
				if(x>=0 && y>=0 && x<h && y<w) {
					if(height[x][y]<height[i][j]){lowest = false;}
				}
			}
			//cout<<i<<" "<<j<<endl;
			if(!lowest)continue;
			//cout<<i<<" "<<j<<endl;
			ind[i][j] = next;
			queue<pii> q;
			q.push( pii(i,j) );
			for(x=0;x<h;++x) for(y=0;y<w;++y) used[x][y]=0;
			used[i][j]=1;
			pii c,n;
			while(!q.empty()) {
				c = q.front();
				q.pop();
				pii best = pii(-1,-1);
				for(k=0;k<4;++k) {
					n = pii( c.first + mx[k], c.second + my[k] );
					if(n.first < 0 || n.first >= h || n.second < 0 || n.second >= w)continue;
					if(used[n.first][n.second])continue;
					best = pii(-1,-1);
					for(kk=0;kk<4;++kk) {
						x = n.first + mx[kk];
						y = n.second + my[kk];
						if(x<0 || x>=h || y<0 || y>=w)continue;
						if(height[x][y] < height[n.first][n.second]) {
							if(best.first==-1 || height[x][y]<height[best.first][best.second]) {
								best = pii(x,y);
							}
						}
					}
					if(best == c) {
						q.push(n);
						used[n.first][n.second]=1;
						ind[n.first][n.second]=next;
					}
				}
			}
			++next;
		}
		fout<<"Case #"<<t<<":"<<endl;
		for(i=0;i<26;++i)ch[i] = -1;
		next = 0;
		for(i=0;i<h;++i) {
			for(j=0;j<w;++j) {
				if(ch[ind[i][j]]==-1) {
					ch[ind[i][j]]=next++;
				}
				fout<<(char)('a'+ch[ind[i][j]]);
				if(j<w-1)fout<<" ";
			}
			fout<<endl;
		}
	}
	return 0;
}
