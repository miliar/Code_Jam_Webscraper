#include <map>
#include <vector>
#include <string>
#include <iostream>

using std::map;
using std::vector;
using std::string;
using std::cout;
using std::cin;
using std::endl;

#define MAXL 20

int L;
int D;
int N;

typedef vector<char>  token_t;
typedef char*         word_t;

struct myInt {
  int			v;
  myInt(int v = -1) : v(v) { }
};

typedef map<int, myInt> hash;

class Trie {
  struct node_t {
    int				orig_state;
    char			c;
    node_t(int orig_state=-1, char c='\0') :
      orig_state(orig_state), c(c) { }
    bool operator<(const node_t &other) const {
      if (orig_state < other.orig_state) return true;
      else if (orig_state > other.orig_state) return false;
      return c < other.c;
    }
  };
  typedef map<node_t, myInt>	tr_map;
  // (orig_state, char) = > (dest_state)
  tr_map			transitions;
  int				next_index;
  hash				CURRENT;
  hash				NEXT;

public:
  Trie() {
    next_index = 1;
  }
  void clear() {
    next_index = 1;
    transitions.clear();
  }
  void addWord(string w) {
    int		 current_state = 0;
    for (int i=0; i<L; ++i) {
      myInt	&dest_state    = transitions[node_t(current_state, w[i])];
      if (dest_state.v == -1)
	dest_state.v	       = next_index++;
      current_state	       = dest_state.v;
    }
  }
  int getNumWords(token_t *pat) {
    CURRENT.clear();
    NEXT.clear();
    CURRENT[0] = myInt(0);
    for (int i=0; i<L; ++i) {
      for (hash::iterator as = CURRENT.begin();
	   as != CURRENT.end();
	   ++as) {
	for (int j=0; j<pat[i].size(); ++j) {
	  tr_map::iterator dest_iterator = transitions.find(node_t(as->first,
								    pat[i][j]));
	  if (dest_iterator != transitions.end())
	    NEXT[dest_iterator->second.v] = myInt(0);
	} // j=0 .. size(token_i)
      } // forall as in CURRENT
      CURRENT.swap(NEXT);
      NEXT.clear();
    } // i=0 .. L-1
    return CURRENT.size();
  }
};

int main()
{
  Trie dict;
  cin >> L >> D >> N;
  for (int i=0; i<D; ++i) {
    string w;
    cin >> w;
    dict.addWord(w);
  }
  for (int i=1; i<=N; ++i) {
    string w;
    cin >> w;
    token_t pat[MAXL];
    int      wpos = 0;
    for (int j=0; j<L; ++j) {
      if (w[wpos] == '(') {
	for (int k=wpos+1; k<w.size(); ++k) {
	  if (w[k] == ')') {
	    wpos = k+1;
	    break;
	  }
	  else pat[j].push_back(w[k]);
	}
      }
      else pat[j].push_back(w[wpos++]);
    }
    cout << "Case #" << i << ": " << dict.getNumWords(pat) << endl;
  }
  return 0;
}
