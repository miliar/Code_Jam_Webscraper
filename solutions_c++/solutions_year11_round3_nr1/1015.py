#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include<cstring>
using namespace std;
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
char a[52][52];

int R, C;
bool check(int x, int y){
	return x >= 0 && x < R && y >= 0 && y < C && a[x][y] == '#';
}

int main(){
	//freopen("test.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("large.txt", "w", stdout);
	int T;
	string line;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		scanf("%d %d", &R, &C);
		getline(cin, line);
		for(int i = 0; i < R; i++){
			getline(cin, line);
			for(int j = 0; j < C; j++){
				a[i][j] = line[j];
			}
		}

		for(int i = 0; i < R; i++){
			for(int j = 0; j < C; j++){
				if(a[i][j] == '#'){
					if(check(i,j+1) && check(i+1, j) && check(i+1, j+1)){
						a[i][j] = '/';
						a[i][j+1] = '\\';
						a[i+1][j] = '\\';
						a[i+1][j+1] = '/';
					}
				}
			}
		}

		bool ans = true;
		for(int i = 0; i < R; i++){
			for(int j = 0; j < C; j++){
				if(a[i][j] == '#'){
					ans = false;
					break;
				}
			}
		}

		cout << "Case #" << t << ":" << endl;
		if(ans){
			for(int i = 0; i < R-1; i++){
				for(int j = 0; j < C; j++){
					cout << a[i][j];
				}
				cout << endl;
			}
			for(int j = 0; j < C; j++)
				cout << a[R-1][j];
		}
		else{
			cout << "Impossible";
		}
		if(t < T)
				cout << endl;

	}
	return 0;
}
