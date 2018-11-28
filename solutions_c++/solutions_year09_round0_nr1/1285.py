#include <iostream>
#include <string>

#include <cassert>
using namespace std;

struct radix_t {
  radix_t *next[26];
  bool word[26];
};




void insert(const string & word, int p, radix_t *& root) {
  radix_t *ptr;
  if (root==NULL) {
    ptr = new radix_t;
    for (int i=0;i<26;i++) {
      ptr->next[i] = NULL;
      ptr->word[i] = false;
    }
    root = ptr;
  }
  if (word.length()-1==p) {
    root->word[word[p]-'a'] = true;
  } else {
    //cout << "Going to " << word[p]-'a' << endl;
    insert(word,p+1, root->next[word[p]-'a']);
  }
}


bool find(const string &word, int p, radix_t *root) {
  if (root==NULL) return false;
  if (word.length()-1==p) {
    return root->word[word[p]-'a'];
  } else {
    return find(word,p+1,root->next[word[p]-'a']);
  }
}

int count_them(const string &word, int p, radix_t *root) {
  if (root == NULL) return 0;
  if (word[p]=='(') {
    int p1 = p+1;
    int p2 = p1;
    while (word[p2]!=')') {
      ++p2;
    }
    //cout << "Here" << endl;
    //cout << p1 << " " << p2 << endl;
    if (p2 == (word.length()-1)) {
      int count = 0;
      for (int i=p1;i<p2;i++) {
	if (root->word[word[i]-'a']) count++;
      }
      return count;
    } else {
      int count = 0;
      for (int i=p1;i<p2;i++) {
	count=count+count_them(word,p2+1,root->next[word[i]-'a']);
	//cout << count << endl;
      }
      return count;
    }
      
    

  }
  else { if (word.length()-1==p) {
      if (root->word[word[p]-'a']) return 1;
      else return 0;
    } else {
      return count_them(word,p+1,root->next[word[p]-'a']);
    }
  }
}

int main() {
  radix_t *tree=NULL;

  int L,D,N;
  cin >> L >> D >> N;

  for (int i=0;i<D;i++) {
    string t;
    cin >> t;
    insert(t,0,tree);
  }
  for (int i=0;i<N;i++) {
    string l;
    cin >> l;
    int count = count_them(l,0,tree);
    cout << "Case #"<<i+1<<": " << count << endl;
  }
}
