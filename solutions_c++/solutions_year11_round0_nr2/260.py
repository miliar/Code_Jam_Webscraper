#include <iostream>
#include <string>
#include <fstream>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");
#define cin fin	
#define cout fout

char final[200];
int ptr, t, test = 1, n;
bool op[300][300];
char comb[300][300];
int pos[300];
string s;

int main() {
	for( cin >> t; t--;  ) {
		ptr = 0;
		memset( op, false, sizeof op );
		memset( comb, 0, sizeof comb );
		memset( pos, -1, sizeof pos );
		cin >> n;
		for( int i = 0; i < n; i++ ) {
			cin >> s;
			comb[s[0]][s[1]] = comb[s[1]][s[0]] = s[2];
		}
		cin >> n;
		for( int i = 0; i < n; i++ ) {
			cin >> s;
			op[s[0]][s[1]] = op[s[1]][s[0]] = true;
		}
		cin >> n >> s;
		for( int i = 0; i < n; i++ ) {
			if( ptr && comb[s[i]][final[ptr - 1]] ) {
				if( pos[final[ptr - 1]] == ptr - 1 )
					pos[final[ptr - 1]] = -1;
				final[ptr - 1] = comb[s[i]][final[ptr - 1]];
			} else {
				bool ops = false;
				for( char j = 'A'; j <= 'Z'; j++ ) {
					if( pos[j] != -1 && op[j][s[i]] )
						ops = true;
				}
				if( ops ) {
					ptr = 0;
					memset( pos, -1, sizeof pos );
				} else {
					if( pos[s[i]] == -1 )
						pos[s[i]] = ptr;
					final[ptr++] = s[i];
				}
			}
		}
		cout << "Case #" << test++ << ": [";
		for( int i = 0; i < ptr; i++ ) {
			if( i )	cout << ", ";
			cout << final[i];
		}
		cout << ']' << endl;
	}
	return 0;
}