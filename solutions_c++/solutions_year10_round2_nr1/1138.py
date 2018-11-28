#include <iostream>
#include <algorithm>
#include <string>
#include <list>
#include <cstring>
#include <cstdlib>
#include <cmath>

#define MAX_N 110
#define MAX_M 110
#define MAX_P 200

using namespace std;

string EXISTS_DIRS[MAX_N];
string CREATE_DIRS[MAX_M];

bool myfunction(const char * a, const char * b) {
  return (strcmp(a,b) < 0);
}

int find_slash(const char * str) 
{
  int i = 0;
  for(const char *p = str; *p != '\0'; ++p, ++i)
    if (*p == '/') return i;

  return -1;
}

struct Tree {
  struct TreeNode {
    char name[MAX_P];
    list<TreeNode*> childhood;
    unsigned mkdirs;
    TreeNode(const char* n) : mkdirs(0) { strcpy(name, n); }

    void Add(const char * path, bool count) {
      char subdir[MAX_P]; strcpy(subdir, path);
      
      int sl = find_slash(subdir);
      if(sl != -1) {
	subdir[sl] = 0;
        sl++;
      }
      
      list<TreeNode*>::iterator it = childhood.begin();
      while( it != childhood.end() && strcmp((*it)->name, subdir) )
	++it;
      
      TreeNode* child;
      if ( it == childhood.end() ) {
	childhood.push_back( (child = new TreeNode(subdir)) );
	if(count) mkdirs++;
      } else {
	child = *it;
      }

      if ( sl != -1)
	child->Add( path+sl, count);
    }

    unsigned size(void) {
      unsigned c = 0;
      for(list<TreeNode*>::iterator it = childhood.begin();
	  it != childhood.end(); ++it)
	c += (*it)->size();
      
      return c + 1;
    }

    unsigned get_mkdirs(void) {
      unsigned c = 0;
      for(list<TreeNode*>::iterator it = childhood.begin();
	  it != childhood.end(); ++it)
	c += (*it)->get_mkdirs();
      return c + mkdirs;
    }
  };

  TreeNode root;

  Tree() : root(TreeNode("/")) {}
  void AddExistent(const char * path) {
    const char * p = strchr(path, '/');
    if (p != 0)
      root.Add( p+1, false );
  }

  void AddNoExistent(const char * path) {
    const char * p = strchr(path, '/');
    if (p != 0)
      root.Add( p+1, true );
  }

  unsigned size(void) {
    return root.size();
  }

  unsigned get_mkdirs(void) {
    return root.get_mkdirs();
  }
};

unsigned int solve(unsigned N, unsigned M) {
  return 0;
}

int main()
{
  unsigned T, N, M;
  cin >> T;

  for(unsigned t = 1; t <= T; ++t) {
    Tree tree;

    cin >> N >> M;
    for(unsigned n = 0; n < N; ++n) {
      cin >> EXISTS_DIRS[n];
    }

    for(unsigned m = 0; m < M; ++m)
      cin >> CREATE_DIRS[m];

    sort(EXISTS_DIRS, EXISTS_DIRS+N);
    sort(CREATE_DIRS, CREATE_DIRS+M);

    for(unsigned int n = 0; n < N; ++n) {
      tree.AddExistent(EXISTS_DIRS[n].c_str());
    }

    for(unsigned int m = 0; m < M; ++m) {
      tree.AddNoExistent(CREATE_DIRS[m].c_str());
    }

    cout << "Case #" << t << ": " << tree.get_mkdirs() << endl;

  }

  return 0;
}
