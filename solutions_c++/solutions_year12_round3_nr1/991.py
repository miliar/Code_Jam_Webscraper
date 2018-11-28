#include <stdio.h>
#include <string.h>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
	int T;
	
  scanf("%d", &T);
	
	for (int t=1; t<=T; t++) { 
	    //printf("--------------------\n");
	    int N;
      bool graph[1001][1001];
      memset(graph, 0, sizeof(graph));
      
      scanf("%d", &N);
    	for (int n=1; n<=N; n++) {    
    	  int M;
	      scanf("%d", &M);
	      for (int m=1; m<=M; m++) {
	        int x;
	        scanf("%d", &x);
	        graph[n][x] = 1;
	      }
    	}
    	
    	bool cycle = false;
    	for (int n=1; n<=N; n++) {
      	bool visited[1001];
      	queue<int> q;
      	
    	  memset(visited, 0, sizeof(visited));
      	
      	q.push(n);
      	
      	while (!q.empty() && !cycle) {
      	  int i = q.front();
      	  q.pop();
      	  //printf("i: %d\n", i);
        	for (int j=1; j<=N; j++) {
        	  if (graph[i][j] == 1 && visited[j] == 1) {
    	        printf("Case #%d: Yes\n", t);  
    	        cycle = true;
    	        n=N+1;
    	        break;
    	      }
    	      
    	      if (graph[i][j] == 1 && visited[j] == 0) {
    	        //printf("push i: %d, j: %d\n", i, j);
    	        q.push(j);
    	        visited[j] = 1;
    	      }
        	}
        }
    	}
    	
    	if (!cycle)
    	  printf("Case #%d: No\n", t);  
	}
	
  return 0;
}
