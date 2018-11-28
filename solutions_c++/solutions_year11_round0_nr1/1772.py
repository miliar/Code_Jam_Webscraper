#include <iostream>

using namespace std;

int t;
int time1, time2, curtime;
int pos1, pos2;
char c;
int b, n;

int abs(int x){
	if (x < 0) return -x;
	return x;
}

int find(int time1, int pos, int curtime){
	int need = abs(pos - b);
	if (curtime - time1 >= need){
		return curtime + 1;
	}
	else{
		return curtime + (need - (curtime - time1) + 1);
	}
}

int main(){
	cin >> t;
	for (int _i = 0; _i < t; ++_i){
		cin >> n;
		time1 = time2 = curtime = 0;
		pos1 = pos2 = 1;
		for (int i = 0; i < n; ++i){
			cin >> c >> b;
			if (c == 'O'){
				time1 = find(time1, pos1, curtime);
				curtime = time1;
				pos1 = b;
			}
			if (c == 'B'){
				time2 = find(time2, pos2, curtime);
				curtime = time2;
				pos2 = b;
			}
		}
		cout << "Case #" << _i + 1<<  ": " << curtime << endl;
	}
	return 0;
}