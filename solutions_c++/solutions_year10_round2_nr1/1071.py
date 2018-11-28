#include <cstring>
#include <iostream>
using namespace std;

struct Node {
	char *name;
	Node *kids;
	Node *next;

	Node(char *s) {
		name = strdup(s);
		kids = 0;
		next = 0;
	}
};

int
insert(Node *root, char *path)
{
	int nmk = 0;
	char *name = strtok(path + 1, "/");
	while (name != 0) {
		if (strcmp(root->name, name) == 0) {
			name = strtok(0, "/");
			if (name == 0)
				break;
		}
		Node *kp;
		for (kp = root->kids; kp != 0; kp = kp->next) {
			if (strcmp(kp->name, name) == 0) {
				root = kp;
				break;
			}
		}
		if (kp == 0) {
			Node *np = new Node(name);
			nmk++;
			np->next = root->kids;
			root->kids = np;
			root = np;
		}
	}
	return nmk;
}

int
main()
{
	int T, N, M;
	int mks = 0;
	char line[1024];

	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> N >> M; cin.getline(line, 1024);
		Node *root = new Node("ROOT");
		for (int n = 0; n < N; n++) {
			cin.getline(line, 1024);
			insert(root, line);
		}
		mks = 0;
		for (int m = 0; m < M; m++) {
			cin.getline(line, 1024);
			mks += insert(root, line);
		}
		cout << "Case #" << t << ": " << mks << endl;
	}
}



