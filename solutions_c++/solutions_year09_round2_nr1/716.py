#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("A-large.out");

struct node;

typedef struct node {
  float weight;
  char feature[20];
  
  struct node *parent;
	struct node *left;
	struct node *right;
} node_t;

node_t root;
node_t *parent;
node_t *cur = &root;

int read_state = 0;

void process_line(char *line) {
  int len = strlen(line);
  int i = 0;
  int during_parens = 1;
  while ((line[i] == ' ' || line[i] == '\n') && i < len) i++;
  if (i == len) return;
  switch (read_state) {
  case 0:
    if (line[i] == '(') {
      read_state = 1;
      i++;
      while ((line[i] == ' ' || line[i] == '\n') && i < len) i++;
      if (i == len) return;
    }
  case 1:
    if (line[i] == '1' || line[i] == '0') {
      sscanf(&(line[i]), "%f", &(cur->weight));
      read_state = 2;
      i++;
      while ((line[i] >= '0' && line[i] <= '9' || line[i] == '.') && i < len) i++;
      while ((line[i] == ' ' || line[i] == '\n') && i < len) i++;
      if (i == len) return;
    }
  case 2:
    if (line[i] == ')') {
      cur->feature[0] = 0;
      goto skipper;
    }
    sscanf(&(line[i]), "%s", &(cur->feature));
    read_state = 3;
    i++;
    while ((line[i] >= 'a' && line[i] <= 'z') && i < len) i++;
    while ((line[i] == ' ' || line[i] == '\n') && i < len) i++;
    if (i == len) return;
  case 3:
    /* left child */
    cur->left = new node_t;
    cur->left->parent = cur;
    cur = cur->left;
    if (line[i] == '(') {
      read_state = 0;
      process_line(&(line[i]));
    }
    if (read_state != 4) return;
    during_parens = 1;
    while (during_parens > 0 && i < len) {
      i++;
      if (line[i] == '(') {
        during_parens++;
      } else if (line[i] == ')') {
        during_parens--;
      }
    }
    i++;
    while ((line[i] == ' ' || line[i] == '\n') && i < len) i++;
    if (i == len) return;
  case 4:
    /* right child */
    cur->right = new node_t;
    cur->right->parent = cur;
    cur = cur->right;
    if (line[i] == '(') {
      read_state = 0;
      process_line(&(line[i]));
    }
    if (read_state != 5) return;
    during_parens = 1;
    while (during_parens > 0 && i < len) {
      i++;
      if (line[i] == '(') {
        during_parens++;
      } else if (line[i] == ')') {
        during_parens--;
      }
    }
    i++;
    while ((line[i] == ' ' || line[i] == '\n') && i < len) i++;
    if (i == len) return;
  case 5:
    if (line[i] == ')') {
      skipper:
      if (cur == &root) {
        return;
      }
      if (cur == cur->parent->left) {
        read_state = 4;
      } else if (cur == cur->parent->right) {
        read_state = 5;
      }
      cur = cur->parent;
      return;
    }
  }
}

void recursive_destroy (node_t *root) {
  if (root->feature[0]) {
    recursive_destroy(root->left);
    delete root->left;
    recursive_destroy(root->right);
    delete root->right;
    root->parent = 0;
  } else {
    root->parent = 0;
  }
  strcpy(root->feature, "");
  root->weight = 0.0f;
}

int main() {
    int cases, lines, animals;
    char line[1024];
    fin >> cases;
    fin.getline(line, 1024);
    for (int i=0;i<cases;i++) {
      cur = &root;
      read_state = 0;
      fin >> lines;
      fin.getline(line, 1024);
      for (int j=0; j<lines; j++) {    
        fin.getline(line, 1024);
        process_line(line);
      }
      fin >> animals;
      fout << "Case #" << i+1 << ":\n";
      for (int j=0; j<animals; j++) {
        fin.getline(line, 1024);
        string name;
        int traits;
        fin >> name >> traits;
        string traitnames[traits];
        for (int k=0; k<traits; k++) {
          fin >> traitnames[k];
        }
        float prob = 1.0;
        node_t *trav = &root;
        while (trav->feature[0]) {
          prob *= trav->weight;
          bool traitcheck = false;
          for (int k=0; k<traits; k++) {
            if (!strcmp(traitnames[k].c_str(), trav->feature)) {
              traitcheck = true;
            }
          }
          if (traitcheck) trav = trav->left;
          else trav = trav->right;
        }
        prob *= trav->weight;
        fout << fixed;
        fout << setprecision(7) << prob << endl;
      }
      recursive_destroy(&root);
    }
    return 0;
}

