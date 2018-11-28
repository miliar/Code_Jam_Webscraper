#include <cstdio>
#include <map>
#include <string>
#include <vector>

int main()
{
  int N;
  char str[1000];
  scanf("%d", &N);
  for(int nc=1; nc<=N; ++nc) {
    int S, Q;
    std::map<std::string, int> st;
    scanf("%d", &S);
    gets(str);
    for(int i=0; i<S; ++i) {
      gets(str);
      st[str] = i;
    }
    std::vector<int> v(S);
    scanf("%d", &Q);
    gets(str);
    for(int i=0; i<Q; ++i) {
      gets(str);
      std::map<std::string, int>::const_iterator it = st.find(str);
      if(st.end() != it) {
	int min = 1000000000;
	for(int j=0; j<S; ++j)
	  if((j != it->second) && (min > v[j]))
	    min = v[j];
	v[it->second] = min + 1;
      }
    }
    int min = 1000000000;
    for(int i=0; i<S; ++i)
      if(min > v[i])
	min = v[i];
    printf("Case #%d: %d\n", nc, min);
  }
  return 0;
}
