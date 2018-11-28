#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>

using namespace std;

int  main (void) {
  int tn;
  scanf ("%d", &tn);

  for (int tt = 1; tt <= tn; tt++) {
    int cnt[26], bad[26][26], ne[26][26];
    memset (cnt, 0, sizeof (cnt));
    memset (bad, 0, sizeof (bad));
    memset (ne, -1, sizeof (ne));

    int n;
    string s;
    int v[1000], vn = 0;

    scanf ("%d", &n);
    while (n--) {
      cin  >> s;
      ne[s[0] - 'A'][s[1] - 'A'] = s[2] - 'A';
      ne[s[1] - 'A'][s[0] - 'A'] = s[2] - 'A';
    }

    scanf ("%d", &n);
    while (n--) {
      cin  >> s;
      bad[s[0] - 'A'][s[1] - 'A'] = 1;
      bad[s[1] - 'A'][s[0] - 'A'] = 1;
    }

    scanf ("%d", &n);
    cin >> s;
    for (int i = 0; i < (int)s.size(); i++) {
      int c = s[i] - 'A';
      v[vn++] = c;
      cnt[c]++;
      while (vn > 1 && ne[v[vn - 1]][v[vn - 2]] != -1) {
        cnt[v[vn - 1]]--;
        cnt[v[vn - 2]]--;
        vn--;
        v[vn - 1] = ne[v[vn]][v[vn - 1]];
        cnt[v[vn - 1]]++;
      }
      cnt[v[vn - 1]]--;
      for (int i = 0; i < 26; i++) {
        if (cnt[i] && bad[v[vn - 1]][i]) {
          vn = 0;
          memset (cnt, 0, sizeof (cnt));
          break;
        }
      }
      
      if (vn) {
        cnt[v[vn - 1]]++;
      }
    }
    
    printf ("Case #%d: ", tt);
    for (int i = 0; i < vn; i++) {
      printf ("%c%c%c", " ["[!i], v[i] + 'A', ",]"[i + 1 == vn]);
    }
    if (!vn) {
      printf ("[]");
    }
    puts ("");
  }

  return 0;
}