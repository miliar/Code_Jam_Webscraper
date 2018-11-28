#include <cstdio>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int,int> pii;
typedef vector<pii> vpii;



int main() {
  int N, T, NA, NB, hh, mm;
  scanf("%d", &N);
  for(int n=0;n<N;++n) {
    scanf("%d %d %d", &T, &NA, &NB);
    vpii v;
    for(int na=0;na<NA;++na) {
      scanf("%d:%d", &hh, &mm);
      v.push_back(make_pair(hh*60+mm, 4));
      scanf("%d:%d", &hh, &mm);
      v.push_back(make_pair(hh*60+mm+T, 2));
    }
    for(int nb=0;nb<NB;++nb) {
      scanf("%d:%d", &hh, &mm);
      v.push_back(make_pair(hh*60+mm, 3));
      scanf("%d:%d", &hh, &mm);
      v.push_back(make_pair(hh*60+mm+T, 1));
    }
    sort(v.begin(), v.end());
    int sa=0, sb=0, a=0, b=0;
    for(int i=0;i<(int)v.size();++i) {
      switch(v[i].second) {
      case 1:
	++a;
	break;
      case 3:
	if(b==0)
	  ++sb;
	else
	  --b;
	break;
      case 2:
	  ++b;
	break;
      case 4:
	if(a==0)
	  ++sa;
	else
	  --a;
	break;
      }
    }
    printf("Case #%d: %d %d\n",n+1,sa,sb);
  }
}
