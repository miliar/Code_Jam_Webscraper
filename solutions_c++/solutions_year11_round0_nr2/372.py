#include <cstdio>
#include <cstdlib>
#include <vector>

int main()
{
  int T;
  scanf("%d", &T);
  for(int cases=1; cases<=T; ++cases) {
    std::vector<std::vector<char> > comb('Z'-'A'+1,
					 std::vector<char>('Z'-'A'+1));
    std::vector<int> opp('Z'-'A'+1);
    std::vector<int> charcount('Z'-'A'+1);
    int charmask = 0;
    std::vector<char> element;
    char str[10];
    int C;
    scanf("%d", &C);
    for(int i=0; i<C; ++i) {
      scanf("%s", str);
      const char c1 = str[0]-'A';
      const char c2 = str[1]-'A';
      const char c3 = str[2];
      comb[c1][c2] = comb[c2][c1] = c3;
    }
    int D;
    scanf("%d", &D);
    for(int i=0; i<D; ++i) {
      scanf("%s", str);
      const char c1 = str[0]-'A';
      const char c2 = str[1]-'A';
      opp[c1] |= 1<<c2;
      opp[c2] |= 1<<c1;
    }
    int N;
    scanf("%d", &N);
    for(int i=0; i<N; ++i) {
      char c;
      scanf(" %c", &c);
      c -= 'A';
      element.push_back(c);
      ++charcount[c];
      charmask |= 1<<c;

      while(element.size() > 1) {
	const char last1 = element.back();
	const char last2 = element[element.size()-2];
	char x = comb[last1][last2];
	if(x) {
	  x -= 'A';
	  --charcount[last1];
	  --charcount[last2];
	  if(!charcount[last1])
	    charmask &= ~(1<<last1);
	  if(!charcount[last2])
	    charmask &= ~(1<<last2);
	  element.resize(element.size()-2);
	  element.push_back(x);
	  ++charcount[x];
	  charmask |= 1<<x;
	  continue;
	}
	if(opp[last1] & charmask) {
	  element.clear();
	  charcount.clear();
	  charcount.resize('Z'-'A'+1);
	  charmask = 0;
	}
	break;
      }
    }
    printf("Case #%d: [", cases);
    for(unsigned i=0; i<element.size(); ++i)
      printf(i==(element.size()-1)?"%c":"%c, ", element[i]+'A');
    printf("]\n");
  }
  return 0;
}
