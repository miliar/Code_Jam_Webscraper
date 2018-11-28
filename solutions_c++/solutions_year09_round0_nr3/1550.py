#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

struct node {
  int sum;
  int st;
  int sd;
  int pos;
  node *rb;
  node *s;
};

const char searched[] = "welcome to code jam";
const int seasize = sizeof(searched) - 1;

const int linesize = 500;

node nodes[seasize][linesize];

void build_nodes () {
  for (int i = 0; i < seasize; i++) {
    for (int j = 0; j < linesize; j++) {
      nodes[i][j].sum = -1;
      nodes[i][j].st = 0;
      nodes[i][j].sd = i;
      nodes[i][j].pos = j;
    }
  }
}
  

node * build_tree (const string &txt, int spos = 0, int sd = 0) {
  int txtlen = txt.size();
  node *ret = NULL;
  node *prev = NULL;
  if (sd >= seasize)
    return NULL;
  for (int i = spos; i < txtlen; i++) {
    if (nodes[sd][i].st == 1)
      return  &nodes [sd][i];
    if (txt[i] == searched[sd]) {
      if (ret == NULL)
	ret = &nodes [sd][i];
      if (prev != NULL)
	prev->rb = &nodes [sd][i];
      nodes [sd][i].s = build_tree (txt,i+1,sd+1);
      nodes [sd][i].st = 1;
      prev = &nodes [sd][i];
    }
  }
  if (prev != NULL)
    prev->rb = NULL;
  if (sd == seasize - 1) {
    int s = 0;
    node *nxt = ret;
    while (nxt != NULL) {
      s++;
      nxt = nxt->rb;
    }
    nxt = ret;
    while (nxt != NULL) {
      nxt->sum = s;
      s--;
      nxt = nxt->rb;
    }	
  }
  return ret;
}

int get_sum (node *n) {
  if (n == NULL)
    return 0;

  if (n->sum != -1)
    return n->sum;
  
  n->sum = (get_sum(n->s) + get_sum(n->rb)) % 10000;
  return n->sum;
}


int main () {
  int ntests;
  string line;
  cin >> ntests;
  node *n;
  getline(cin,line);
  for (int c = 1; c <= ntests; c++) {
    build_nodes ();
    getline(cin,line);
    n = build_tree (line);
    cout << "Case #"<< c <<": " << setfill('0') << setw(4) << get_sum(n) << "\n";
  }
}
