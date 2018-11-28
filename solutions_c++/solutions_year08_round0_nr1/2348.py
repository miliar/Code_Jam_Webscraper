#include <iostream>
#include <vector>
#include <limits.h>


using namespace std;
int cache[102][1002];

int search(vector<string>& s, vector<string>& e) {
   if(s.size() == 0) return 0;
   for(int i = 0; i < e.size(); i++) {
      cache[i][s.size()-1] = s[s.size()-1] == e[i] ? 1:0;
   }
   for(int query = s.size()-2; query >= 0; query--) {
      for(int eng = 0; eng < e.size(); eng++) {
         if(s[query] != e[eng]) {
            cache[eng][query] = cache[eng][query+1];
         } else {
            int min = INT_MAX;
            for(int i = 0; i < e.size(); i++) {
               if(i == eng) continue;
               if(cache[i][query+1] < min) min = cache[i][query+1];
            }
            cache[eng][query] = min + 1;
         }
      }
   }
   int min = INT_MAX;
   for(int i = 0; i < e.size(); i++) {
      if(cache[i][0] < min) min = cache[i][0];
   }
   return min;


}

int main() {
   int NUM_CASES;
   string s;
   cin >> NUM_CASES;
   getline(cin,s);
   for(int i = 0; i < NUM_CASES; i++) {
      int  n;
      cin >> n;
      getline(cin,s);
      vector<string> engines;
      while(n--) {
         string in;
         getline(cin ,in);
         engines.push_back(in);
      }
      vector<string> searches;
      cin >> n;
      getline(cin,s);
      while(n--) {
         string in;
         getline(cin ,in);
         searches.push_back(in);
      }

      int gmin = search(searches, engines);
      

      cout << "Case #" << i+1 << ": " << gmin << endl;
   }
   return 0;
}

