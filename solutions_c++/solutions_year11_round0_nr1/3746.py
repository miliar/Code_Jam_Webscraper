#include <cstdio>
#include <queue>

int main() {
  int z;
  scanf("%d", &z);
  std::queue<int> O,B;
  std::queue<char> Q;
  for(int j=0;j<z;++j) {
    int n;
    scanf("%d ", &n);
    
    for(int i=0; i<n; ++i) {
      char rob; int but;
      scanf("%c %d ", &rob, &but);
      if(rob=='O') O.push(but);
      else B.push(but);
      Q.push(rob);
    }

    int i = 0;
    int O_cur = 1;
    int B_cur = 1;
    while(!Q.empty()) {
      //printf("%c %d %d %d %d\n", Q.front(), O.front(), O_cur, B.front(), B_cur);
      if(Q.front() == 'O' && (O.front() == O_cur)) {
	O.pop();
	Q.pop();
	goto L1;
      }
      if( !O.empty() && O.front() < O_cur ) --O_cur;
      else if(!O.empty() && O.front() > O_cur) ++O_cur;
    
      if((Q.front() == 'B' && (B.front() == B_cur))) {
	Q.pop();
	B.pop();
	goto L2;
      }
    L1:
      if( !B.empty() && B.front() < B_cur ) --B_cur;
      else if(!B.empty() && B.front() > B_cur) ++B_cur;
    L2:;
      i++;
    }
   
    
    
    printf("Case #%d: %d\n", j+1,i );
  }
  
}

