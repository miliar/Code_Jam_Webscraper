#include <iostream>
#include <algorithm>

using namespace std;

#define for_to(i,j,k) for(i=j; i<=k; ++i)
#define for_downto(i,j,k) for(i=j; i>=k; --i)

#define MAX 50

int i,j,k;
int test,n_tests,n;
char tab[MAX][MAX];
int M[MAX],ans,cnt;

int main() {
  scanf("%d",&n_tests);
  for_to(test,1,n_tests) {
    scanf("%d",&n);
    for_to(i,0,n-1) {
      scanf(" %s",tab[i]);
      M[i] = -1;
      for_to(j,0,n-1) {
        if (tab[i][j] =='1') {
          M[i] = j;
        }
      }
    }
    cnt = 0;
    ans = 0;
    //cout << "--" << endl;
    //for_to(i,0,n-1) cout << M[i] << endl;
    //cout << "--" << endl;
    for_to(i,0,n-1) {
      if (M[i] > i) {
        for_to(j,i+1,n-1) {
          if (M[j] <= i) {
            k = j;
            while (k > i) {
              swap(M[k],M[k-1]);
              ++ans;
              --k;
            }
            break;
          }
        }
      }

    }

    printf("Case #%d: %d\n",test,ans);
  }
  return 0;
}
