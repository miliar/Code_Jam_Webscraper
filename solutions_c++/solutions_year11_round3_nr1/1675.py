#include <iostream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define repd(i,n,m) for(int i=n;i<(int)(m);i++)
#define repvi(v,i) for(vector<int>::iterator i = v.begin(); i < v.end();i++)
#define repvs(v,i) for(vector<string>::iterator i = v.begin(); i < v.end();i++)
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )

int main() {
	freopen("a.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int cases;
	cin >> cases;
	repd(nn, 1, cases+1) {
		cout << "Case #" << nn << ": " << endl;
		int rows, cols;
		cin >> rows >> cols;
		char floor[rows][cols];

		rep(i, rows) {
			rep(j, cols) {
				cin >> floor[i][j];
			}
		}

		rep(i, rows) {
			rep(j, cols) {
				if ( floor[i][j] == '#') {
					floor[i][j] = '/';
					if ((j+1) < cols && floor[i][j+1] == '#') {
						floor[i][j+1] = '\\';
						if ((i+1) < rows && floor[i+1][j] == '#') {
							floor[i+1][j] = '\\';
							if (floor[i+1][j+1] == '#') {
								floor[i+1][j+1] = '/';

							} else 
							goto fail;	

						} else 
							goto fail;	

					} else 
						goto fail;	
				}
			}
		
		}
			rep(i, rows) {
				rep(j, cols) {
					cout << floor[i][j];
				}
				cout << endl;
			}
			continue;
		fail:
			cout	<< "Impossible" << endl;
	}	
	
	return 0;
}
