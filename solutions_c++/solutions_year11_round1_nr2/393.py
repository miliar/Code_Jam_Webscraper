#include <vector>
#include <iostream>
#include <list>
#include <string>
using namespace std;

const int SIZE = 26;

typedef vector<string> Dictionary;
typedef vector<int> Pattern;
typedef vector<Pattern> PatternDictionary;
typedef list<unsigned> IndexList;

IndexList remaining;

int letter_pattern(const string& word, char ch) {
  int pattern = 0;
  for(int i=0;i<word.size();i++) {
    if(word[i] == ch)
      pattern |= (1 << i);
  }
  return pattern;
}

Pattern letter_pattern(const string& word) {
  Pattern p(SIZE + 1);
  for(char ch='a';ch<='z';ch++)
    p[ch - 'a'] = letter_pattern(word, ch);
  p[SIZE] = word.size();
  return p;
}

bool has_letter(unsigned index, const PatternDictionary& PD, char ch) {
  return PD[index][ch - 'a'] != 0;
}

bool is_letter_remaining(const PatternDictionary& PD, char ch) {
  for(IndexList::const_iterator it=remaining.begin();it!=remaining.end();++it)
    if(has_letter(*it, PD, ch))
      return true;
  return false;
}

void remove_matching(const Pattern& pattern, const PatternDictionary& PD, char ch) {
  const int p = pattern[ch - 'a'];
  typedef IndexList::iterator Iter;
  Iter it = remaining.begin();
  while(it != remaining.end()) {
    Iter next = it;
    ++next;
    if(PD[*it][ch - 'a'] != p) {
      remaining.erase(it);
    }
    it = next;
  }
}

int best_score(const Pattern& pattern, const PatternDictionary& PD, const string& L) {
    remaining.clear();
    for(unsigned i=0;i<PD.size();i++) {
      if(PD[i][SIZE] == pattern[SIZE])
	remaining.push_back(i);
    }

    int score = 0;
    for(int i=0;i<L.size();i++) {
      if(remaining.size() <= 1)
	break;

      char ch = L[i];
      if(!is_letter_remaining(PD, ch))
	continue;

      remove_matching(pattern, PD, ch);
      if(!pattern[ch-'a'])
	score++;
    }
    return score;
}

string best_word(const Dictionary& D, const PatternDictionary& PD, const string& L) {
  string best;
  int bestScore = -1;
  for(unsigned i=0;i<D.size();i++) {
    int score = best_score(PD[i], PD, L);
    //    std::cout << "Score for " << D[i] << " with " << L << " is " << score << "\n";
    if(score > bestScore) {
      bestScore = score;
      best = D[i];
    }
  }

  return best;
}

int main()
{
  Dictionary D;
  PatternDictionary PD;
  int T;
  cin >> T;
  for(int c=1;c<=T;c++) {
    int N, M;
    cin >> N >> M;
    D.resize(N);
    PD.resize(N);
    for(int i=0;i<N;i++) {
      string s;
      cin >> s;
      D[i] = s;
      PD[i] = letter_pattern(s);
    }
    cout << "Case #" << c << ": ";
    for(int i=0;i<M;i++) {
      string L;
      cin >> L;
      string best = best_word(D, PD, L);
      if(i > 0)
	cout << " ";
      cout << best;
    }
    cout << "\n";
  }
  return 0;
}

