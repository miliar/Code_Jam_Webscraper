#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int nt, nt0;
int c, d, n;
char combine[64][3], oppose[64][2];
char text[128], ans[128];
int end;
bool tem['Z'-'A'+1];

int main() {
  scanf(" %d", &nt0);
  for(nt = 1 ; nt <= nt0 ; nt++) {

    scanf(" %d", &c);
    for(int i=0 ; i<c ; i++)
      for(int j=0 ; j<3 ; j++)
	scanf(" %c", &combine[i][j]);

    scanf(" %d", &d);
    for(int i=0 ; i<d ; i++)
      for(int j=0 ; j<2 ; j++)
	scanf(" %c", &oppose[i][j]);

    scanf(" %d", &n);
    for(int i=0 ; i<n ; i++)
      scanf(" %c", &text[i]);

    ans[0] = text[0];
    end = 1;
    for(int i=1 ; i<n ; i++) {
      if(end > 0)
      for(int j=0 ; j<c ; j++)
	if(text[i] == combine[j][0] && ans[end-1] == combine[j][1]) {
	  ans[end-1] = combine[j][2];
	  goto NEXT;
	} else if(text[i] == combine[j][1] && ans[end-1] == combine[j][0]) {
	  ans[end-1] = combine[j][2];
	  goto NEXT;
	}

      fill(tem, tem+'Z'-'A'+1, false);
      for(int j=0 ; j<end ; j++)
	tem[ans[j]-'A'] = true;
      for(int j=0 ; j<d ; j++)
	if(text[i] == oppose[j][0] && tem[oppose[j][1]-'A']) {
	  end = 0;
	  goto NEXT;
	} else if(text[i] == oppose[j][1] && tem[oppose[j][0]-'A']) {
	  end = 0;
	  goto NEXT;
	}

      ans[end++] = text[i];

    NEXT:
      ;
    }

    printf("Case #%d: [", nt);
    if(end > 0) printf("%c", ans[0]);
    for(int i=1 ; i<end ; i++)
      printf(", %c", ans[i]);
    printf("]\n");
  }
  return 0;
}
