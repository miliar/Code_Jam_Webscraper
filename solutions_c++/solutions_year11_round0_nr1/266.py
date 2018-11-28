#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");
#define cin fin
#define cout fout

int t, n, test = 1;
int id[200];
char who[200];

int main() {
	for( cin >> t; t--; ) {
		cin >> n;
		int pos[2] = {1, 1};
		for( int i = 0; i < n; i++ ) 
			cin >> who[i] >> id[i];
		int res = 0;
		for( int i = 0; i < n; i++ ) {
			
			int trg[2] = {-1, -1};
			for( int j = i; j < n; j++ ) {
				if( who[j] == 'O' && trg[0] == -1 )
					trg[0] = id[j];
				if( who[j] == 'B' && trg[1] == -1  )
					trg[1] = id[j];
			}
		
			int mov = (who[i] == 'O' ? 0 : 1); 
			int tmp = abs( pos[mov] - trg[mov] ) + 1;
			pos[mov] = trg[mov];
			mov = 1 - mov;
			if( trg[mov] != -1 ) {
				if( tmp >= abs( pos[mov] - trg[mov] ) )
					pos[mov] = trg[mov];
				else if( trg[mov] > pos[mov] )
					pos[mov] += tmp;
				else
					pos[mov] -= tmp;
			}
			res += tmp;
		}
		cout <<	"Case #" << test++ << ": " << res << endl;
	}
	return 0;
}