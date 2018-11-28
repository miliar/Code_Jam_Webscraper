#include <cstdio>
#include <set>
#include <vector>
#include <stack>

using namespace std;

typedef pair<int, int> par;

stack<int> list;
vector<par> combinations[26];
vector<int> opositions[26];
int count[26];

int removeTop() {
	if (list.empty()) {
		return -1;
	}
	
	int top = list.top();
	list.pop();
	count[top]--;
	
	return top;
}

void clear() {
	while (!list.empty()) {
		removeTop();
	}
}

void insertStraight(int element) {
	if (element > -1) {
		list.push(element);
		count[element]++;
	}
}

void insertElement(int element) {
	int top = removeTop();
	
	for (int i = 0; top > -1 && i < combinations[element].size(); i++) {
		par p = combinations[element][i];
		
		if (p.first == top) {
			insertElement(p.second);
			return;
		}
	}
	
	insertStraight(top);
	
	for (int i = 0; i < opositions[element].size(); i++) {
		int o = opositions[element][i];
		
		if (count[o] > 0) {
			clear();
			return;
		}
	}
	
	insertStraight(element);
}

int main() {
	int t;
	scanf("%d", &t);
	
	for (int test = 1; test <= t; test++) {
		clear();
		
		int c, d, n;
		
		for (int i = 0; i < 26; i++) {
			combinations[i].clear();
			opositions[i].clear();
			count[i] = 0;
		}
		
		scanf("%d", &c);
		
		for (int i = 0; i < c; i++) {
			char comb[4];
			scanf("%s", comb);
			
			int a = comb[0] - 'A';
			int b = comb[1] - 'A';
			int novo = comb[2] - 'A';
			
			combinations[a].push_back(make_pair(b, novo));
			combinations[b].push_back(make_pair(a, novo));
		}
		
		scanf("%d", &d);
		
		for (int i = 0; i < d; i++) {
			char opos[3];
			
			scanf("%s", opos);
			
			int a = opos[0] - 'A';
			int b = opos[1] - 'A';
			
			opositions[a].push_back(b);
			opositions[b].push_back(a);
		}
		
		scanf("%d", &n);
		
		char input[101];
		
		scanf("%s", input);
		
		for (int i = 0; i < n; i++) {
			insertElement(input[i] - 'A');
		}
		
		stack<int> aux;
		
		while (!list.empty()) {
			aux.push(list.top());
			list.pop();
		}
		
		printf("Case #%d: [", test);
		if (!aux.empty()) {
			printf("%c", aux.top() + 'A');
			aux.pop();
		}
		
		while (!aux.empty()) {
			printf(", %c", aux.top() + 'A');
			aux.pop();
		}
		printf("]\n");
	}
	return 0;
}

