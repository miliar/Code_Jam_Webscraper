/*******************************************************************************
   Charlie Andrews
   Google Code Jam, Qualification Round Problem B
******************************************************************************/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Combination {
   char first;
   char second;
   char result;

   bool operator==(const Combination &b) const {
      return ((first == b.first && second == b.second) ||
              (first == b.second && second == b.first));
   }
};

struct Opposition {
   char first;
   char second;

   bool operator==(const Opposition &b) const {
      return ((first == b.first && second == b.second) ||
              (first == b.second && second == b.first));
   }
};

bool opposes(char a, vector<char> watchList) {
   vector<char>::iterator it = find(watchList.begin(),
                                    watchList.end(),
                                    a);

   return (it != watchList.end());
}

bool combines(vector<Combination> combos, char a, char b, char &result) {
   Combination desired;
   desired.first = a;
   desired.second = b;
   vector<Combination>::iterator it = find(combos.begin(), combos.end(), desired);
   if(it != combos.end())
      result = it -> result;

   return (it != combos.end());
}

// Clears the chain with the new chain starting at character n
string clearChain(string chain, int n) {
   string newChain = "";

   if(n < chain.size()) {
      newChain = chain.substr(n, chain.size() - n);
   }
   
   return newChain;
}

string combine(string chain, int a, int b, char newChar) {
   string newChain;

   if(a != 0) {
      newChain += chain.substr(0, a);
   }
   newChain += newChar;
   if(b != (chain.size() - 1)) {
      newChain += chain.substr(b + 1, chain.size() - b);
   }
   
   return newChain;
}

void addOppositions(char c,
                     vector<Opposition> opps,
                     vector<char> &currentWatch) {
   for(int i = 0; i < opps.size(); ++i) {
      if(opps[i].first == c)
         currentWatch.push_back(opps[i].second);
      else if(opps[i].second == c)
         currentWatch.push_back(opps[i].first);
   }
}

void solve(string chain, vector<Combination> combos, vector<Opposition> opps) {
   vector<char> watchList;

   while(true) {
      string originalChain = chain;

      // Skip the first character (it won't ever combine with the one previous
      int pos = 1;

      while(pos < chain.size()) {
         char result;

         if(combines(combos, chain[pos], chain[pos - 1], result)) {
            chain = combine(chain, pos - 1, pos, result);
            break;
         }

         // Only add the character to possible oppositions when it's no longer
         // possible that it'll be combined
         addOppositions(chain[pos - 1], opps, watchList);

          if(opposes(chain[pos], watchList)) {
            watchList.clear();
            chain = clearChain(chain, pos + 1);
            break;
         }

         // Move on to the next character
         ++pos;
      }
      
      // We made it through an entire iteration without changing the string -
      // our work is done
      if(chain == originalChain)
         break;
   }

   cout << "[";
   for(int i = 0; i < chain.size(); ++i) {
      cout << chain[i];
      if(i != chain.size() - 1)
         cout << ", ";
   }
   cout << "]";
}

int main() {
   int caseCount;
   cin >> caseCount;

   for(int i = 1; i <= caseCount; ++i) {
      vector<Combination> combinations;
      vector<Opposition> oppositions;
      string chain;

      int comboCount;
      cin >> comboCount;

      for(int j = 0; j < comboCount; ++j) {
         Combination c;
         cin >> c.first >> c.second >> c.result;
         combinations.push_back(c);
      }

      int oppCount;
      cin >> oppCount;

      for(int j = 0; j < oppCount; ++j) {
         Opposition o;
         cin >> o.first >> o.second;
         oppositions.push_back(o);
      }

      int chainLength;
      cin >> chainLength;
      cin >> chain;
      
      cout << "Case #" << i << ": ";
      solve(chain, combinations, oppositions);
      cout << endl;
   }
}
