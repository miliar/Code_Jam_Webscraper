#include <cstdio>
#include <list>
#include <queue>

bool is_tree_root(int root, std::list<int> *G, int N) {
  bool vis[1001];
  std::queue<int> q;
  q.push(root);

  for(int i=0;i<=1000;i++) vis[i] = false;
  vis[root] = true;

  //printf("Starting BFS at %d\n", root);
  while(!q.empty()) {
    int cur = q.front();
    q.pop();
    //printf("\tAt %d...\n", cur);

    for(std::list<int>::iterator it = G[cur].begin(); it != G[cur].end(); it++) {
      if(vis[*it]) {
        return false;
      } else {
        q.push(*it);
        vis[*it] = true;
      }
    }
  }

  return true;
}

int main() {
  FILE *fin = fopen("input.txt", "r"), *fout = fopen("output.txt", "w");  
  int T, t, N, deg, i, s, d;
  std::list<int> G[1001];

  bool is_root[1001];

  for(i=1;i<=1000;i++) {
    is_root[i] = true;
  }

  fscanf(fin, "%d", &T);
  for(t=1;t<=T;t++) {
    fscanf(fin, "%d", &N);
    for(s=1;s<=N;s++) {
      fscanf(fin, "%d", &deg);
      for(i=1; i<=deg; i++) {
        fscanf(fin, "%d", &d);
        G[s].push_back(d);
        is_root[d] = false;
      }
    }



    printf("Testcase %d... ", t);

    bool is_diamond = false;
    for(i=1;i<=N;i++) {
      if(is_root[i]) {
        if(!is_tree_root(i, G, N)) {
          is_diamond = true;
          break;
        }
      }
    }

    for(i=1;i<=N;i++) {
      is_root[i] = true;
      G[i].clear();
    }

    printf("%s!\n", is_diamond?"Diamond":"Tree");
    fprintf(fout, "Case #%d: %s\n", t, is_diamond?"Yes":"No");
  }
  
  fclose(fin); fclose(fout);
  return 0;
}
