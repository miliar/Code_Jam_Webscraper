#include <cstdio>
#include <vector>

using namespace std;

struct Pair {
	int x, n;
	Pair() {}
	Pair(int x, int n): x(x), n(n) {}
};

vector<Pair> button[2];
Pair bot[2];

bool tryPush(int botNum, int buttonNum) {
	Pair &currBot = bot[botNum];
	if(currBot.n >= button[botNum].size() ) return false;
	Pair &currButton = button[botNum][currBot.n];

	if(buttonNum == currButton.n &&  currBot.x == currButton.x) {
		//printf("%d: Push button %d\n", botNum, buttonNum);
		currBot.n++;
		return true;
	}
	return false;
}

void move(int botNum) {
	Pair &currBot = bot[botNum];
	if(currBot.n >= button[botNum].size() ) return;
	Pair &currButton = button[botNum][currBot.n];

	int d = currButton.x - currBot.x;
	if(d > 0) d = 1;
	else if(d < 0) d = -1;

	currBot.x+=d;	
	//printf("%d: Move to button %d\n", botNum, currBot.x);

}

void solve(int caseNumber) {
	int n;
	scanf("%d\n", &n);
	for(int i = 0; i < n; i++) {
		char c;	int x;
		scanf("%c %d ", &c, &x);

		int j = (c=='O')?1:0;
		button[j].push_back(Pair(x, i));
	}

	bot[0].x = bot[1].x = 1;
	bot[0].n = bot[1].n = 0;

	int t = 0;

	for(int i = 0; i < n; i++) {
		while(true) {
			t++;
			//printf("t = %d\n", t);
			if(tryPush(0, i)) {
				move(1);
				break;
			}
			else if(tryPush(1, i)) {
				move(0);
				break;
			}
			else {
				move(0); move(1);
			}
		}
	}
	button[0].clear(); button[1].clear();
	printf("Case #%d: %d\n", caseNumber, t);
	

}


int main() {

	//freopen("in.txt", "r", stdin);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) solve(i);

}