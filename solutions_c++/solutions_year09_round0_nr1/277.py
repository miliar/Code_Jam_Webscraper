#include <stdio.h>
#include <string.h>

#define MAX_LEN 20
#define MAX_WORDS 5100

char words[MAX_WORDS][MAX_LEN];
char pattern[10000];
int tokens[MAX_LEN];
int L;

inline void parse() {
  memset(tokens,0,sizeof(tokens));
  int l=strlen(pattern);
  int ind=0;
  int i=0;
  while(ind<l) {
    if(pattern[ind]=='(') {
      ++ind;
      while(pattern[ind]!=')')
        tokens[i]|=(1<<(pattern[ind++]-'a'));
      ++ind;
    }
    else {
      tokens[i]=(1<<(pattern[ind++]-'a'));
    }
    ++i;
  }
}

inline int check(char *word) {
  for(int i=0;i<L;++i) {
    if(!(tokens[i]&(1<<(word[i]-'a'))))
      return 0;
  }
  return 1;
}

int main() {
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int D,N;
  scanf("%d%d%d",&L,&D,&N);
  for(int i=0;i<D;++i)
    scanf("%s",words[i]);
  for(int tst=1;tst<=N;++tst) {
    int cnt=0;
    scanf("%s",pattern);
    parse();
    for(int i=0;i<D;++i)
      cnt+=check(words[i]);
    printf("Case #%d: %d\n",tst,cnt);
  }
  return 0;
}
