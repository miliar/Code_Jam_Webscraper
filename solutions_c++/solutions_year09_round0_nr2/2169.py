#include <iostream>
#include <algorithm>
#include <stdio.h>

using namespace std;

#define INF 0x3f3f3f3f

int m, n;
int mat[101][101];
char ch[101][101];
char next = 'a';

char flow(int l, int c){
	if(ch[l][c] != -1) return ch[l][c];
	int menor = INF, dir = 0;
	if(l - 1 >= 0) {
		if(mat[l-1][c] < menor) {
			menor = mat[l-1][c];
			dir = 1;
		}
	}
	if(c - 1 >= 0){
		if(mat[l][c-1] < menor){
			menor = mat[l][c-1];
			dir = 2;
		}
	}
	if(c + 1 < m) {
		if(mat[l][c+1] < menor){
			menor = mat[l][c+1];
			dir = 3;
		}
	}
	if(l + 1 < n) {
		if(mat[l+1][c] < menor){
			menor = mat[l+1][c];
			dir = 4;

		}
	}
	if(menor < mat[l][c]){
		char tmp;
	    	if(dir == 1) tmp = flow(l-1, c);
		else if(dir == 2) tmp = flow(l, c-1);
		else if(dir == 3) tmp = flow(l, c+1);
		else tmp = flow(l+1, c);
		return ch[l][c] = tmp;
	} else {
		ch[l][c] = next;
		next++;
		return ch[l][c];
	}
}

int main(){
	int T, caso = 1;
	cin>>T;
	while(T--){
		cin>>n>>m;
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				cin>>mat[i][j];
			}
		}
		memset(ch, -1, sizeof(ch));
		next = 'a';
		cout<<"Case #"<<caso++<<":"<<endl;
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				if(ch[i][j] == -1)
					flow(i, j);
				cout<<ch[i][j]<<" ";
			}
			cout<<endl;
		}
	}
	
	return 0;
}
