#include <cstdio>
#include <string.h>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

const int MAXL = 10000, MAXA = 100, MAXN = 100, MAXP = 100, MAXLEN = 10;

int prop_cnt;

char dec_fea[MAXL][MAXLEN + 1];
int left[MAXL], right[MAXL];
double weight[MAXL];

struct trie {
  trie* next[4];
  bool end; // 0 for non-ending-node; > 0 for the sequence number of the string
  
  trie() {memset(this, 0, sizeof(trie));}
  ~trie() { for (int i = 0; i < 4; ++i) if (next[i]) delete next[i]; }
};
trie* trie_root;

void print_dec(int r, int l) {
  for (int i = 0; i < l; ++i)
    fputc(' ', stderr);
  fputc('(', stderr);
  if (left[r] != 0) {
    fprintf(stderr, "%f %s\n", weight[r], dec_fea[r]);
    print_dec(left[r], l + 2);
    print_dec(right[r], l + 2);
    for (int i = 0; i < l; ++i)
      fputc(' ', stderr);
    fprintf(stderr, ")\n");
  }
  else
    fprintf(stderr, "%f)\n", weight[r]);
}

void readdata() {
  const int LINELEN = 80;
  char buf[LINELEN + 2];
  int stack[MAXL], dep = -1;
  int l, k;
  double wei;
  double level;

  int fea = -1;
  int str_pos = 0;

  memset(left, 0, MAXL * sizeof(int));
  memset(right, 0, MAXL * sizeof(int));

  scanf("%d\n", &l);

  for (int i = 0; i < l; ++i) {
    gets(buf); k = strlen(buf);
    buf[k] = ' '; buf[++k] = '\0';
    for (int j = 0; j < k; ++j)
      if (buf[j] == '(') {
	
	if (str_pos > 0) {
	  dec_fea[stack[dep]][str_pos] = '\0';
	  weight[stack[dep]] = wei;
	}	  

	/* init */
	wei = 0;
	level = 1;
	str_pos = 0;

	++fea;
	if (dep != -1)
	  if (left[stack[dep]] == 0)
	    left[stack[dep]] = fea;
	  else
	    right[stack[dep]] = fea;
	stack[++dep] = fea;
      }
      else if (buf[j] == ')') {
	if (left[stack[dep]] == 0) {
	  dec_fea[stack[dep]][str_pos] = '\0';
	  weight[stack[dep]] = wei;
	}	  
	  
	--dep;
      }
      else if (buf[j] == ' ' || buf[j] == '\t') {
      }	
      else if (buf[j] == '.') {
	level = 0.1;
      }
      else if (buf[j] >= '0' && buf[j] <= '9') {
	if (level > 0.5) {
	  wei *= 10; wei += buf[j] - '0';
	}
	else {
	  wei += (buf[j] - '0') * level;
	  level /= 10;
	}
      }
      else 
	dec_fea[stack[dep]][str_pos++] = buf[j];
  }

  print_dec(0, 0);

  prop_cnt = fea + 1;
}  

bool find(char* str) {
  char i;
  trie* p; trie** q;

  if (!trie_root) return false;
  p = trie_root;
  for (int j = 0; (i = str[j]) != '\0'; ++j) {
    			q = p->next + (i & 3);
			if (*q == NULL) return false;
			p = *q;
			i >>= 2;
			
			q = p->next + (i & 3);
			if (*q == NULL) return false;
			p = *q;
			i >>= 2;
			
			q = p->next + (i & 3);
			if (*q == NULL) return false;
			p = *q;
			i >>= 2;
			
			q = p->next + (i & 3);
			if (*q == NULL) return false;
			p = *q;			
  }
  return p->end;
}

void solve() {
  char feature[MAXLEN + 2];
  int n, c, k;
  scanf("%d", &n);
  for (int u = 0; u < n; ++u) {
    scanf("%s %d", feature, &c);
    double res = weight[0];

    trie_root = new trie();
    for (int v = 0; v < c; ++v) {
      scanf("%s", feature);
      trie* p; trie** q;
      char i;

      p = trie_root;
      for ( int j = 0; (i = feature[j]) != '\0'; ++j) {
			q = p->next + (i & 3);
			if (*q == NULL) *q = new trie();
			p = *q;
			i >>= 2;
			
			q = p->next + (i & 3);
			if (*q == NULL) *q = new trie();
			p = *q;
			i >>= 2;
			
			q = p->next + (i & 3);
			if (*q == NULL) *q = new trie();
			p = *q;
			i >>= 2;
			
			q = p->next + (i & 3);
			if (*q == NULL) *q = new trie();
			p = *q;			
      }
      p->end = true;
    }
    
    for (int now = 0; ; ) {
      fprintf(stderr, "at %d: prob %f\n", now, res);
      if (find(dec_fea[now]))
	now = left[now];
      else 
	now = right[now];
      if (now == 0)
	break;
      res *= weight[now];
    }

    printf("%f\n", res);
  }
}

int main() {
  int n;
  
  scanf("%d", &n);
  for (int cnt = 1; cnt <= n; ++cnt) {
    readdata();
    printf("Case #%d:\n", cnt);
    solve();
  }
}
