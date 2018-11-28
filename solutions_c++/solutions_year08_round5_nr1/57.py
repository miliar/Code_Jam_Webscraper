
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

#define SZ 500

char data[SZ][SZ];

int dx[4] = {0,1,0,-1};
int dy[4] = {1,0,-1,0};

int main(void){
	int cases;
	cin >> cases;
	for(int case_no=1; case_no<=cases; case_no++){
		int L;
		cin >> L;
		memset(data, '.', sizeof(data));
		int dir = 0;
		int cx = SZ/2, cy = SZ/2;
		for(int i=0; i<L; i++){
			string S;
			int T;
			cin >> S >> T;
			while(T--){
				for(int i=0; i<S.size(); i++){
					if(S[i] == 'F'){
						cx += dx[dir]; cy += dy[dir];
						data[cy][cx] = '#';
						cx += dx[dir]; cy += dy[dir];
						data[cy][cx] = '#';
					}else{
						dir = (dir + 4 + (S[i] == 'L' ? 1 : -1))&3;
					}
				}
			}
		}
		int ans = 0;
		assert(cx == SZ/2 && cy == SZ/2);
		for(int rot_no = 0; rot_no < 2; rot_no++){
			for(int y=1; y<SZ; y+=2){
				int nwall = 0, curwall = 0;
				for(int x=0; x<SZ; x++)
					nwall += data[y][x] == '#';
				for(int x=0; x<SZ; x++){
					if(data[y][x] == '#'){
						curwall++;
					}else if(data[y][x] == '.' && (x&1) &&
									 curwall != 0 &&((curwall&1)== 0)&& curwall != nwall){
						data[y][x] = '@';
						ans++;
					}
				}
			}
			for(int y=0; y<SZ; y++)
				for(int x=0; x<y; x++)
					swap(data[y][x], data[x][y]);
		}
		cout << "Case #"<<case_no<<": " << ans << endl;
	}
	return 0;
}
