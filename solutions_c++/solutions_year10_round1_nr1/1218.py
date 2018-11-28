/*
 * Rotate
 */
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

int N,K;
const int maxn = 105;
char G[maxn][maxn];
char E[maxn][maxn];

void Input(){
	cin >> N >> K;
	scanf("\n");

	for(int i = 0;i<N;i++){
		scanf("%s",G[i]);
	}

	/*
	for(int i = 0;i<N;i++){
		cout << G[i] << endl;
	}
	*/
}

void Gravity(int y,int x,char c){
	int i;
	for(i = N-1;i>=0;i--){
		if(E[y][i] == 0) break;
	}
	E[y][i] = c;
}
		

void Rotate(){
	memset(E,0,sizeof(E));
	for(int i = N-1;i>=0;i--){
		for(int j = 0;j<N;j++){
			if(G[j][i] != '.') Gravity(j,i,G[j][i]);
		}
	}
}

bool Row(char c){
	for(int i = 0;i<N;i++){
		bool ok = false;
		int cnt = 0;
		for(int j = 0;j<N;j++){
			if(E[i][j] == c){
				if(ok == true) cnt++;
				else cnt = 1;
				ok = true;
			}
			else ok = false;
			if(cnt == K) return true;
		}
	}
	return false;
}

bool Col(char c){
	for(int i = 0;i<N;i++){
		bool ok = false;
		int cnt = 0;
		for(int j = 0;j<N;j++){
			if(E[j][i] == c){
				if(ok == true) cnt++;
				else cnt = 1;
				ok = true;
			}
			else ok = false;
			if(cnt == K) return true;
		}
	}
	return false;
}

bool Dia(char c){
	int end = 2*N-K+1;
	for(int sum = K-1; sum < end;sum++){
		bool ok = false;
		int cnt = 0;
		for(int i = 0;i<=sum;i++){
			int j = sum-i;
			if(E[i][j] == c){
				if(ok == true) cnt++;
				else cnt = 1;
				ok = true;
			}
			else ok = false;
			if(cnt == K) return true;
		}
	}
	return false;
}

int Check(char c){
	if(c == 'R'){
		if(Row(c) || Col(c) || Dia(c))
			return 1;
		else return 0;
	}
	if(c == 'B'){
		if(Row(c) || Col(c) || Dia(c))
			return 2;
		else return 0;
	}
	return 0;
}

string Solve(){
	Input();

	Rotate();

	/*
	cout << endl;
	for(int i = 0;i<N;i++){
		for(int j = 0;j<N;j++){
			if(E[i][j] == 0) cout << " " ;
			else cout << E[i][j];
		}
		cout << endl;
	}
	*/

	int ans = 0;
	ans = Check('R')+Check('B');

	//cout << ans << endl;
	
	if(ans == 0) return "Neither";
	else if(ans == 1) return "Red";
	else if(ans == 2) return "Blue";
	else return "Both";

}

int main(){
	freopen("rotate.in","r",stdin);
	freopen("rotate.out","w",stdout);
	
	int T;
	cin >> T;

	for(int i = 1;i<=T;i++){
		cout << "Case #" << i << ": " << Solve() << endl;
	}

	return 0;
}
