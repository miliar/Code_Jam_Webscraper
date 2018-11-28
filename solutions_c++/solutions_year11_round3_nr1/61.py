#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

char buf[60][60];
int t, r, c;

int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	cin >> t;
	for (int I=0; I<t; I++){
		cout << "Case #" << I+1 << ":\n";
		cin >> r >> c;
		bool bad = false;
		memset(buf, 0, sizeof buf);
		for (int i=0; i<r; i++){
			cin >> buf[i];
		}
		for (int i=0; i<r && !bad; i++){
			for (int j=0; j<c && !bad; j++){
				if (buf[i][j] == '#'){
					if (buf[i][j+1] != '#' || buf[i+1][j+1] != '#' || buf[i+1][j] != '#'){
						bad = true;
						break;
					} else {
						buf[i][j] = '/';
						buf[i][j+1] = '\\';
						buf[i+1][j+1] = '/';
						buf[i+1][j] = '\\';
					}
				}
			}
		}
		if (bad){
			cout << "Impossible\n";
		} else {
			for (int i=0; i<r; i++){
				cout << buf[i] << endl;
			}
		}
	}
	return 0;
}