#include <iostream>
#include <cstdio>
#include <cstring>

int L, D, N;

struct AlphabTree {
  AlphabTree *children[256];
  bool is_word;

  AlphabTree() {
    memset(children, 0, sizeof(AlphabTree*)*256);
    is_word = false;
  }
};

AlphabTree tree;

void rec_find(AlphabTree *cur_node, const char *s, unsigned int *n) {
  char c = *s;

  if(!c && cur_node->is_word)
    (*n)++;
  
  else if(c == '(') {
    char *next = strchr(s, ')') + 1;
    s++;

    while((*s) != ')') {
      if(cur_node->children[*s])
	rec_find(cur_node->children[*s], next, n);
     
      s++;
    }
  }

  else if(c && cur_node->children[c])
    rec_find(cur_node->children[c], s+1, n);
}

void rec_build(char *p, int n, AlphabTree *node) {
  if(n >= L) node->is_word = true;
  
  else {
    if(!node->children[p[n]]) node->children[p[n]] = new AlphabTree();
    rec_build(p, n+1, node->children[p[n]]);
  }
}

void buildtree() {
  for(int i=0; i<D; i++) {
    char line[20];
    fgets(line, 20, stdin);
    rec_build(line, 0, &tree);
  }
}

int main() {
  char s[512];
  fgets(s, 512, stdin);
  sscanf(s, "%d %d %d", &L, &D, &N);
  buildtree();
  
  std::string line;
  int i = 1;

  while(std::cin >> line) {
    unsigned int n = 0;
    rec_find(&tree, line.c_str(), &n);
    printf("Case #%d: %d\n", i++, n);
  }
}
