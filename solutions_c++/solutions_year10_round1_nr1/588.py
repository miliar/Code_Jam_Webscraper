#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <map>
#include <fstream>
using namespace std;
typedef long long ll;
const int MAXN = 60;

int N;
char mp[MAXN][MAXN], mp2[MAXN][MAXN];
int valid(int r, int c){
	return r>=0 && r<N && c>=0 && c<N;
}
int calc(char board[][MAXN], int m, char ch){
	int res = 0, nr, nc;
	for(int i = 0; i < N; ++i)
		for(int j = 0; j < N; ++j)if(board[i][j] == ch){
			int cnt = 1;
			//row
			for(int k = j+1; k < N; ++k)
				if(board[i][k] == ch)++cnt;
				else break;
			if(cnt >= m)return 1;
			//col
			cnt = 1;
			for(int k = i+1; k < N; ++k)
				if(board[k][j] == ch)++cnt;
				else break;
			if(cnt >= m)return 1;
			//left down
			cnt = 1;
			nr = i+1;	nc = j-1;
			while(valid(nr, nc) && board[nr][nc] == ch){
				++cnt;
				nr++;	nc--;
			}
			if(cnt >= m)return 1;
			//right down
			cnt = 1;
			nr = i+1;	nc = j+1;
			while(valid(nr, nc) && board[nr][nc] == ch){
				++cnt;
				nr++;	nc++;
			}
			if(cnt >= m)return 1;
		}
	return 0;
}			
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, k, f1, f2;
	cin>>T;
	for(int tt = 1; tt <= T; ++tt){
		cin>>N>>k;
		for(int i = 0; i < N; ++i)
			cin>>mp[i];
		for(int i = 0; i < N; ++i)
			for(int j = 0; j < N; ++j)
				mp2[i][j] = mp[N-1-j][i];
		for(int i = N-1; i >= 0; --i)
			for(int j = 0; j < N; ++j)if(mp2[i][j] != '.'){
				int k;
				for(k = i + 1; k < N; ++k)
					if(mp2[k][j] != '.')break;
				--k;
				if(mp2[k][j] == '.'){
					mp2[k][j] = mp2[i][j];
					mp2[i][j] = '.';
				}
			}
		f1 = calc(mp2, k, 'R');
		f2 = calc(mp2, k, 'B');
		cout<<"Case #"<<tt<<": ";
		if(f1 && f2)cout<<"Both"<<endl;
		else if(f1)cout<<"Red"<<endl;
		else if(f2)cout<<"Blue"<<endl;
		else cout<<"Neither"<<endl;
	}
	return 0;
}

