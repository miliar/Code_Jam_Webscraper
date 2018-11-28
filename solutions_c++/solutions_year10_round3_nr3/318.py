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
#define in(x, n) (0 <= (x) && (x) < n)
#define MAX 513
using namespace std;

typedef pair<int, int> Point;

void imprime(bool v[MAX][MAX], int m, int n){
	int i, j;
	for(i = 0; i < m; i++, cout << endl)
		for(j = 0; j < n; j++)
			cout << v[i][j] << " ";
	return;
}

int main(){
	register int a, b, i, j, n, m, z,k, t, suma;
	bool mat[MAX][MAX], u[MAX][MAX], v[MAX], ok;
	string s;
	map<int, int> dicc;
	map<int, int>::iterator it;
	pair<int, int> vec[MAX];
	cin >> t;
	for(z = 1; z <= t; z++){
		cin >> m >> n;
		for(i = 0; i < m; i++){
			cin >> s;
			for(j = k = 0; j < s.size(); j++, k+=4){
				if(isdigit(s[j]))
					a = s[j]-'0';
				else
					a = s[j]-'A'+10;
				for(b = 3; b >= 0; b--, a>>=1){
					mat[i][k+b] = a&1;
				}
			}
		}
		for(i = 0; i < m; i++)
			for(j = 0; j < n;j++)
				u[i][j] = true;
		//imprime(mat, m, n);
		for(k = min(m, n); k > 1; k--){			
			for(i = 0; i <= (m-k); i++)
				for(j = 0; j <= (n-k); j++)
					if(u[i][j]){
						v[j] = mat[i][j];
						ok = true;
						for(b = j+1; b < (j+k); b++){
							v[b] = mat[i][b];
							if(v[b] == v[b-1] || !u[i][b]){
								ok = false;
								break;
							}
						}
						if(!ok)
							continue;
						for(a = i+1; a < (i+k) && ok; a++)
							for(b = j; b < (j+k); b++){
								if(v[b] == mat[a][b] || !u[a][b]){
									ok = false;
									break;
								}
								v[b] = mat[a][b];
							}	
						if(ok){
							for(a = i; a < (i+k); a++)
								for(b = j; b < (j+k); b++)
									u[a][b] = false;
							if(dicc.find(k) == dicc.end())
								dicc[k] = 1;
							else
								dicc[k]++;
						}
					}
		}
		suma = 0;
		for(it = dicc.begin(), i = 0; it != dicc.end(); it++, i++){
			vec[i] = *it;
			suma+=vec[i].x*vec[i].x*vec[i].y;
		}		
		cout << "Case #"<< z<<": "<<(dicc.size()+(suma == (m*n) ? 0 : 1)) << endl;
		for(i--; i >= 0; i--)
			cout << vec[i].x << " " << vec[i].y << endl;
		if(suma < (m*n))
			cout << 1 << " " << ((m*n)-suma) << endl;
		dicc.clear();
	}
	return 0;
}
