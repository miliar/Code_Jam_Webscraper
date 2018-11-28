#include <cstdio>
#include <cstdlib>
#include <stack>
#include <map>
#include <queue>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class node 
{
 public:
  string name;
  vector<node*> * nodes;
  node(string theName)
  {
    name = theName;
    nodes = new vector<node*>();
  }
};


int add(queue<string> paths, node* curr)
{
  int result = 0;
  string target = paths.front();
//printf("target:%s\n", target.c_str());
  node* nextNode = NULL;
  if ((curr == NULL) || (paths.empty())){
    return 0;
  }
  for (vector<node*>::iterator it = curr->nodes->begin(); it != curr->nodes->end(); ++it) {
    if (target == (*it)->name) {
      nextNode = (*it);
      break;
    }
  }
  if (nextNode == NULL) {
    result++;
//printf("add Path:%d\n", result);
    nextNode = new node(target);
    curr->nodes->push_back(nextNode);
  }
  paths.pop();
  return (paths.empty())? result: (result + add(paths, nextNode));
}

int main(int argc, const char *argv[])
{
  int T; //Number of cases

  scanf("%d\n", &T);

  for (int i = 0; i < T; i++) {
    node* tree = new node("");
    vector<string> existedPath;


    int result = 0;
    int N = 0;  //The next N lines each give the path of one directory that already exists on your computer. 
    int M = 0;  //The next M lines each give the path of one directory that you want to create.

    scanf("%d %d\n", &N, &M);

    for (int n = 0; n < N; n++) {
      queue<string> createPath;
      char* input = new char[10240];
      scanf("%s\n", input);

      char* pch = strtok (input,"/");
      while (pch != NULL)
      {
        string str(pch);
        createPath.push(str);
//printf("add:%s\n", str.c_str());
        pch = strtok (NULL, "/");
      }

      add(createPath, tree);
      delete input;
    }

    for (int m = 0; m < M; m++) {
      queue<string> createPath;
      char* input = new char[10240];
      scanf("%s\n", input);
      string str(input);

      char* pch = strtok (input,"/");
      while (pch != NULL)
      {
        string str(pch);
        createPath.push(str);
//printf("add2:%s\n", str.c_str());
        pch = strtok (NULL, "/");
      }

      result += add(createPath, tree);
      delete input;
    }

    printf("Case #%d: %d\n", i+1, result);

  }

  return 0;
}
