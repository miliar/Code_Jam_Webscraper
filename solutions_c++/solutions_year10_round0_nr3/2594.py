#include <stdio.h>
#include <inttypes.h>
#include <queue>
#include <iostream>

using namespace std;

int main(){
  int cases;
  scanf("%d",&cases);
  for(int i = 1; i<=cases; i++){
    int r,k,n;
    scanf("%d %d %d",&r,&k,&n);
    queue<int> q;
    for(int j = 0; j < n; j++){
      int m;
      scanf("%d",&m);
      q.push(m);
    }
    uint64_t total = 0;
    for(int j = 0; j < r; j++){
      int on_board = 0;
      int next;
      for(int l = 0; l < n && (next = q.front(), next + on_board <= k); l++){
	on_board += next;
	q.push(q.front());
	q.pop();
      }
      total+= on_board;
    }
    printf("Case #%d: ",i);
    cout<<total<<endl;
  }
  return 0;
}
