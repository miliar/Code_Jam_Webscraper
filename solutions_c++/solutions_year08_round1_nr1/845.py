#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>
#include <iterator>

using namespace std;
using namespace __gnu_cxx;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define fr(i,n) for(int i=0; i<(n); ++i)
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())

int main(){
  int cases;

  cin >> cases;

  fr(cas,cases) {
    printf("Case #%d: ", cas+1);
    vi a1, a2;
    int n;
    cin >> n;

    fr(j, n) {
      int tmp;
      cin >> tmp;
      a1.push_back( tmp );
    }
    fr(j, n) {
      int tmp;
      cin >> tmp;
      a2.push_back( tmp );
    }
    sort(all(a1));
    sort(a2.rbegin(), a2.rend());

    cout << inner_product(all(a1), a2.begin(), 0);
  
    printf("\n");
  }

  
  return 0;
}
  
