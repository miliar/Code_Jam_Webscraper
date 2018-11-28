#include <cassert>
#include <cstdio>

using namespace std;

struct trie {
  trie() {
    cnt = 0;
    for(int i=0; i<26; ++i) {
      v[i] = 0;
    }
  }
  int cnt;
  trie * v[26];
};

void insert(trie * t, char * str) {
  if (*str) {
    if (!t->v[*str-'a']) {
      t->v[*str-'a'] = new trie();
    }
    insert(t->v[*str-'a'], str+1);
  } else {
    ++t->cnt;
  }
}

int count(trie * t, char * str) {
  if (*str) {
    if (*str >= 'a' && *str <= 'z') {
      if (t->v[*str-'a']) {
	return count(t->v[*str-'a'], str+1);
      } else {
	return 0;
      }
    } else {
      char * next;
      assert(*str == '(');
      for(next=str; *next && *next != ')'; ++next);
      assert(*next == ')');
      int cnt = 0, seen = 0;
      for(++str; str<next; ++str) {
	if (!(seen&(1<<(*str-'a')))) {
	  seen |= 1<<(*str-'a');
	  if (t->v[*str-'a']) {
	    cnt += count(t->v[*str-'a'], next+1);
	  }
	}
      }
      return cnt;
    }
  } else {
    return t->cnt;
  }
}

int main() {
  int l, d, n; scanf("%d%d%d", &l, &d, &n);
  trie root;
  while(d--) {
    char str[20]; scanf("%s", str);
    insert(&root, str);
  }
  for(int i=1; i<=n; ++i) {
    char str[1024]; scanf("%s", str);
    printf("Case #%d: %d\n", i, count(&root, str));
  }
}
