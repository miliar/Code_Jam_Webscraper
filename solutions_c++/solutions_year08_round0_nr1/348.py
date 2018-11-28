#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

map<string , int> eng;
int query[1001];
bool seen[101];

int main() {
	int N, S, Q;
	string str;
	char se[200], Nstr[100], Sstr[100], Qstr[100];
	cin.getline(Nstr, sizeof Nstr);
	N = atoi(Nstr);
	int nn = 0;
	while(nn < N) {
		eng.clear();
		cin.getline(Sstr, sizeof Sstr);
		S = atoi(Sstr);
		for(int i = 0; i < S; i++) {
			cin.getline(se, sizeof se);
			str = se;
			eng[str] = i;
		}
		cin.getline(Qstr, sizeof Qstr);
		Q = atoi(Qstr);
		for(int i = 0; i < Q; i++) {
			cin.getline(se, sizeof se);
			str = se;
			query[i] = eng[str];
		}
		int ans = 0;
		for(int i = 0; i < Q;) {
			memset(seen, 0, sizeof seen);
			int seentot = 0;
			do{
				if(!seen[query[i]]) {
					seen[query[i]] = true;
					seentot++;
					if (seentot == S) break;
				}
				i++;
			} while(i < Q);
			if(i < Q)
				ans ++;
		}
		nn++;
		cout << "Case #" << nn << ": " << ans << endl;
	}
	return 0;
}
