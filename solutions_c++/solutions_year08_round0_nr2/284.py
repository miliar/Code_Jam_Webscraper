#include<iostream>
#include<string>
#include<vector>
#include<queue>

using namespace std;

int get_time(string s) {
  return ((s[0]-'0') * 10 + (s[1]-'0')) * 60 + (s[3]-'0') * 10 + s[4]-'0';
}

struct train {
   int ini, fin, tip;
   train (int a, int b, int c) {
      ini = a, fin = b, tip = c; 
   }   
   bool operator < (const train &A) const {
      if (ini != A.ini) return ini > A.ini;
      if (fin != A.fin) return fin > A.fin;
      return tip > A.tip; 
   }
};

int main() {
   int n;
   cin >> n;
   for (int cas = 1; cas <= n; cas++) {
      int sec;
      cin >> sec;
      int tripA, tripB;
      cin >> tripA >> tripB;
      priority_queue<train> pq;
      for (int i = 0; i < tripA; i++) {
         string s, t; 
         cin >> s >> t;
         pq.push(train(get_time(s),get_time(t),0));
      }
      for (int i = 0; i < tripB; i++) {
         string s, t; 
         cin >> s >> t;
         pq.push(train(get_time(s),get_time(t),1));
      }
      vector<priority_queue<int,vector<int>,greater<int> > > pqWait(2);
      vector<int> res(2);
      while (pq.size()) {
         train a = pq.top();
         pq.pop();
         if (pqWait[a.tip].size() == 0 or pqWait[a.tip].top() > a.ini) res[a.tip]++;
         else                                                          pqWait[a.tip].pop();             
         pqWait[(a.tip+1)%2].push(a.fin+sec);
      }
      cout << "Case #" << cas << ": " << res[0] << " " << res[1] << endl;
   }
}
