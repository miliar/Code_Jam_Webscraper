#include <iostream>
//#include <cstdlib>
#include <cstring>

using namespace std;

#define uint unsigned int 
#define DICT 26
#define MAX_WORD 4096+1

typedef struct _node {
  struct _node * child [DICT];
  _node() {
    memset(child, 0x00, sizeof(struct _node) * DICT);
  }
} Node;

uint L; // Words lenght
uint D; // Number of words in the dictionary
uint N; // Number of cases.

uint count_cases(char * word, uint pos, uint n, Node ** dict) {
  if( n == L ) return 1;    /* Base case... */

  if( word[pos] != '(' ) {
      uint beg = pos, end = pos;
      while(word[beg] != '(' && beg < L) ++beg;
      while(word[end] != ')' && end < L) ++end;

      uint next_pos;
      if(end < beg) next_pos = end + 1;
      else next_pos = pos + 1;

      uint letter = word[pos] - 'a';
      if( dict[letter] != NULL )
	return count_cases(word, next_pos, n+1, dict[letter]->child);
      else return 0;

  } else {
    uint end = ++pos;
    while( word[end] != ')' ) ++end;

    uint sum = 0;
    for(uint p = pos; p < end; ++p) {
      uint letter = word[p] - 'a';
      if ( dict[letter] != NULL )
	sum += count_cases(word, end+1, n+1, dict[letter]->child);
    }
    return sum;
  }  
}

int main() {


  Node * tree [DICT];
  memset(tree, 0x00, sizeof(Node*) * DICT);

  cin >> L >> D >> N;
  
  /* Build dictionary. */
  for(uint i = 0; i < D; ++i){
    char word [MAX_WORD];
    cin >> word;

    Node ** curr_dict = tree;
    for(uint j = 0; j < L; ++j) {
      uint letter = word[j] - 'a';
      if( curr_dict[letter] == NULL )
	curr_dict[letter] = new Node;
      curr_dict = curr_dict[letter]->child;
    }
  }

  
  for(uint i = 0; i < N; ++i) {
    char word [MAX_WORD];
    cin >> word;

    cout << "Case #" << i+1 << ": " << count_cases(word, 0, 0, tree) << endl;
  } 

  return 0;
}
