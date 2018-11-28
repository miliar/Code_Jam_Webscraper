#include<iostream>
using namespace std;
int N;
char buf[1000000];
char msg[]="welcome to code jam";
int calc(char* ptr, int a) {
  if(a==19) return 1;
  int c=0;
  while(*ptr!='\0') {
    if(*ptr==msg[a]) c+=calc(ptr,a+1);
    if(c>1000) c-=1000;
    ptr++;
  }
  return c;
}
int main() {
  scanf("%d\n", &N);
  for(int i=0;i<N;i++) {
    gets(buf);
    printf("Case #%i: %0.4i\n", i+1, calc(buf,0));
  }
  return 0;
}
