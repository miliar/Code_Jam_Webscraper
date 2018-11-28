#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstdlib>
using namespace std;

int W, L, N, r[1111];
double x[1111], y[1111];
vector<pair<double,int> >v;
vector<pair<int,pair<double,double> > >aa;

bool sec(int p, int q) {
  return (x[p]-x[q])*(x[p]-x[q])+(y[p]-y[q])*(y[p]-y[q])<
    (v[p].first+v[q].first)*(v[p].first+v[q].first);
}

int main() {
  int T;
  scanf("%d", &T);
  for (int tc=1; tc<=T; tc++) {
    v.clear();
    aa.clear();
    scanf("%d%d%d", &N, &W, &L);
    for (int i=0; i<N; i++) {
      scanf("%d", r+i);
      v.push_back(make_pair(r[i], i));
    }

    sort(v.begin(), v.end());
    reverse(v.begin(), v.end());
    x[0]=y[0]=0;
    x[1]=W;y[1]=L;
    for (int i=2; i<N; i++) {

      for (int k=0; ; k++) {
	x[i]=(double) rand()/RAND_MAX*W;
	y[i]=(double) rand()/RAND_MAX*L;
	bool b=1;
	for (int j=0; b && j<i; j++) {
	    if (sec(i,j)) b=0;
	}
	if (b) break;
	if (k==10000) {
	  i=1;
	  break;
	}
      }
    }
    for (int i=0; i<N; i++) aa.push_back(make_pair(v[i].second, make_pair(x[i], y[i])));
    sort(aa.begin(), aa.end());

    printf("Case #%d:", tc);
    for (int i=0; i<N; i++)
      printf(" %.9f %.9f", aa[i].second.first, aa[i].second.second);
    puts("");
    
  }

  return 0;
}
