#include <cstdio>
#include <vector>

using namespace std;

vector<pair<char, int> > order;

class Bot {
public:
	int pos;
	bool act;
	char type;
	vector<int> ord;

	Bot(char type) {
		this->type = type;
		pos = 1;
		act = false;
		ord.clear();
	}

	void move() {
		if (ord.empty())
			return;

		if (ord[0] > pos) {
			pos = pos + 1;
			act = true;
		}
		else if (ord[0] < pos) {
			pos = pos - 1;
			act = true;
		}
	}

	bool push() {
		if (act == true)
			return false;
		if (order[0].first != type || order[0].second != pos) {
			return false;
		}

		ord.erase(ord.begin());
		return true;
	}
};

int solve() {
	int z = 0;
	scanf("%d", &z);

	Bot bot1 = Bot('O');
	Bot bot2 = Bot('B');

	for(int i = 0; i < z; ++i) {
		char t[10];
		int pos;
		scanf("%s%d", t, &pos);

		order.push_back(make_pair(t[0], pos));
		if (t[0] == 'O')
			bot1.ord.push_back(pos);
		else
			bot2.ord.push_back(pos);
	}

	int res = 0;

	while(order.empty() == false) {
		bot1.act = bot2.act = false;
		res = res + 1;

		bot1.move();
		bot2.move();

		if (bot1.push() || bot2.push())
			order.erase(order.begin());
	}

	return res;
}

int main() {
	freopen("C:\\Users\\kiheon\\Downloads\\A-large.in", "r", stdin);
	freopen("c:\\users\\kiheon\\desktop\\output.txt", "w", stdout);
	int z;
	scanf("%d", &z);

	for (int i = 0; i < z; ++i) {
		printf("Case #%d: %d\n", i + 1, solve());
	}

	return 0;
}
