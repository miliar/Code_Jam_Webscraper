#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
#include <map>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("A-large.out");

long long count = 0;

class node {
  public:
    map<string, node> children;
};

node root;

void parse(string cache) {
  node *cur = &root;
  char* cstr = new char[101];
  strcpy(cstr, cache.c_str());
  char* p = strtok(cstr, "/");
  while (p != NULL) {
    string conv = p;
    if (cur->children.count(conv) == 0) {
      node child;
      cur->children[conv] = child;
      ::count++;
    }
    cur = &(cur->children[conv]);
    p = strtok(NULL, "/");
  }
  delete[] cstr;
  delete[] p;
}

int main() {
  long long num;
  long long pre;
  long long post;
  fin >> num;
  for (int i = 0; i < num; i++) {
    ::count = 0;
    
    fin >> pre >> post;
    string cache;
    for (int j = 0; j < pre; j++) {
      fin >> cache;
      parse(cache);
    }
    ::count = 0;
    for (int j = 0; j < post; j++) {
      fin >> cache;
      parse(cache);
    }
    fout << "Case #" << i+1 << ": " << ::count << endl;
    root.children.erase(root.children.begin(), root.children.end());
  }
  return 0;
}
