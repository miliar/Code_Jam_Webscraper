#include <cstdio>
#include <queue>
#include <cmath>

using namespace std;

int main()
{
	int N, ccN;
	scanf("%d", &ccN);
	for(int cc=0;cc < ccN;cc++) {
		queue<int> a, b;
		queue<char> order;
		scanf("%d", &N);
		for(int i=0;i<N;i++) {
			char name;
			int btn;
			scanf(" %c %d ", &name, &btn);
			if(name == 'O')
				a.push(btn);
			else
				b.push(btn);
			order.push(name);
		}
		int posA = 1, posB = 1;
		int time = 0;
		while(!a.empty() || !b.empty()) {
			int push = 0;
			if(!a.empty()) {
				if(order.front() == 'O' && posA == a.front()) {
					order.pop();
					a.pop();
					push = 1;
				} else {
					if(posA != a.front())
						posA += posA > a.front() ? -1 : 1;
				}
			}
			if(!b.empty()) {
				if(push == 0 && order.front() == 'B' && posB == b.front()) {
					order.pop();
					b.pop();
				} else {
					if(posB != b.front())
						posB += posB > b.front() ? -1 : 1;
				}
			}
			time++;
		}
		printf("Case #%d: %d\n", cc+1, time);
	}
	return 0;
}
