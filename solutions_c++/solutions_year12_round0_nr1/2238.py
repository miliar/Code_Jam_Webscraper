
#include <bitset>
#include <cassert>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <map>
#include <unordered_set>
#include <set>
#include <vector>
#include <sstream>
#include <fstream>
using namespace std;

typedef unsigned int uint;

#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define foreach(i,c) for(decltype((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(x,c) ((c).find(x) != (c).end()) 
#define cpresent(x,c) (std::find(all(c),x) != (c).end()) 
#define mapget(x,c,d) (present(x,c)?(c).find(x)->second:d)
#define cmapget(x,c,d) (cpresent(x,c)?(c).find(x)->second:d)
#define iter(x) decltype((x).begin())

int main()
{
  uint n;
  cin >> n;
  string tmp;
  getline(cin, tmp);

  ifstream in("data");
  assert(in.good());
  map<char, char> translate;

  translate['y'] = 'a';
  translate['q'] = 'z';
  translate['e'] = 'o';

  translate['z'] = 'q';

  for(uint i = 0; i < 3; i++){
    string from,to;
    getline(in, from);
    getline(in, to);
    assert(from.size() == to.size());

    for(uint j = 0; j < from.size(); j++){
      if(from[j] != ' '){
        if(present(from[j], translate))
          assert(to[j] == translate[from[j]]);
        translate[from[j]] = to[j];
      }else
        assert(to[j] == ' ');
    }
  }

  //set<char> def;
  //foreach(iter, translate)
    //def.insert(iter->second);
  //foreach(iter, def)
    //cout << *iter << endl;

  for(uint i = 1; i <= n; i++){
    string ret;
    
    getline(cin, ret);
    foreach(iter, ret){
      if(*iter != ' ')
        *iter = translate[*iter];
    }

    cout << "Case #" << i << ": " << ret << endl;
  }

  assert(cin.good());
  return EXIT_SUCCESS;
}

