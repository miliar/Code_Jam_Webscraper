								/* in the name of Allah */
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <cstdio>
#include <cmath>
#include <map>

using namespace std;

ifstream fin("C_House of Kittens.in");
ofstream fout("C_House of Kittens.out");

#define cin fin
#define cout fout

int n, m;
int e[10][2], col[10];
bool mat[10][10];

bool isGood(int ted){
	bool mark[5];
	for(int i = 0; i < m; i++){
		for(int j = 0; j < 2; j++){
			for(int k = 0; k < ted; k++)
				mark[k] = false;
			int s = e[i][j];
			bool fl = true;
			int t = e[i][1 - j];
			mark[col[s]] = mark[col[t]] = true;
			while(s != t){
				int idx = s + 1;
				if(idx == n) idx = 0;
				int k = idx;
				while(k != t){
					k++;
					if(k == n)
						k = 0;
					if(k == t && s == e[i][j])
						break;
					if(mat[s][k])
						idx = k;
				}
				mark[col[idx]] = true;
				s = idx;
			}
			for(int k = 0; k < ted; k++)
				if(!mark[k])
					return false;
		}
	}
	return true;
}

bool bt(int idx, int ted){
	if(idx == n)
		return isGood(ted);
	for(int i = 0; i < ted; i++){
		col[idx] = i;
		if(bt(idx + 1, ted))
			return true;
	}
	return false;
}

bool can(int ted){
	if(ted == 1){
		for(int i = 0; i < n; i++)
			col[i] = 0;
		return true;
	}
	if(bt(0, ted))
		return true;
	return false;
}

int main(){
	int T, test = 0;
	for(cin >> T; T--; ){
		cin >> n >> m;
		memset(mat, false, sizeof mat);
		for(int i = 0; i < m; i++)
			cin >> e[i][0];
		for(int i = 0; i < m; i++)
			cin >> e[i][1];
		for(int i = 0; i < m; i++){
			e[i][0]--, e[i][1]--;
			mat[e[i][0]][e[i][1]] = mat[e[i][1]][e[i][0]] = true;
		}
		int res = 5;
		while(!can(res))
			res--;
		cout << "Case #" << ++test << ": " << res << endl;
		for(int i = 0; i < n; i++){
			if(i > 0) cout << ' ';
			cout << col[i] + 1;
		}
		cout << endl;
	}
	return 0;
}