#include<iostream>
#include<string>
#include<set>

using namespace std;

int main() {
   int n;
   cin >> n;
   for (int cas = 1; cas <= n; cas++) {
      int m;
      cin >> m >> ws;
      string s;
      for (int i = 0; i < m; i++) getline(cin, s);
      int k;
      cin >> k >> ws;
      set<string> S;
      int cnt = 0;
      string ini= "";
      while (k--) {
         getline(cin, s);
         S.insert(s);
         if (S.size() == m) {
            S.clear();
            S.insert(s);
            cnt++;
         }
      }
      cout << "Case #" << cas << ": " << cnt << endl;
   }
}
