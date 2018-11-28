									/* in the name of Allah */
#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("A-small.in");
ofstream fout("A-small.out");

#define cin fin
#define cout fout

int main(){
	int T, n, test = 0;
	int p;
	char ch;
	for(cin >> T; T--; ){
		int bp = 1, bt = 0;
		int op = 1, ot = 0;
		int t = 0;
		cin >> n;
		for(int i = 0; i < n; i++){
			cin >> ch >> p;
			if(ch == 'O'){
				t = max(t, ot + abs(op - p)) + 1;
				op = p;
				ot = t;
			}
			else{
				t = max(t, bt + abs(bp - p)) + 1;
				bp = p;
				bt = t;
			}
		}
		cout << "Case #" << ++test << ": " << t << endl;
	}
	return 0;
}
