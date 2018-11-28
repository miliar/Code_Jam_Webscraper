#include<iostream>
using namespace std;
void run();
int main () {
    freopen("data.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int credits;
	cin >> credits;
	//cout << credits << endl;
	for (int i = 0; i < credits; ++ i) {
		cout <<"Case #"<<i+1<<": ";
		run();
	}
	return 0;
}

void run() {
	int N;
	cin >> N;
	int change[200];
	int cur = -1;
	int other = -1;
	int botton[2][200];
	int top[2] = {0,0};
	int pos[2] = {1,1};
	int color = -1;
	char c;
	int b;
	for (int i = 0; i < N; ++ i) {
		cin >> c >> b;
		if (c == 'O') color = 0;
		else color = 1;
		change[i] = color;
		botton[color][top[color]] = b;
		top[color] ++;
	}
	//////////
	/*cout << "##################"<<endl;
	for (int i = 0; i < top[0]; ++ i)
		cout << botton[0][i] <<' ';
	cout << endl;
	for (int i = 0; i < top[1]; ++ i)
		cout << botton[1][i] <<' ';
	cout << endl;
	for (int i = 0; i < N; ++ i)
		cout << change[i] << ' ';
	cout << endl;
	cout << "##################"<<endl;*/
	///////
	int timer = 0;
	int step = 0;
	int task[2] = {0,0};
	while (step != N) {
		++ timer;
		cur = change[step];
		other = 1 - cur;
		while (true) {
			if (pos[cur] == botton[cur][task[cur]]) {
				++ task[cur]; 
				++ step;
				break;
			}
			if (pos[cur] < botton[cur][task[cur]]) {
				++ pos[cur];
				break;
			}
			if (pos[cur] > botton[cur][task[cur]]) {
				-- pos[cur];
				break;
			}
		}
		while(true) {
			if (pos[other] == botton[other][task[other]]) {
				break;
			}
			if (pos[other] < botton[other][task[other]]) {
				++ pos[other];
				break;
			}
			if (pos[other] > botton[other][task[other]]) {
				-- pos[other];
				break;
			}
		}		
	}
	cout <<timer<<endl;		
}
