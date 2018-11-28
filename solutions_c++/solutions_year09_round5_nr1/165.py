#include <iostream>
#include <string>
#include <sstream>
#include <queue>
#include <set>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

#define hash(x) (x[0]+(x[1]<<8)+(x[2]<<16)+(x[3]<<24)+((long long)x[4]<<32))
#define unhash(x, n) x[0]=n&255; x[1]=(n>>8)&255; x[2]=(n>>16)&255; x[3]=(n>>24)&255; x[4]=(n>>32)&255;
const int dx[4]={0, 1, 0, -1};
const int dy[4]={1, 0, -1, 0};

int eval(){
	int R, C;
	string line;
	getline(cin, line);
	istringstream(line)>>R>>C;
	char board[12][13];
	for(int i=0; i<R; i++)
		cin.getline(board[i], 13);
	int boxcount=0;
	int goalcount=0;
	int boxes[5]={0};
	int goals[5]={0};
	for(int i=0; i<R; i++)
	for(int j=0; j<C; j++){
		switch(board[i][j]){
			case '.':
			case '#':
				break;
			case 'x':
				goals[goalcount++]=12*i+j;
				board[i][j]='.';
				break;
			case 'o':
				boxes[boxcount++]=12*i+j;
				board[i][j]='.';
				break;
			case 'w':
				goals[goalcount++]=12*i+j;
				boxes[boxcount++]=12*i+j;
				board[i][j]='.';
				break;
		}
	}
	assert(boxcount==goalcount);
	if(hash(boxes)==hash(goals))
		return 0;
	set<long long> seen;
	queue<long long> cur, next;
	seen.insert(hash(boxes));
	cur.push(hash(boxes));
	int moves=0;
	for(;;){
		if(cur.empty())
			return -1;
		while(!cur.empty()){
			long long x=cur.front();
			cur.pop();
			unhash(boxes, x);
			for(int i=0; i<boxcount; i++)
				board[boxes[i]/12][boxes[i]%12]='x';
			int dangerous;
			{
				queue<int> bfs;
				bfs.push(boxes[0]);
				board[boxes[0]/12][boxes[0]%12]='*';
				int cnt=1;
				while(!bfs.empty()){
					int f=bfs.front();
					bfs.pop();
					int y=f/12, x=f%12;
					for(int dir=0; dir<4; dir++){
						int nx=x+dx[dir], ny=y+dy[dir];
						if(0<=nx && nx<C && 0<=ny && ny<R && board[ny][nx]=='x'){
							cnt++;
							board[ny][nx]='*';
							bfs.push(12*ny+nx);
						}
					}
				}
				dangerous=cnt!=boxcount;
			}
			for(int i=0; i<boxcount; i++){
				if(!dangerous) assert(board[boxes[i]/12][boxes[i]%12]=='*');
				board[boxes[i]/12][boxes[i]%12]='x';
			}
			for(int i=0; i<boxcount; i++){
				int y=boxes[i]/12, x=boxes[i]%12;
				for(int dir=0; dir<4; dir++){
					int nx=x+dx[dir], ny=y+dy[dir];
					int fx=x-dx[dir], fy=y-dy[dir];
					if(board[ny][nx]=='.' && (0<=fx && fx<C && 0<=fy && fy<R) && board[fy][fx]=='.'){
						int nextboxes[5]={0};
						for(int j=0; j<boxcount; j++)
							nextboxes[j]=boxes[j];
						nextboxes[i]=12*ny+nx;
						if(seen.count(hash(nextboxes)))
							continue;
						board[ny][nx]='x';
						board[y][x]='.';
						int isbad=0;
						if(dangerous){
							queue<int> bfs;
							bfs.push(nextboxes[0]);
							board[nextboxes[0]/12][nextboxes[0]%12]='*';
							int cnt=1;
							while(!bfs.empty()){
								int f=bfs.front();
								bfs.pop();
								int y=f/12, x=f%12;
								for(int dir=0; dir<4; dir++){
									int nx=x+dx[dir], ny=y+dy[dir];
									if(0<=nx && nx<C && 0<=ny && ny<R && board[ny][nx]=='x'){
										cnt++;
										board[ny][nx]='*';
										bfs.push(12*ny+nx);
									}
								}
							}
							isbad=cnt!=boxcount;
							for(int i=0; i<boxcount; i++)
								board[nextboxes[i]/12][nextboxes[i]%12]='x';
						}
				//		if(!isbad){
				//			for(int i=0; i<R; i++)
				//				cout<<board[i]<<endl;
				//		}
						board[ny][nx]='.';
						board[y][x]='x';
				//		if(!isbad){
				//			for(int i=0; i<R; i++)
				//				cout<<board[i]<<endl;
				//			cout<<endl;
				//		}
						if(isbad)
							continue;
						int j=i;
						while(j>0 && nextboxes[j]<nextboxes[j-1]){
							swap(nextboxes[j], nextboxes[j-1]);
							j--;
						}
						while(j<boxcount-1 && nextboxes[j]>nextboxes[j+1]){
							swap(nextboxes[j], nextboxes[j+1]);
							j++;
						}
						if(seen.count(hash(nextboxes)))
							continue;
						if(hash(nextboxes)==hash(goals))
							return moves+1;
						seen.insert(hash(nextboxes));
						next.push(hash(nextboxes));
					}
				}
			}
			for(int i=0; i<boxcount; i++)
				board[boxes[i]/12][boxes[i]%12]='.';
			for(int i=0; i<R; i++)
			for(int j=0; j<C; j++)
				assert(board[i][j]=='.' || board[i][j]=='#');
		}
		moves++;
	//	cout<<moves<<endl;
		swap(cur, next);
	}
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		cout<<eval()<<endl;
	}
	return 0;
}
