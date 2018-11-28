#include <cstdio>
#include <vector>
#include <set>

using std::vector;
using std::set;

int main()
{
  int C;
  scanf("%d", &C);
  for(int nc=1; nc<=C; ++nc) {
    int A, B, P;
    scanf("%d%d%d", &A, &B, &P);
    vector<int> v[1001];
    vector<int> s(1001);
    for(int i=A; i<=B; ++i) {
      int x=i;
      for(int j=2; x >= j; ++j) {
	if(0==(x%j) && j >= P) {
	  v[i].push_back(j);
	}
	while(0==(x%j))
	  x /= j;
      }
    }
    for(int i=0; i<1001; ++i)
      s[i] = i;
    for(int i=A; i<=B; ++i)
      for(int j=i+1; j<=B; ++j)
	if(s[i] != s[j]) {
	  vector<int>::const_iterator it1, it2;
	  it1 = v[i].begin();
	  it2 = v[j].begin();
	  while(it1 != v[i].end() && it2 != v[j].end()) {
	    if(*it1 == *it2) {
	      int old = s[j];
	      for(int k=A; k<=B; ++k)
		if(s[k] == old)
		  s[k] = s[i];
	      break;
	    }
	    if(*it1 > *it2)
	      ++it2;
	    else
	      ++it1;
	  }
	}
    set<int> st;
    for(int i=A; i<=B; ++i)
      st.insert(s[i]);
    printf("Case #%d: %d\n", nc, st.size());
  }
  return 0;
}
