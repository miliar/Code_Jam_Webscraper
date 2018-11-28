
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

vector<int> to_ints(string str){
  vector<int> ret;
  foreach(iter, str){
    ret.pb(*iter - '0');
  }
  return ret;
}

bool incr(vector<int>& to_incr){

  for(int i = to_incr.size()-1; i >= 0; i--){
    if(to_incr[i] != 9){
      ++to_incr[i];
      return true;
    }else
      to_incr[i] = 0;
  }

  return false;
}

bool lessthan(const vector<int>& v1,
              const vector<int>& v2)
{
  assert(v1.size() == v2.size());
  for(uint i = 0; i < v1.size(); i++){
    if(v1[i] < v2[i])
      return true;
    else if(v1[i] > v2[i])
      return false;
  }
  return false;
}

void rotate(vector<int>& to_rotate,
            unsigned int n){
  assert(n >= 1);
  assert(n < to_rotate.size());
  
  vector<int> ret;
  for(uint i = to_rotate.size()-n; i < to_rotate.size(); i++)
    ret.pb(to_rotate[i]);
  for(uint i = 0; i < to_rotate.size()-n; i++)
    ret.pb(to_rotate[i]);
  to_rotate = ret;
}

int main()
{
  uint n;
  cin >> n;

  for(uint i = 1; i <= n; i++){
    string sA, sB;
    cin >> sA >> sB;
    assert(sA.size() == sB.size());

    vector<int> A,B;
    A = to_ints(sA);
    B = to_ints(sB);
    assert(sA.size() == sB.size());

    unsigned long long ret = 0;
    vector<int> n = A;

    do
    {
      assert(n[0] != 0);
      multiset<pair<vector<int>, vector<int> > > nms;

      for(uint i = 1; i < n.size(); i++){
        vector<int> m = n;
        rotate(m, i);

        if(m[0] != 0){
          if(lessthan(n, m) &&
              (lessthan(m, B) ||
                m == B)){
            pair<vector<int>,vector<int> > nm;
            nm = make_pair(n,m);
            if(!present(nm, nms)){
              nms.insert(make_pair(n,m));
              ret += 1;
            }
          }
        }
      }
      
      if(!incr(n))
        break;
    }while(!lessthan(B, n));
    
    cout << "Case #" << i << ": " << ret << endl;
  }

  assert(cin.good());
  return EXIT_SUCCESS;
}

