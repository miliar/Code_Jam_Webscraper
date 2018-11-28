#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
vector<int> mat;
int f[200];
int main(void) {
  freopen("fdin.txt","r",stdin);
  freopen("fdout.txt","w",stdout);
  int T;
  scanf("%d\n",&T);
  int cas = 1;
  while (T--) {
    mat.clear();
    int P,Q;
    scanf("%d%d",&P,&Q);
    for (int i = 0;i<Q;++i) {
      int tmp;
      scanf("%d",&tmp);
      mat.push_back(tmp);
    }
    sort(mat.begin(),mat.end());
    int ans = 10000000;
    do {
      memset(f,0,sizeof(f));
      int cnt = 0;
      for (int i = 0;i<Q;++i) {
        f[mat[i]-1] = 1;
        for (int j = mat[i]-2;j>=0 && f[j]==0;--j) ++cnt;
        for (int j = mat[i];j<P && f[j]==0;++j) ++cnt;
      }
      ans = cnt<ans?cnt:ans;
    }while(next_permutation(mat.begin(),mat.end()));
    printf("Case #%d: %d\n",cas,ans);
    ++cas;
  }
}