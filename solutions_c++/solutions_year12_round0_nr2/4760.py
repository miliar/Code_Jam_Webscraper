#include<cstdio>

using namespace std;

int main(){
  int T, N, S, p;
  scanf("%d", &T);
  for(int i = 1; i <= T; i++){
    int num = 0;
    int tmp;
    scanf("%d %d %d", &N, &S, &p);

    int cr = 3*p - 2;
    int pr = cr - 2;
    if(p == 1) pr = cr = 1;
    for(int j = 0; j < N; j++){
      scanf("%d", &tmp);
      if(tmp >= cr) num++;
      else if(S > 0 && tmp >= pr){
        S--;
        num++;
      }
    }
    printf("Case #%d: %d\n", i, num);
  }
  return 0;
}
