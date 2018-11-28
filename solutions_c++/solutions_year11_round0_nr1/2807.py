#include <iostream>
#include <algorithm>
#include <queue>
#include <fstream>
using namespace std;

struct Order {
	char who;
	int pos;
	int time;
};

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("out.txt");

	int caseNo = 0;
	int cn;
	for (fin>>cn; cn>0; --cn) {
		int n;
		fin >> n;

		queue<Order> oran;
		queue<Order> blue;
		for (int i=0; i < n; ++i) {
			Order o;
			fin >> o.who >> o.pos;
			--o.pos;
			o.time = i;
			if (o.who=='O') oran.push(o);
			else blue.push(o);
		}

		int turn = 0;
		int po = 0;
		int pb = 0;
		for (int i=0; i < n; ++i) {
			while (true) {
				++turn;

				bool orangeTurn;
				Order o; if (!oran.empty()) o = oran.front();
				Order b; if (!blue.empty()) b = blue.front();

				if (oran.empty()) {
					orangeTurn = false;
				}
				else if (blue.empty()) {
					orangeTurn = true;
				}
				else {
					orangeTurn = (o.time < b.time);
				}

				bool pushed = false;
				if (!oran.empty()) {
					if (o.pos == po && orangeTurn) {
						oran.pop();
						pushed = true;
					}
					else {
						if (o.pos < po) --po;
						else if (o.pos > po) ++po;
					}
				}

				if (!blue.empty()) {
					if (b.pos == pb && !orangeTurn) {
						blue.pop();
						pushed = true;
					}
					else {
						if (b.pos < pb) --pb;
						else if (b.pos > pb) ++pb;
					}
				}

				if (pushed) break;
			}
		}

		fout << "Case #" << ++caseNo << ": " << turn << endl;
	}

	fin.close();
	fout.close();

	return 0;
}
