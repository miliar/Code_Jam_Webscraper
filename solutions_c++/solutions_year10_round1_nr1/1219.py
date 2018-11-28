#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <cmath>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <climits>
#include <cstring>
#include <cctype>
#define x first
#define y second
#define in(x, n) (0 <= (x) && (x) <= n)
using namespace std;

typedef pair<int, int> Point;

void imprime(string m[], int n){
	int i, j;
	for(i = 0; i < n; i++)
		cout << m[i] << endl;
	cout << endl;
	return;
}

bool busca(int f, int c, string s[], char color, int n, int k){
	int i, j, p, cont;
	for(i = c+1, cont = 1; i < n; i++){
		if(s[f][i] == color)
			cont++;
		else
			break;
	}
	for(i = c-1; i >= 0; i--){
		if(s[f][i] == color)
			cont++;
		else
			break;
	}
	if(cont >= k)
		return true;
	for(i = f+1, cont = 1; i < n; i++){
		if(s[i][c] == color)
			cont++;
		else
			break;
	}
	for(i = f-1; i >= 0; i--){
		if(s[i][c] == color)
			cont++;
		else
			break;
	}
	if(cont >= k)
		return true;
	for(i = f-1, j = c-1, cont = 1; i >= 0 && j >= 0; i--, j--){
		if(s[i][j] == color)
			cont++;
		else
			break;
	}
	for(i = f+1, j = c+1; i <n && j <n; i++, j++){
		if(s[i][j] == color)
			cont++;
		else
			break;
	}	
	if(cont >= k)
		return true;
	return false;
}

int main(){
	string s[52], m[52];
	register int i, j, n, t, k, z, p, q;
	bool v[2];
	cin >> t;
	for(z = 1; z <= t; z++){
		cin >> n >> k;
		for(i = 0; i < n; i++){
			cin >> s[i];
			m[i] = s[i];
		}
		for(i = n-1, p = 0; i >= 0; i--, p++)
			for(j = 0; j < n; j++)
				m[j][p] = s[i][j];
//		imprime(m, n);
		for(i = n-1; i >= 0; i--){
				p = q = n-1;
				do{
					for(; p >= 0 && m[p][i] == '.';p--);
					if(p < 0)
						break;
					for(; q >= 0 && m[q][i] != '.';q--);
					if(q > p){
/*					
						cout << q << " " << p << endl;
						cout << m[q][i] << m[p][i]<<endl;*/
						m[q][i] = m[p][i];
						m[p][i] = '.';
						p--;
						q--;
					}
					else
						p--;
				}while(true);
		}
//		imprime(m, n);
		v[0] = v[1] = false;
		for(i = 0; i < n; i++){
			for(j = 0; j < n; j++){
				if(m[i][j] == 'R'){
					if(busca(i, j, m, 'R', n, k)){
						v[0] = true;
					}
				}
				else if(m[i][j] == 'B'){
					if(busca(i, j, m, 'B', n, k)){
						v[1] = true;			
					}		
				}
			}
			if(v[0] && v[1])
				break;
		}
		if(v[0] && v[1])
			cout << "Case #"<< z<<": Both" << endl;
		else if(v[0])
			cout << "Case #"<< z<<": Red" << endl;
		else if(v[1])
			cout << "Case #"<< z<<": Blue" << endl;			
		else
			cout << "Case #"<< z<<": Neither" << endl;			
	}
	return 0;
}
