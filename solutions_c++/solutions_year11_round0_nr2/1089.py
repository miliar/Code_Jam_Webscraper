#include <vector>
#include <cstdio>
using namespace std;

int trans[200][200];
int oppose[200][200];

int main() {
	int TESTS;
	scanf("%d", &TESTS);
	for(int test = 1; test<=TESTS; test++) {
		memset(trans, -1, sizeof(trans));
		memset(oppose, 0, sizeof(oppose));
		int C;
		scanf("%d", &C);
		for(int i = 0; i<C; i++) {
			char a, b, c;
			scanf(" %c%c%c ", &a, &b, &c);
			trans[a][b] = c;
			trans[b][a] = c;
		}
		int D;
		scanf("%d", &D);
		for(int i = 0; i<D; i++) {
			char a, b;
			scanf(" %c%c ", &a, &b);
			oppose[a][b] = oppose[b][a] = 1;
		}
		int N;
		scanf("%d", &N);
		vector<char> list;
		for(int i = 0; i<N; i++) {
			char c;
			scanf(" %c", &c);
			list.push_back(c);
			while(list.size() >= 2 && trans[list[list.size()-1]][list[list.size()-2]] != -1) {
				char newch = trans[list[list.size()-1]][list[list.size()-2]];
				list.pop_back();
				list.pop_back();
				list.push_back(newch);
			}
			for(int i = 0; i<list.size()-1; i++) {
				if(oppose[list[i]][list[list.size()-1]]) {
					list.clear();
					break;
				}
			}
		}
		printf("Case #%d: [", test);
		for(int i = 0; i<list.size(); i++) {
			printf("%c", list[i]);
			if(i != list.size() -1) {
				printf(", ");
			}
		}
		printf("]\n");
	}
	return 0;
}
