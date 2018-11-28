#include <numeric>
#include <cstring>
#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <cstdlib>
#include <cctype>
#include <deque>
#include <cmath>
#include <sstream>
#include <string>
using namespace std;
typedef pair<int, int> pii;
#define mp make_pair
#define fst first
#define snd second
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
int N, k;
char mapa[60][60];
char aux[60][60];

void rota(){
	//empuja a derecha
	for(int i = 0; i < N; i++) for(int j = 0; j < N; j++) aux[i][j] = '.';
	
	for(int i = 0; i < N; i++){
	 int pos = N - 1;
	 for(int j = N - 1 ; j >= 0; j--){
	 	if(mapa[i][j] != '.') 
	 		aux[i][pos--] = mapa[i][j];
	 }
	}
	for(int i = 0; i < N; i++) for(int j = 0; j < N; j++) mapa[i][j] = aux[i][j];
		
}
int dx[] = {1, 0, 1, 1};
int dy[] = {0, 1, -1, 1};
 
bool gana(char who){
	for(int i = 0; i < N; i++) 
	for(int j = 0; j < N; j++) if(mapa[i][j] == who){
		
		for(int kk = 0; kk < 4; kk++){
			int x = i, y = j;
			int d;
			for(d = 0; d < k - 1; d++){
				x = x + dx[kk];
				y = y + dy[kk];
				if(x < 0 || y < 0 || x >= N || y >= N || mapa[x][y] != who) break;
			}
			if(d == k - 1) return true;
		}		
	}
	return false;
}

int main(){
	int tt;
	cin >> tt;
	for(int casos = 1; casos <= tt; casos++){
		cin >> N >> k;
		for(int i = 0; i < N; i++) for(int j = 0; j < N; j++)
			cin >> mapa[i][j];
			
		rota();
		bool b = false, r = false;
		if(gana('B')) b = true;
		if(gana('R')) r = true;
	
//		for(int i = 0; i < N; i++){ for(int j = 0; j < N; j++)
//			printf("%c", mapa[i][j]);
//			cout << endl;
//		}
		cout << "Case #"<<casos<<": "; 
		if(b && r) cout << "Both" << endl;
		else if(r) cout << "Red" << endl;
		else if(b) cout << "Blue" << endl;
		else cout << "Neither" << endl;
	}
}
