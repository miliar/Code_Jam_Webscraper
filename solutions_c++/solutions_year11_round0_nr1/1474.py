#include <iostream>
#include <stdlib.h>
#include <vector>
using namespace std;

char opp(char v) {
	if (v=='O') return 'B'; else return 'O';
}
int pos[2] = {1,1};
int ptr[2] = {0,0};
int cmd_nums[100];
char cmd_names[100];

int main() {
	int testcases;
	cin >> testcases;
	for (int tc=0;tc<testcases;tc++) {
		int numbuttons;
		cin >> numbuttons;
		for (int i=0;i<numbuttons;i++) {
			char c;
			cin >> c >> cmd_nums[i];
			if (c=='O') cmd_names[i] = 0; else cmd_names[i] = 1;
		}
		pos[0] = 1;pos[1] = 1;
		ptr[0] = 0;ptr[1] = 0;
		int t = 0;
		for (int i=0;i<numbuttons;i++) {
			char name = cmd_names[i];
			int delta = abs( cmd_nums[i]-pos[name]);
			pos[name] = cmd_nums[i];
			ptr[name] = max(t+1,ptr[name]+delta+1);
			t = ptr[name];
			//cout << "#" << tc << " pos=[" << pos[0] << "," << pos[1] << "]; ptr=[" << ptr[0] << "," << ptr[1] << "]; t=" << t << endl;
		}
		cout << "Case #" << (tc+1) << ": " << t << "\n";
	}
}