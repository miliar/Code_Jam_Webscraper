#include <iostream>
#include <math.h>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;

int a[4][4];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	long long n,i,j;
	int test;
	cin>>test;
	getchar();
	
	for (int t=1;t<=test;++t){
		string s;
		int num1 = 0, num2 = 0, num0 = 0;
		for (int i = 0;i<4; ++i){
			cin>>s;
			for (int j=0;j<4;++j){
				if (s[j] == 'X'){ a[i][j] = 1; ++num1; }
				else if (s[j] == 'O'){ a[i][j] = 2; ++num2; }
				else if (s[j] == 'T'){ a[i][j] = 3; }
				else { a[i][j] = 0; ++num0; }
			}
		}

		for (int i = 0;i<4; ++i){
			for (int j=0;j<4;++j){
				if (a[i][j] == 3){
					if (num1 > num2){
						a[i][j] = 1;
					}
					else{
						a[i][j] = 2;
					}
				}
			}
		}
		
		int player = 2;
		if (num1 > num2){
			player = 1;
		}

		bool isWin = false;
		for (int i = 0;i<4; ++i){
			if (a[i][0]==player && a[i][1]==player && a[i][2]==player && a[i][3]==player) { isWin = true; }
			if (a[0][i]==player && a[1][i]==player && a[2][i]==player && a[3][i]==player) { isWin = true; }
		}
		if (a[0][0]==player && a[1][1]==player && a[2][2]==player && a[3][3]==player) { isWin = true; }
		if (a[0][3]==player && a[1][2]==player && a[2][1]==player && a[3][0]==player) { isWin = true; }

		string ans = "";
		if (isWin){
			if (player == 1){ ans = "X won"; }
			else{ ans = "O won"; }
		}
		else if (num0>0){
			ans = "Game has not completed";
		}
		else {
			ans = "Draw";
		}

		cout<<"Case #"<<t<<": "<<ans<<'\n';
	}

	return 0;
}