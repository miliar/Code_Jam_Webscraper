#include <cstdio>
#include <cstring>

int main() {
  const char msg[] = "welcome to code jam";
  char buff[1000];
  fgets(buff, 1000, stdin);
  int N, c[19];
  sscanf(buff, "%d", &N);
  for(int n=0;n<N;++n) {
    fgets(buff, 1000, stdin);
    memset(c, 0, sizeof(c));
    for(int i=0;i<1000 && buff[i];++i) {
      if(buff[i]=='w') ++c[0];
      for(int j=1;j<19;++j)
	if(buff[i]==msg[j])
	  c[j]+=c[j-1], c[j]%=10000;
    }
    printf("Case #%d: %04d\n",n+1,c[18]);
  }
}
