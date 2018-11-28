#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MAXN = 500;
struct Node {
  int st, ed;
  int mark, used;
};
int T, NA, NB, N;
Node train[MAXN];
int num[2];

void init();
void work();
int main()
{
  int test;
  scanf("%d", &test);
  for (int i = 0; i < test; ++i) {
    init();
    work();
    printf("Case #%d: %d %d\n", i+1, num[0], num[1]);
  }
  return 0;
}

bool cmp(Node i, Node j) {
  return i.st == j.st ? i.ed < j.ed : i.st < j.st;
}
void init() {
  scanf("%d%d%d", &T, &NA, &NB);
  for (int i = 0; i < NA; ++i) {
    char t[10];
    scanf("%s", t);
    train[i].st = (t[0]-'0')*10 + (t[1]-'0');
    train[i].st = train[i].st*60 + (t[3]-'0')*10 + (t[4]-'0');
    scanf("%s", t);
    train[i].ed = (t[0]-'0')*10 + (t[1]-'0');
    train[i].ed = train[i].ed*60 + (t[3]-'0')*10 + (t[4]-'0');
    train[i].mark = 0; train[i].used = 0;
  }
  for (int i = NA; i < NA+NB; ++i) {
    char t[10];
    scanf("%s", t);
    train[i].st = (t[0]-'0')*10 + (t[1]-'0');
    train[i].st = train[i].st*60 + (t[3]-'0')*10 + (t[4]-'0');
    scanf("%s", t);
    train[i].ed = (t[0]-'0')*10 + (t[1]-'0');
    train[i].ed = train[i].ed*60 + (t[3]-'0')*10 + (t[4]-'0');
    train[i].mark = 1; train[i].used = 0;
  }
  N = NA+NB;
  sort(train, train+N, cmp);

  //  for (int i = 0; i < N; ++i) printf("%d %d %d\n" , train[i].st, train[i].ed, train[i].mark);
}

void work() {
  num[0] = 0; num[1] = 0;

  for (int i = 0; i < N; ++i) if (train[i].used == 0) {
    ++num[train[i].mark];

    int now = i;
    for (int j = i+1; j < N; ++j) if (train[j].used == 0)
      if (1-train[now].mark == train[j].mark)
	if (train[now].ed+T <= train[j].st) {
	  now = j;
	  train[j].used = 1;
	}
  }
}
