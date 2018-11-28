#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int m[26+'A']={0};
char A;
bool check(){
	if ((m['X']==3&&m['T']==1)||m['X']==4){
		A='X';
		memset(m,0,sizeof(m));
		return true;
	}
	if ((m['O']==3&&m['T']==1)||m['O']==4){
		A='O';
		memset(m,0,sizeof(m));
		return true;
	}
	A='.';
	memset(m,0,sizeof(m));
	return false;
}



int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,D;
	char c[4][4];
	
	cin >> T;
	for (int t = 0; t < T; t++){
		D=0;
		cin >> c[0] >> c[1] >> c[2] >> c[3];
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				if (c[i][j]!='.')D++;
			}
		}
		m[(int)c[0][0]]++;m[(int)c[0][1]]++;m[(int)c[0][2]]++;m[(int)c[0][3]]++;if (check()) goto ret;
		m[(int)c[1][0]]++;m[(int)c[1][1]]++;m[(int)c[1][2]]++;m[(int)c[1][3]]++;if (check()) goto ret;
		m[(int)c[2][0]]++;m[(int)c[2][1]]++;m[(int)c[2][2]]++;m[(int)c[2][3]]++;if (check()) goto ret;
		m[(int)c[3][0]]++;m[(int)c[3][1]]++;m[(int)c[3][2]]++;m[(int)c[3][3]]++;if (check()) goto ret;
		m[(int)c[0][0]]++;m[(int)c[1][0]]++;m[(int)c[2][0]]++;m[(int)c[3][0]]++;if (check()) goto ret;
		m[(int)c[0][1]]++;m[(int)c[1][1]]++;m[(int)c[2][1]]++;m[(int)c[3][1]]++;if (check()) goto ret;
		m[(int)c[0][2]]++;m[(int)c[1][2]]++;m[(int)c[2][2]]++;m[(int)c[3][2]]++;if (check()) goto ret;
		m[(int)c[0][3]]++;m[(int)c[1][3]]++;m[(int)c[2][3]]++;m[(int)c[3][3]]++;if (check()) goto ret;
		m[(int)c[0][0]]++;m[(int)c[1][1]]++;m[(int)c[2][2]]++;m[(int)c[3][3]]++;if (check()) goto ret;
		m[(int)c[0][3]]++;m[(int)c[1][2]]++;m[(int)c[2][1]]++;m[(int)c[3][0]]++;if (check()) goto ret;
	ret:
		cout << "Case #" << t+1 << ": ";
		if (A=='.'){
			if (D==16) cout << "Draw" << endl;
			else cout << "Game has not completed" << endl;
		}else cout << A << " won" << endl;
	}
	return 0;
}
