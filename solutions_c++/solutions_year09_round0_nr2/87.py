#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define inbounds(x, y) (0<=x && x<W && 0<=y && y<H)

int main(){
	int T;
	cin>>T;
	for(int c=1; c<=T; c++){
		int H, W;
		cin>>H>>W;
		vector<vector<int> > alt(H, vector<int>(W, 0)), basin(alt);
		for(int y=0; y<H; y++)
		for(int x=0; x<W; x++)
			cin>>alt[y][x];
		for(int b=1; ; b++){
			int lowest=100000, sx, sy;
			for(int y=0; y<H; y++)
			for(int x=0; x<W; x++){
				if(!basin[y][x] && alt[y][x]<lowest){
					lowest=alt[y][x];
					sx=x;
					sy=y;
				}
			}
			if(lowest==100000)
				break;
			queue<pair<int, int> > q;
			q.push(make_pair(sx, sy));
			basin[sy][sx]=b;
			while(!q.empty()){
				const int dx[4]={0, -1, 1, 0}, dy[4]={-1, 0, 0, 1};
				int x=q.front().first, y=q.front().second;
				q.pop();
				for(int d=0; d<4; d++){
					int nx=x+dx[d], ny=y+dy[d];
					if(!inbounds(nx, ny) || basin[ny][nx] || alt[ny][nx]<=alt[y][x])
						continue;
					int d2;
					for(d2=0; d2<4; d2++){
						int ax=nx+dx[d2], ay=ny+dy[d2];
						if(!inbounds(ax, ay))
							continue;
						if(alt[ay][ax]<alt[y][x] || (alt[ay][ax]==alt[y][x] && d2<(3-d)))
							break;
					}
					if(d2!=4)
						continue;
					basin[ny][nx]=b;
					q.push(make_pair(nx, ny));
				}
			}
		}
		char mapping[27]={0}, letter='a';
		cout<<"Case #"<<c<<":"<<endl;
		for(int y=0; y<H; y++){
			for(int x=0; x<W; x++){
				if(x) cout<<' ';
				if(!mapping[basin[y][x]])
					mapping[basin[y][x]]=letter++;
				cout<<mapping[basin[y][x]];
			}
			cout<<endl;
		}
	}
}