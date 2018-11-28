#include <iostream>
using namespace std;

struct node {
	node* children[11];
	int cost;
};

node pool[2000000];
string dict[10000];
node* which[10000];

void recurse(node* n, int ccost, bool newletter) {
	n->cost = ccost;
	bool anyExist = false;
	for (int i = 1; i <= 10; i++) if (n->children[i] != NULL) {
		anyExist = true;
		recurse(n->children[i], ccost, false);
	}
	if (newletter && anyExist) ccost++;
	if (n->children[0] != NULL) recurse(n->children[0], ccost, true);
}

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int N, M;
		cin >> N >> M;
		for (int i = 0; i < N; i++)
			cin >> dict[i];
		
		cout << "Case #" << t+1 << ':';
		for (int m = 0; m < M; m++) {
			char alph[27];
			cin >> alph;
			
			node* tries[10];
			int used = 0;
			for (int i = 0; i < 10; i++) {
				tries[i] = &pool[used++];
				for (int j = 0; j <= 10; j++) tries[i]->children[j] = NULL;
			}
			
			for (int i = 0; i < N; i++) {
				node* cur = tries[dict[i].size()-1];
				for (int j = 0; j < 26; j++) {
					for (int k = 0; k < dict[i].size(); k++) {
						if (dict[i][k] == alph[j]) {
							if (!cur->children[k+1]) {
								cur->children[k+1] = &pool[used++];
								for (int l = 0; l <= 10; l++) cur->children[k+1]->children[l] = NULL;
							}
							cur = cur->children[k+1];
						}
					}
					
					if (!cur->children[0]) {
						cur->children[0] = &pool[used++];
						for (int l = 0; l <= 10; l++) cur->children[0]->children[l] = NULL;
					}
					cur = cur->children[0];
				}
				
				which[i] = cur;
			}
			
			for (int i = 0; i < 10; i++) recurse(tries[i], 0, true);
			int best = 0;
			for (int i = 1; i < N; i++) if (which[i]->cost > which[best]->cost) best = i;
			cout << ' ' << dict[best];
		}
		cout << '\n';
	}
	
	return 0;
}
