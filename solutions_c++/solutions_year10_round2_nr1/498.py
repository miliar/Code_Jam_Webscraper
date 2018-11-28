#include <iostream>
#include <string>
#include <vector>

#define SIZE 205

using namespace std;

int n,m;

struct node {
  string name;
  vector<node*> next;
};

int add(node *r, string str) {
  int first = 1;
  int cnt = 0;
 
  for (size_t i = 1; i<str.length(); i++) {
    if (str[i] == '/') {
      bool found = false;

      string name = str.substr(first, i-first);
      
      for (size_t j = 0; j < r->next.size(); j++) {
	if (r->next[j]->name == name) {
	  found = true;
	  r = r->next[j];
	  break;
	}
      }
      
      if (!found) {
	node *novo = new node();
	novo->name = name;
	r->next.push_back(novo);
	r = novo;
	cnt++;
      }
      first = i+1;
    }
  }
  
  int i = str.length();

  //cout << first << " " << i << " " << r->next.size() << endl;
  
  bool found = false;
  
  string name = str.substr(first, i-first);

  for (size_t j = 0; j < r->next.size(); j++) {
    if (r->next[j]->name == name) {
      //cout << r->next[j]->name << " " << name << " aqui" << endl;
      found = true;
      r = r->next[j];
      break;
    }
  }
  if (!found) {
    node *novo = new node();
    novo->name = name;
    r->next.push_back(novo);
    r = novo;
    cnt++;
  }  
  //cout << cnt << endl;
  return cnt;
}

int main() {
  int t;
  string str;

  cin >> t;
  for (int tt = 1; tt<=t; tt++) {
    cin >> n >> m;

    node *root = new node();
    for (int i = 0;i<n;i++) {
      cin >> str;
      add(root, str);
    }
    //cout << "---" << endl;
    int cnt = 0;    
    for (int i = 0;i<m;i++) {
      cin >> str;
      cnt += add(root, str);
    }
    cout << "Case #" << tt << ": " << cnt << endl;
  }
  return 0;
}
