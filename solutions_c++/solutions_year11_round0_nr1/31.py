#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;

struct node{
  int task, a, b;
  node(int x = 0, int y = 0, int z = 0):
    task(x), a(y), b(z){}
};

int where[100];
int who[100];
int dist[101][100][100];

int main(){
  int t; scanf("%d", &t);
  for(int caso = 1; caso <= t; caso++){
    int n; cin >> n;
    for(int i = 0; i < n; i++){
      char c; int x; cin >> c >> x;
      who[i] = c == 'B';
      where[i] = x - 1;
    }

    memset(dist, -1, sizeof dist);
    dist[0][0][0] = 0;
    queue<node> q;
    q.push(node(0, 0, 0));
    cout << "Case #" << caso << ": ";

    while(!q.empty()){
      node cur = q.front(); q.pop();
      int task = cur.task, a = cur.a, b = cur.b;
      int d = dist[task][a][b];
      if(task == n){
        cout << d << endl;
        break;
      }
      for(int da = -1; da <= 1; da++)if(a + da >= 0 && a + da < 100)
      for(int db = -1; db <= 1; db++)if(b + db >= 0 && b + db < 100){
        bool pisa = false, pisb = false;
        if(da == 0 && where[task] == a && who[task] == 0)
          pisa = true;
        if(db == 0 && where[task] == b && who[task] == 1)
          pisb = true;
  
        int ntask, na, nb;
        if(!pisa && !pisb)
            ntask = task, na = a + da, nb = b + db;
        else
            ntask = task + 1, na = a + da, nb = b + db;

        if(dist[ntask][na][nb] == -1)
            dist[ntask][na][nb] = d + 1,
              q.push(node(ntask, na, nb));
        
      }
    }
  }
}

