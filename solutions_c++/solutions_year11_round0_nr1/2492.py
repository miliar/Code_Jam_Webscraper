#include <cstdio>
#include <queue>

using namespace std;

char seq[200];

int main() {
  int nt, cases = 1;

  scanf(" %d", &nt);
  while (nt--) {
    int n;
    scanf(" %d", &n);
    queue<int> B, O;
    for (int i = 0; i < n; i++) {
      int p;
      scanf(" %c %d", &seq[i], &p);
      if (seq[i] == 'B')
	B.push(p);
      else O.push(p);
    }

    int res = 0, pb = 1, po = 1;
    for (int i = 0; i < n; ) {
      bool moveb = false, moveo = false;
      if (seq[i] == 'B' && pb == B.front()) {
	++i;
	B.pop();
	moveb = true;
      } else if (seq[i] == 'O' && po == O.front()) {
	++i;
	O.pop();
	moveo = true;
      }
      
      if (!moveb)
	pb += (B.empty() || B.front() == pb) ? 0 : (B.front() > pb ? 1 : -1);

      if (!moveo)
	po += (O.empty() || O.front() == po) ? 0 : (O.front() > po ? 1 : -1);
	      
      ++res;
    }

    printf("Case #%d: %d\n", cases++, res);
  }

  return 0;
}
