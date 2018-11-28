#include <cstdio>
#include <cstdlib>
#include <cstring>

char table[] = { 'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char translate(char word)
{
  char trans=table[word-'a'];
  return trans;
}
int main(void)
{
  freopen("A-small.in","r",stdin);
  freopen("A-small.out","w",stdout);
  int N;
  scanf("%d\n", &N);
  for(int i=0; i<N; i++) {
    printf("Case #%d: ", i+1);
    char google;
    while(scanf("%c", &google)!=EOF) {
      if(google=='\n')
	break;
      if(google!=0x20)
	printf("%c",translate(google));
      else printf(" ");
    }
    printf("\n");
  }
  return 0;
}
