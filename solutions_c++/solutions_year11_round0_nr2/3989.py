///@file main.cpp
///@author Marcus Henry Ewert
///@date 2011-05-07


#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>

using namespace std;

pair<char, char> orderedPair(char a, char b){
  if(a > b)
    return make_pair(a, b);
  return make_pair(b, a);
}

int main(int argc, char ** argv){
  int trials;
  cin >> trials;
  for(int trial = 1; trial <= trials; trial++){
    map<char, int> letteruses;
    map<pair<char, char>, char> replacements;
    multimap<char, char> rejects;
    int c;
    cin >> c;
    for(int rep = 0; rep < c; rep++){
      string s;
      cin >> s;
      if(s.length() != 3)
        cout << "ERROR" << s << endl;
      replacements.insert(make_pair(orderedPair(s[0], s[1]) , s[2]));
    }

    int d;
    cin >> d;
    for(int rej = 0; rej < d; rej++){
      string s;
      cin >> s;
      rejects.insert(make_pair(s[0], s[1]));
      rejects.insert(make_pair(s[1], s[0]));
    }


    int n;
    cin >> n;

    string eval;
    cin >> eval;

    vector<char> output;
    for(int i = 0; i < eval.size(); i++){
      //first 'add' it
      letteruses.insert(make_pair(eval[i], 0)).first->second++;
      output.push_back(eval[i]);

      char addedlet = eval[i];

      //then combine
      int end = output.size();
      if(end >=2){
        map<pair<char, char>, char>::iterator repi =
          replacements.find(orderedPair(output[end-1], output[end-2]));
        if(repi != replacements.end()){
          char a = output[end-1];
          char b = output[end-2];
          output.pop_back();
          output.pop_back();
          output.push_back(repi->second);
          letteruses[a]--;
          letteruses[b]--;
          letteruses.insert(make_pair(repi->second, 0)).first->second++;
          addedlet=repi->second;
        }
      }

      
      //then clear if required
      pair<multimap<char, char>::iterator,
          multimap<char, char>::iterator> range;

      range = rejects.equal_range(addedlet);
      letteruses[addedlet]--;
      multimap<char, char>::iterator current;
      for(current = range.first; current != range.second; ++current){
        if(letteruses.insert(make_pair(current->second, 0)).first->second > 0){
          letteruses.clear();
          output.clear();
          letteruses[addedlet]=-1;
        }
      }
      letteruses[addedlet]++;

    }
    
    cout << "Case #" << trial << ": [";

    if(output.size() > 0){
      cout << output[0];
      for(int i = 1; i < output.size(); i++){
        cout << ", " << output[i];
      }
    }

    cout << "]" << endl;

  }
}
