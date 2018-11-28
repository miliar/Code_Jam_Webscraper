#include <cstdio>
#include <string>

using namespace std;

char mapping[32] = {0};

void trainMapping(string a, string b) {
   for (int i=0; i<a.length(); i++) {
      if ('a' <= b[i] && b[i] <= 'z') {
         mapping[b[i] - 'a'] = a[i];
      }
   }
}

void solve() {
   char lin[1024];
   fgets(lin, sizeof(lin), stdin);
   const int length = strlen(lin);
   for (int i=0; i<length; i++) {
      if ('a' <= lin[i] && lin[i] <= 'z') {
         lin[i] = mapping[lin[i] - 'a'];
      }
   }
   printf("%s", lin);
}

int main() {
   freopen("A-small-attempt0.in", "rb", stdin);
   freopen("A-data.txt", "wb", stdout);

   mapping['z' - 'a'] = 'q';
   mapping['q' - 'a'] = 'z';

   trainMapping("our language is impossible to understand", "ejp mysljylc kd kxveddknmc re jsicpdrysi");
   trainMapping("there are twenty six factorial possibilities", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
   trainMapping("so it is okay if you want to just give up", "de kr kd eoya kw aej tysr re ujdr lkgc jv");

   int tst;
   scanf("%d\n", &tst);
   for (int i=1; i<=tst; i++) {
      printf("Case #%d: ", i);
      solve();
   }
   fclose(stdout);
}