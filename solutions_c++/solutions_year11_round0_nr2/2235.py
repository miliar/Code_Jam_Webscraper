#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int C, D;
int com[109][109];
bool opp[109][109];

int inp[109], res[109], N, s;

int main() {
  int T; scanf("%d", &T);

  for(int t = 1; t <= T; t++) {
    scanf("%d", &C);
    memset(com, -1, sizeof(com));
    memset(opp, 0, sizeof(opp));
    for(int i=1; i<=C; i++) {
      char a, b, c;
      do scanf("%c", &a); while(a == ' ' || a == '\n');
      do scanf("%c", &b); while(b == ' ' || b == '\n');
      do scanf("%c", &c); while(c == ' ' || c == '\n');
      com[a-'A'][b-'A'] = com[b-'A'][a-'A'] = c - 'A';
      //printf("COMBINE %c %c\n", a, b);
    }

    scanf("%d", &D);
    for(int i=1; i<=D; i++) {
      char a, b;
      do scanf("%c", &a); while(a == ' ' || a == '\n');
      do scanf("%c", &b); while(b == ' ' || b == '\n');

      opp[a-'A'][b-'A'] = opp[b-'A'][a-'A'] = true;
    }

    scanf("%d", &N);
    char c;
    s = 0;
    for(int i=1; i<=N; i++) {
      do scanf("%c", &c); while(c == ' ' || c == '\n');
      //printf("%c", c);
      s++; res[s] = c-'A';
      int combine;
      if(s>1) combine = com[res[s]][res[s-1]];
      else combine = -1;
      //printf("%d\n", combine);
      if(combine != -1) {
	s--;
	res[s] = combine;
      }
      else{
	for(int j=1; j<s; j++) {
	  if(opp[res[j]][res[s]]) { s = 0; break; }
	}
      }
    }

    printf("Case #%d: [", t);
    for(int i=1; i<=s; i++) { printf("%c", 'A'+res[i]); if(i<s) printf(", "); } printf("]\n");
  }
}
