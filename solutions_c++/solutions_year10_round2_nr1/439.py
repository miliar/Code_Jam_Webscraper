#include <iostream>
#include <string>
#include <queue>
#include <vector>

using namespace std;

typedef struct node_ {
  string name;
  vector<struct node_*> children;
} node;



int insert(queue<string> path, node *n) {
  if(path.empty()) {
    return 0;
  }
  string s = path.front();
  path.pop();
  for(vector<node*>::iterator it = n->children.begin(); it != n->children.end(); it++) {
    if((*it)->name == s) {
      return insert(path, *it);
    }
  }
  node* nn = new node;
  nn -> name = s;
  n -> children.push_back(nn);

  return 1 + insert(path, nn); 
}

int main() {
  int T, N, M;

  cin >> T;
  for(int t = 1; t <= T; t++) {
    cin >> N >> M;
    char buf[256];
    char* p;
    node* root = new node;
    root -> name = "root";

    for(int i = 0; i < N; i++) {
      queue<string> path;
      cin.ignore();
      cin.getline(buf, 256, '\n');
      p = strtok(buf, "/");
      while(p != NULL) {
	path.push(p);
	p = strtok(NULL, "/");
      }
      insert(path, root);
    }

    cin.ignore();

    int count = 0;
    for(int i = 0; i < M; i++) {
      queue<string> path;
      cin.getline(buf, 256, '\n');
      p = strtok(buf, "/");
      while(p != NULL) {
	path.push(p);
	p = strtok(NULL, "/");
      }
      count += insert(path, root);
    }
    cout << "Case #" << t << ": " << count << endl;
  }

  return 0;
}
