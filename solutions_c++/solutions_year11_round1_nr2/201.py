#include <map>
#include <string>
#include <vector>
#include <iostream>
using namespace std;
void realsolver(const vector<string> &words, map<string, string> matches, map<string, int> counter, map<string, map<int, int> > letters, string list) {
// cout << "I" << endl;
   int rev = 0;
   int best = 0;
   int alreadyLost = 0;
   map<string, bool> hangers;
   map<string, int> lostPoints;

   while (matches.size()) {
     hangers.clear();
     for (int x = 0; x < words.size(); x++) {
       if (matches.count(words[x]) && counter[matches[words[x]]] == 1) {
         counter.erase(matches[words[x]]);
         matches.erase(words[x]);
// cout << "D " << words[x] << endl;
       } else {
         if (matches.count(words[x]) && letters[words[x]].count(list[rev])) {
           hangers[matches[words[x]]] = true;
// cout << "H " << matches[words[x]] << endl;
         }
       }
     }

     for (int x = 0; x < words.size(); x++) {
       if (matches.count(words[x]) && hangers.count(matches[words[x]])) {
         int lost = 1;
         string hangy = matches[words[x]];
         for (int y = 0; y < hangy.size(); y++) {
           if (words[x][y] == list[rev]) {
             hangy[y] = list[rev];
             lost = 0;
           }
         }
// cout << "L " << lost << " " << words[x] << endl;

         counter[hangy]++;
         matches[words[x]] = hangy;
         lostPoints[words[x]] += lost;
         if (lostPoints[words[x]] >= alreadyLost) {
           best = (lostPoints[words[x]] == alreadyLost) ? min(x, best) : x;
           alreadyLost = lostPoints[words[x]];
// cout << "R " << alreadyLost << " " << words[x] << endl;
         }
       }
     }
     if (++rev == list.size()) break;
   }

   cout << " " << words[best];
}
void solver() {
  int W, L;
  string word;
  vector<string> words;
  map<string, int> counter;
  map<string, string> matches;
  map<string, map<int, int> > letters;
  cin >> W >> L;
  for (int x = 0; x < W; x++) {
    cin >> word;
    words.push_back(word);
    string hangy(word.size(), '-');
    matches[word] = hangy;
    counter[hangy]++;
    for (int y = 0; y < word.size(); y++) {
      letters[word][word[y]]++;
    }
  }

  for (int x = 0; x < L; x++) {
    cin >> word;
    realsolver(words, matches, counter, letters, word);
  }
}
int main() {
  int N;
  cin >> N;
  for (int x = 0; x < N; x++) {
    cout << "Case #" << (x+1) << ":";
    solver();
    cout << endl;
  }
  return 0;
}

