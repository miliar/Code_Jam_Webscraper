#include <iostream>
#include <map>
#include <cstring>
#include <cstdio>
#include <set>
#include <vector>
#include <string>

using namespace std;

int nodes;

#define MAX 2000

int graph[MAX][2];
int tipo[MAX];
double val[MAX];
char nome[MAX][100];

int nnode() {
  return nodes++;
}

char s[MAX];

int le() {
  double d;
  int id = nnode();
  scanf(" %*c");
  scanf(" %lf",&d);
  scanf("%[^\n]s",s);
  val[id] = d;
  if (s[strlen(s)-1] == ')') {
    tipo[id] = 0;
    val[id] = d;
  }
  else {
    tipo[id] = 1;
    val[id] = d;
    sscanf(s," %[^ )]s",nome[id]);
    graph[id][0] = le();
    graph[id][1] = le();
    scanf(" )");
  }
  return id;
}

set<string> m;

double calc(int id) {
  if (tipo[id] == 0) return val[id];
  if (m.find(nome[id]) != m.end()) {
    return val[id]*calc(graph[id][0]);
  }
  return val[id]*calc(graph[id][1]);
}

int main() {
  int k;
  scanf("%d",&k);
  int test = 0;
  int nt, na, n; 
  while (k--) {
    nodes = 0;
    test++;
    printf("Case #%d:\n",test);
    scanf("%d",&nt);
    le();
    scanf("%d",&na);
    for (int i = 0; i < na; i++) {
      m.clear();
      scanf("%*s");
      scanf("%d",&n);
      for (int j = 0; j < n; j++) {
	scanf("%s",s);
	m.insert(s);
      }
      printf("%.7lf\n",calc(0));
    }
  }
  return 0;
}
