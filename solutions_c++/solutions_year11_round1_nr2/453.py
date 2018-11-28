#include <vector>
#include <iostream>
#include <cstdlib>
#include <map>
#include <algorithm>
#include <iterator>
#include <set>
#include <list>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
#include <string>

using namespace std;
using namespace std::tr1;

list<size_t> positionsWithLetter(string s,char letter)
{
  list<size_t> result;
  for (size_t i = 0;i < s.size();++i) {
    if (s[i] == letter) {
      result.push_back(i);
    }
  }
  return result;
}

int pointsWithWord(const string word,const list<string> & originalWords,string l)
{
  // cout << "Entramos con " << word << " " << l << endl;
  // copy(originalWords.begin(),originalWords.end(),ostream_iterator<string>(cout," "));
  // First, we keep only the words of the correct length
  list<string> words;
  const size_t length = word.size();
  unordered_set<char> availableLetters;
  for (list<string>::const_iterator it = originalWords.begin();it != originalWords.end();++it) {
    if (it->size() == length) {
      words.push_back(*it);
      for (int i = 0;i < length;++i) {
	availableLetters.insert(it->at(i));
      }
    }
  }

  size_t letter = 0;
  int result = 0;
  while (words.size() > 1) {
    while (availableLetters.find(l[letter]) == availableLetters.end()) {
      ++letter;    
    }
    // We are at the next reasonable letter
    list<size_t> positionsInWord = positionsWithLetter(word,l[letter]);
    // copy(positionsInWord.begin(),positionsInWord.end(),ostream_iterator<size_t>(cout," "));
    // cout << endl;
    list<string> temp;
    availableLetters.clear();
    if (!positionsInWord.empty()) {
      for (list<string>::iterator it = words.begin();it != words.end();++it) {
	if (positionsInWord == positionsWithLetter(*it,l[letter])) {
	  for (int i = 0;i < length;++i) {
	    availableLetters.insert(it->at(i));
	  }
	  temp.push_back(*it);
	}
      }
    } else {
      result += 1;
      for (list<string>::iterator it = words.begin();it != words.end();++it) {
	if (it->find(l[letter]) == string::npos) {
	  for (int i = 0;i < length;++i) {
	    availableLetters.insert(it->at(i));
	  }
	  temp.push_back(*it);
	}
      }      
    }
    words = temp;
    ++letter;
  }
  // cout << "Devolvemos " << result;
  // cout << endl;
  // cout << endl;
  // cout << endl;
  return result;
}

int main()
{
  int T;
  cin >> T;
  for (int caseNumber = 1;caseNumber <= T;++caseNumber) {
    list<string> words;
    list<string> lists;
    int N, M;
    cin >> N >> M;
    string s;
    for (int i = 0;i < N;++i) {
      cin >> s;
      words.push_back(s);
    }
    for (int i = 0;i < M;++i) {
      cin >> s;
      lists.push_back(s);
    }
    cout << "Case #" << caseNumber
	 << ":";
    for (list<string>::iterator it = lists.begin();it != lists.end();++it) {
      int max = -1;
      string best;
      for (list<string>::iterator word = words.begin();word != words.end();++word) {
	int newValue = pointsWithWord(*word,words,*it);
	if (newValue > max) {
	  max = newValue;
	  best = *word;
	}
      }
      cout << " " << best;
    }
    cout << endl;
  }
  return 0;
}
