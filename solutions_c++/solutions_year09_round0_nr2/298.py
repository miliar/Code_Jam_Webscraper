#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <cctype>
#include <cstring>
#include <queue>
#include <stack>
#define x first
#define y second
#define MAX 103
using namespace std;

string next(string s, int &i){
	string r = "";
	if(i == s.size())
		return r;
	if(s[i] == '('){
		i++;
		while(s[i] != ')'){
			r+=s[i];
			i++;
		}
		i++;
		return r;
	}
	r = s[i];
	i++;
	return r;
}

int main(){
	int a, b, i, j, k, N, n, m, f, c, xx, yy, menor, rx, ry, v[MAX][MAX];	
	int pos[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0} };
	char ind, mat[MAX][MAX];
	bool entra, u[MAX][MAX];
	queue<pair<int, int> > q;
	pair<int, int> ins, sert;
	cin >> N;
	for(k = 1; k <= N; k++){
		cin >> n >> m;
		memset(u, false, sizeof(u));
		for(i = 0; i < n; i++)
			for(j = 0; j < m; j++)
				scanf("%d", &v[i][j]);
		ind = 'a';
		for(i = 0; i < n; i++)
			for(j = 0; j < m; j++){
				if(!u[i][j]){
					ins.x = i;
					ins.y = j;
					q.push(ins);
					u[ins.x][ins.y] = true;
					mat[ins.x][ins.y] = ind;
					while(!q.empty()){
						ins = q.front();
						q.pop();
						menor = v[ins.x][ins.y];
						entra = false;
						/*elijo a donde inundo*/
						for(a = 0; a < 4; a++){
							xx = ins.x+pos[a][0];
							yy = ins.y+pos[a][1];
							if(0 <= xx && xx < n && 0 <= yy && yy < m && v[xx][yy] < menor){
								menor = v[xx][yy];
								rx = xx;
								ry = yy;
								entra = true;
							}
						}
						if(entra && !u[rx][ry]){
							u[rx][ry] = true;
							mat[rx][ry] = ind;
							sert.x = rx;
							sert.y = ry;
							q.push(sert);
						}
						/*elijo a los que me inundan*/
						for(a = 0; a < 4; a++){
							xx = ins.x+pos[a][0];
							yy = ins.y+pos[a][1];
							/*verifico la valides del que me podria inundar y si no ha sido visitado*/
							if(0 <= xx && xx < n && 0 <= yy && yy < m && !u[xx][yy] && v[xx][yy] > v[ins.x][ins.y]){
								/*puede ser que me inunde*/
								menor = v[xx][yy];
								entra = false;
								for(b = 0; b < 4; b++){/*checo si si me inundaria*/
									f = xx+pos[b][0];
									c = yy+pos[b][1];
									if(0 <= f && f < n && 0 <= c && c < m && v[f][c] < menor){
										menor = v[f][c];
										rx = f;
										ry = c;
										entra = true;
									}
								}
								if(entra){
									if(rx == ins.x && ry == ins.y){
										sert.x = xx;
										sert.y = yy;
										mat[xx][yy] = ind;
										u[xx][yy] = true;
										q.push(sert);
									}
								}
							}
						}
					}
					if(ind == 'z')
						ind = 'a';
					else
						ind++;
				}
			}
		cout << "Case #"<< k << ":" << endl;
		for(i = 0; i < n; i++){
			putchar(mat[i][0]);
			for(j = 1; j < m; j++){
				putchar(' ');
				putchar(mat[i][j]);
			}
			putchar('\n');
		}
	}
	return 0;
}
