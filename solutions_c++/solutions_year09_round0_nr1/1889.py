#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string> 
#include <vector>
#include <stack>
#include <stdexcept>

using namespace std;


struct tnode {
  tnode* children[256];
  tnode() : hits (0) {
    fill (children, children+256, (tnode*)0);
  }
  ~tnode() {
    for (int i = 0; i < 256; ++i) delete children[i];
  }
  int hits;
};

bool match_against_pattern (const std::string& word, const vector<set<char> >& pattern)
{
  for (size_t i = 0; i < word.size(); ++i)
    if (pattern[i].find (word[i]) == pattern[i].end()) return false;
  return true;
}


int main() {
  int l,d,n;
  cin >> l >> d >> n;
  //tnode root;
  vector<string> words;

  
  for (int i = 0; i < d; ++i) {
    string word;
    cin >> word;
    words.push_back (word);
//     tnode* curr = &root;
//     for (int j = 0; j < l; ++j) {
//       if (curr->children[word[j]] == 0) {
//         curr->children[word[j]] = new tnode;
//       }
//       curr = curr->children[word[j]];
//       curr->hits++;
//     }
  }
  for (int case_num = 1; case_num <= n; ++case_num) {
    string pattern;
    cin >> pattern;
    vector<set<char> > ppattern (l);
    int pos = 0;
    bool in_brace = false;
    
    for (size_t j = 0; j < pattern.size(); ++j) {
      if (in_brace) {
        if (pattern[j] == ')') {
          in_brace = false;
          ++pos;
        } else {
          ppattern[pos].insert (pattern[j]);
        }
      } else {
        if (pattern[j] == '(') {
          in_brace = true;
        } else {
          ppattern[pos].insert (pattern[j]);
          ++pos;
        }
      }
      if (pos >= l) break;
    }
//     for (int i = 0; i < l; ++i) {
//       sort (ppattern[i].begin(), ppattern[i].end());
//       ppattern[i].erase (unique (ppattern[i].begin(), ppattern[i].end()), ppattern[i].end());
//     }

    int num_matches = 0;
//     queue<pair<tnode*, int> > q;
//     q.push (make_pair(&root, 0));
//     while (!q.empty()) {
//       tnode* curr = q.front().first;
//       int pos = q.front().second;
//       q.pop();
//       if (pos == l-1) {
//         cerr << "good: " <<  pattern << "\n";
//         num_matches += curr->hits;
//         continue;
//       }
//       for (size_t i = 0; i < ppattern[pos].size(); ++i) {
//         if (curr->children[ppattern[pos][i]] != 0) {
//           q.push (make_pair (curr->children[ppattern[pos][i]], pos+1));
//         }
//       }
//     }
    for (size_t i = 0; i < words.size(); ++i)
      if (match_against_pattern (words[i], ppattern)) ++ num_matches;
    cout << "Case #" << case_num << ": " << num_matches << endl;
  }
          
}
