
#include <set>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;
template <typename T>
static inline void checkMin(T& dst, T src) { if (dst > src) dst = src; }

template <typename T>
static inline void checkMax(T& dst, T src) { if (dst < src) dst = src; }



typedef struct dirtree{
  char name[101];
  int count;
  struct dirtree* children[200];
}DirTree;

static void divideName(char* name, char** res, int& count)
{
  ++name;
  count = 0;
  char * end;
  while (*name != '\0') {
    end = strchr(name, '/');
    if (end == NULL) {
       res[count++] = name;
       break;
    }
    *end = '\0';
    res[count++] = name;
    name = end + 1;
  }
}

static void createTree(DirTree** tree)
{
  *tree = (DirTree*) malloc(sizeof(DirTree));
  (*tree)->count = 0;
}

static int doInsertTree(DirTree* root, char** names, int begin, int end)
{
  int count = 0;
  DirTree* last = root;
  while (begin != end) {  
    DirTree* next = (DirTree*) malloc(sizeof(DirTree)); 
    next->count = 0;
    strcpy(next->name, names[begin++]);
    last->children[last->count++] = next;
    last = next;
    ++count;
  }
  return count;
}

static int insertTree(DirTree* root, char** dir, int len, int level)
{
  int count = 0;
  if (level == len) return 0;
  for (int i = 0; i < root->count; i++)
    if (strcmp(root->children[i]->name, dir[level]) == 0) {
      return insertTree(root->children[i], dir, len, level + 1);
    }  
  return doInsertTree(root, dir, level, len);
}


int main()
{

  int T;
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  scanf("%d", &T);
  
  for (int i = 1; i <= T; i++) {
    int n, m;
    char dire[101]; 
    DirTree* root;
    scanf("%d%d", &n, &m);
    createTree(&root);
    for (int j = 0; j < n; j++) {
      char *parsed[100];
      int len;
      scanf("%s", dire);
      divideName(dire, parsed, len);
      insertTree(root, parsed, len, 0);
    }

    int count = 0;
    for (int j = 0; j < m; j++) {
      char *parsed[100];
      int len;
      scanf("%s", dire);
      divideName(dire, parsed, len);
      count += insertTree(root, parsed, len, 0);
    }

    printf ("Case #%d: %d\n", i, count);
  }
}