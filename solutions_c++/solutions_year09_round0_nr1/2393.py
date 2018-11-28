#include <iostream>
#include <set>
#include <vector>
using namespace std;

const int MAX_L = 15, MAX_D = 5000, MAX_N = 500;

string words[MAX_D + 5];
int L, D, N;

int main(){
  cin >> L >> D >> N;
  for(int i = 0; i < D; ++i)
    cin >> words[i];
//   for(int i = 0; i < D; ++i)
//     cout << words[i] << endl;
  for(int i = 1; i <= N; ++i){
    vector< set<char>* > pattern;
    char c;
    for(int j = 0; j < L; ++j){
      set<char> *c_set = new set<char>();
      cin >> c;
      if( c == '(' ) {
        cin >> c;
        while( c != ')' ){
          c_set->insert(c);
          cin >> c;          
        }
      } else {
        c_set->insert(c);
      }
      pattern.push_back(c_set);
    }
    
    int matches = 0;
    for(int w = 0; w < D; ++w){
      for(int k = 0; k < words[w].length(); ++k){
        if(pattern[k]->find(words[w][k]) == pattern[k]->end())
          goto not_matches;
      }
      matches++;      
      not_matches: ;
    }
    printf("Case #%d: %d\n", i, matches);
//     for(vector< set<char>* >::iterator it = pattern.begin(); it != pattern.end(); ++it){
//       for(set<char>::iterator set_it = (*it)->begin(); set_it != (*it)->end(); ++set_it){
//         printf("%c,", *set_it);
//       }
//       printf("\n");
//     }
  }
  return 0;
}