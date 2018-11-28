#include <cstdio>
#include <vector>

int main()
{
  int L, D, N;
  scanf("%d%d%d", &L, &D, &N);
  std::vector<std::vector<int> > dictionary;
  char str[1000];
  for(int i=0; i<D; ++i) {
    scanf("%s", str);
    std::vector<int> v;
    for(int j=0; j<L; ++j) {
      v.push_back(1<<(str[j]-'a'));
    }
    dictionary.push_back(v);
  }
  for(int i=1; i<=N; ++i) {
    std::vector<int> word;
    scanf("%s", str);
    for(int j=0; str[j]; ++j) {
      int p=0;
      if(str[j]=='(')
	while(str[++j]!=')')
	  p |= 1<<(str[j]-'a');
      else
	p = 1<<(str[j]-'a');
      word.push_back(p);
    }
    int poss=0;
    for(int j=0; j<D; ++j) {
      int k;
      for(k=0; k<L; ++k)
	if(0 == (dictionary[j][k]&word[k]))
	  break;
      if(k==L)
	++poss;
    }
    printf("Case #%d: %d\n", i, poss);
  }
}
