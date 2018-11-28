#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
using namespace std;
#define GI ({int t; scanf("%d\n",&t); t;})
int L, D, N;
struct trie {
  bool end;
  struct trie* adj[26];
  trie() {
    for (int i = 0; i < 26; i++) {
      adj[i] = NULL;
    }
    end = false;
  }
};
typedef pair<struct trie*,int> ti;
queue<ti> Q;
//vector<struct trie*> T;
struct trie* root;
void build(string& str) {
  struct trie* save = root;
  for (int i = 0; i < L; i++) {
    int curr = str[i]-'a';
    if (!save->adj[curr]) {
      save->adj[curr] = new trie();
    }
    save = save->adj[curr];
  }
  save->end = true;
}

int query(vector<string>& V) {
  while (!Q.empty())
    Q.pop();
  Q.push(ti(root,0));
  for (int i = 0; i < V.size(); i++) {
    //cout << i << " " << V[i] << endl;
    while (!Q.empty()) {
      ti top = Q.front();
      if (top.second != i) {
	break;
      }
      //cout << top.second << endl;
      Q.pop();
      for (int j = 0; j < V[i].length(); j++) {
	int curr = V[i][j]-'a';
	if (top.first->adj[curr])
	  Q.push(ti(top.first->adj[curr],top.second+1));
      }
    }
  }
  int sz = 0;
  while (!Q.empty()) {
    Q.pop();
    sz++;
  }
  return sz;
}
main() {
  L = GI, D = GI, N = GI;
  string str;
  root = new trie();
  while (D--) {
    cin >> str;
    build(str);
  }
  for (int cas = 1; cas <= N; cas++) {
    printf("Case #%d: ",cas);
    cin >> str;
    vector<string> V;
    V.clear();
    bool flag = false;
    string tmp = "";
    for (int i = 0; i < str.size(); i++) {
      if (str[i] == '(') {
	flag = true;
	tmp = "";
	continue;
      }
      if (str[i] == ')') {
	V.push_back(tmp);
	flag = false;
	tmp = "";
	continue;
      }
      if (flag) {
	tmp += str[i];
	continue;
      }
      tmp = str[i];
      V.push_back(tmp);
    }
    /*cout << "size = " << V.size() << endl;
      for (int i = 0; i < V.size(); i++) {
      cout << V[i] << " ";
      }
      cout << endl;*/
    if (V.size() == L)
      printf("%d\n",query(V));
    else
      printf("0\n");
  }
  
}
