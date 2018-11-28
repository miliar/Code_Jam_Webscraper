#include <iostream>

using namespace std;

int t;
int n, c, d;
char com[36][3];
char opp[28][2];
char q[105];
int a[255];
int l;


bool find(char w){
	if (l == 0) return false;
	for (int i = 0; i < c; ++i){
		if (q[l - 1] == com[i][0] && w == com[i][1]){
			--a[q[l - 1]];
			q[l - 1] = com[i][2];
			return true;
		}
		if (q[l - 1] == com[i][1] && w == com[i][0]){
			--a[q[l - 1]];
			q[l - 1] = com[i][2];
			return true;
		}
	}
	return false;
}

bool delet(char w){
	for (int i = 0; i < d; ++i){
		if (a[opp[i][0]] && w == opp[i][1]){
			for (int i = 0; i < 255; ++i) a[i] = 0;
			l = 0;
			return true;
		}
		if (a[opp[i][1]] && w == opp[i][0]){
			for (int i = 0; i < 255; ++i) a[i] = 0;
			l = 0;
			return true;
		}
	}
	return false;
}

int main(){
	cin >> t;
	for (int _i = 0; _i < t; ++_i){
		for (int i = 0; i < 255; ++i) a[i] = 0;
		l = 0;

		cin >> c;
		for (int i = 0; i < c; ++i) cin >> com[i][0] >> com[i][1] >> com[i][2];
		cin >> d;
		for (int i = 0; i < d; ++i) cin >> opp[i][0] >> opp[i][1];
		cin >> n;
		for (int i = 0; i < n; ++i){
			char w;
			cin >> w;
			if (!find(w)){
				if (!delet(w)){
					q[l] = w;
					++a[w];
					++l;
				}
			}
		}
		cout << "Case #" << _i + 1 << ": [";
		for (int i = 0; i < l - 1; ++i) cout << q[i] << ", ";
		if (l) cout << q[l - 1];
		cout << "]\n";
	}
	return 0;
}