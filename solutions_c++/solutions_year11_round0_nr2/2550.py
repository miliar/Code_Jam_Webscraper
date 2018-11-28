#include <iostream>
#include <iomanip> 
#include <string> 
#include <algorithm> 
#include <vector> 
#include <set> 
#include <map> 
#include <math.h> 
#include <cstdlib>
#include <queue>
using namespace std;

char non[8][8]; //q - 0, w - 1, e- 2, r- 3, a- 4, s- 5, d-6, f-7;
bool del[8][8];
int used[8]; 
vector<char> magic;
int make(char a) {
	if (a == 'Q') {
		return 0;
	}
	if (a == 'W') {
		return 1;
	}
	if (a == 'E') {
		return 2;
	}
	if (a == 'R') {
		return 3;
	}
	if (a == 'A') {
		return 4;
	}
	if (a == 'S') {
		return 5;
	}
	if (a == 'D') {
		return 6;
	}	
	if (a == 'F') {
		return 7;
	}
}

int main(void) {
	//	freopen("/Users/admin/Desktop/[Contests]/informatics/Cpl/be/a.in","r",stdin);
	//	freopen("/Users/admin/Desktop/[Contests]/informatics/Cpl/be/a.out","w",stdout);
	int n, t, f, c;
	char x, y, z;
	cin >> n;
	cout << n << endl;
/*	for(int i = 0; i < n; i++) {
		memset(used, 0, 8);
		for (int j = 0; j < 8; j++) {
			for (int k = 0; k < 8; k++) {
				non[j][k] = '0';
				del[j][k] = 0;
			}
		}
		
		scanf("d", &c);
		for (int j = 0; j < c; j++) {
			cin >> x >> y >> z;
			non[make(x), make(y)] = z;
			non[make(y), make(x)] = z;
		}
		
		scanf("%d", &c);
		for (int j = 0; i < c; j++) {
			cin >> x >> y;
			del[make(x), make(y)] = true;
			del[make(y), make(x)] = true;
		}
		
		scanf("%d", &c);
		cout << c<< endl; 
		for (int j = 0; j < c; j++) {
			cin >> x;
			if (magic.size() > 0) {
				if (non[make(x), make(magic.size() - 1)] != '0') {
					used[make(magic.size() - 1)]--;
					magic[size() - 1] = non[make(x), make(magic.size() - 1)];
				} else {
					magic.push_back(x);
					cout << x;
					used[make(x)]++;
					for (int k = 0; k < 8; k++) {
						if (del[k][make(x)] && used[k] > 0) {
							magic.clear();
							memset(used, 0, 8);
							break;
						}	
					}
				}
			} else {
				magic.push_back(x);
			}
		}
		cout << "Case #"<< i + 1<< ": ";
		for (int k = 0; k < magic.size; k++) {
			cout << magic[k] << " ";
		}
		cout<< endl;
	}
 */
	return 0;
}