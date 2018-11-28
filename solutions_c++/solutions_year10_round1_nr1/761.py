#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<vector>
#define all(x) x.begin() , x.end()
using namespace std;

vector<string> board;

string elimina(string s){
	string res = "";
	for(int i = 0 ; i < s.size(); i++){
		if(s[i] != '.')
			res += s[i];
	}
	int espacios = s.size() - res.size();
	for(int i = 0 ; i < espacios ; i++){
		res ='.'+res;
	}
	
	return res;
}

vector<string> rotate(vector<string> bb){
	string res = "";
	vector<string> xx(bb[0].size());
	
	for(int i = 0 ;i < bb[0].size() ; i++){
		res = "";
		for(int j = 0 ; j < bb.size() ; j++){
			res = bb[j][i]+ res;
		}
		xx[i] = res;
		
	}	
	return xx;
}


void grab(vector<string> &bbb){
	vector<string> s = bbb;
	for(int i = 0 ; i < bbb.size() ;i++){
		s[i] = elimina(bbb[i]);
	}
	
	s = rotate(s);
		bbb = s;
}


char get(int i , int j){
	if(i >= 0 && i < board.size() && j >= 0 && j < board[0].size())
		return board[i][j];
	else
		return '.';
}

int dr[] = { 1, 1, 0, -1 },
	dc[] = { 0, 1, 1, 1 };

bool tiene(char ch, int K){
	for (int k = 0 ; k< 4 ; k++) {
		for(int r = 0 ; r < board.size() ; r++)
			for(int c = 0 ; c < board.size() ; c++){
				if (get(r-dr[k],c-dc[k]) != ch) {
					int len=0;
					while (get(r+len*dr[k],c+len*dc[k]) == ch) ++len;
					
					if (len >= K) {
						return true;
					}
				}
			}
		}
}

int main(){
	int c = 1;
	int runs;
	cin >> runs;
	while(runs--){
		int n , k;
		cin >> n >> k;
		board.clear();
		board.resize(n);

		for(int i = 0 ; i < n ; i++)
			cin >> board[i];
		grab(board);
		
		int res = tiene('R',k)+tiene('B',k)*2;
		printf("Case #%d: ",c++);
		if(res == 0)
			printf("Neither");
		else if(res == 3)
			printf("Both");
		else if(res == 1)
			printf("Red");
		else
			printf("Blue");
		putchar('\n');
	}
	return 0;
}
