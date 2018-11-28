#include <iostream>

#define f(x,y) for (int x = 0; x < y; ++x)

#define L 16
#define D 5005
#define N 505

using namespace std;

int n, l, d;

char dict[D][L];

int main() {
	cin >> l >> d >> n;
	f(i,d) f(j,l) cin >> dict[i][j];
	
	f(i,n) {
		bool pos[l][26];
		f(j,l) f(k,26) pos[j][k] = false;
		
		f(j,l) {
			char c;
			cin >> c;
			if (c == '(') {
				cin >> c;
				while (c != ')') {
					pos[j][c-'a'] = true;
					cin >> c;
				}
			} else pos[j][c-'a'] = true;
		}
		
		int counter = 0;
		f(j,d) {
			bool good = true;
			f(k,l) if (!pos[k][dict[j][k]-'a']) good = false;
			if (good) ++counter;
		}
		
		cout << "Case #" << (i+1) << ": " << counter << endl;
	}
	
	return 0;
}

