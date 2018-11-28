#include <iostream>
#include <cstdio>
using namespace std;
int T;
char s[4][4];
const string str[4] = {
 "X won", "O won", "Draw", "Game has not completed"
};

bool win(char c){
	bool flag = false, mem = true;
	for(int i = 0; i < 4; i++){
		mem = true;
		for(int j = 0; j < 4; j++)
			mem  = mem && ((s[i][j] == c) || (s[i][j] == 'T'));
		flag = flag || mem;
	}
	for(int i = 0; i < 4; i++){
		mem = true;
		for(int j = 0; j < 4; j++)
			mem  = mem && ((s[j][i] == c) || (s[j][i] == 'T'));
		flag = flag || mem;
	}
	mem = true;
	for(int i = 0; i < 4; i++){
		mem = mem && (s[i][i] == c || s[i][i] == 'T');
	}
	flag = flag || mem;
	mem = true;
	for(int i = 0; i < 4; i++){
		mem = mem && (s[i][3-i] == c || s[i][3-i] == 'T');
	}
	flag = flag || mem;
	return flag;
}
bool remain(){
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++)
			if(s[i][j] == '.') return true;
	}
	return false;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	cin >> T;
	for(int cas = 1; cas <= T; cas++){
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++)
				cin >> s[i][j];
		}
		cout << "Case #" << cas << ": ";
		if(win('X')){
			cout << str[0] << endl;
		}
		else if(win('O')){
			cout << str[1] << endl;
		}
		else if(remain()){
			cout << str[3] << endl;
		}
		else cout << str[2] << endl;
	
	}
	fclose(stdin);
	fclose(stdout);
}