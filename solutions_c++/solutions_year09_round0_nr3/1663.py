#include <iostream>
int N,len;
#define MAX 510
char st[MAX];
char gcj[] = "welcome to code jam";
int d[MAX][3];
int find_ans(int step,int pre) {
  int ret = 0;
  if (step==19) {
    ++ret;
  } else {
    for (int i = pre+1;i<len;++i) {
      if (st[i]==gcj[step])
        ret+=find_ans(step+1,i);
      ret%=10000;
    }
  }
  return ret%10000;
}
int main(void) {
  int N;
  freopen("fdin.txt","r",stdin);
  freopen("fdin.out","w",stdout);
  scanf("%d\n",&N);
  for (int i = 1;i<=N;++i) {
    scanf("%[^\n]\n",st);
    len = strlen(st);
    int tmp = find_ans(0,-1);
    printf("Case #%d: ",i);
    if (tmp<10) putchar('0');
    if (tmp<100) putchar('0');
    if (tmp<1000) putchar('0');
    printf("%d\n",tmp);
  }
  return 0;
}