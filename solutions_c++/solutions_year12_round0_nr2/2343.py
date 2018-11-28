
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

  for(uint i = 1; i <= n; i++){
    int ret = 0;
    uint N, S, p;

    cin >> N >> S >> p;
    
    uint anyway_ok, could_be_ok;
    anyway_ok = could_be_ok = 0;
    for(uint j = 0; j < N; j++){
      uint tmp;
      cin >> tmp;
      
      uint notsurprising_res;
      if(tmp % 3)
        notsurprising_res = tmp/3 + 1;
      else
        notsurprising_res = tmp/3;

      if(notsurprising_res >= p)
        ++anyway_ok;
      else if(tmp % 3 != 1){
        if(p == notsurprising_res+1 &&
            tmp >= 2)
          ++could_be_ok;
      }
    }
    ret = anyway_ok + min(could_be_ok, S);

    cout << "Case #" << i << ": " << ret << endl;
  }

  assert(cin.good());
  return EXIT_SUCCESS;
}

