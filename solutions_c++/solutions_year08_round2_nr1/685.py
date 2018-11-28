#include <map>
#include <vector>
#include <list>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

#define FOR(x,N) for(large x=0; x<N; x++)

#define GET(x) cin >> x;
#define GETt(T,x) T x; cin >> x;

#define SORT(A) sort(A.begin(), A.end());
#define RSORT(A,T) sort(A.begin(), A.end(), greater<T>());

#define DEBUG_TRACE(x) cout << #x "=" << x << endl;
//#define DEBUG_TRACE(x)

typedef long long large;
typedef long double real;

struct Node {large x; large y;};

int main()
{
  GETt(int, prob);

  FOR(iii,prob)
  {
    GETt(large, n);
    GETt(large, A);
    GETt(large, B);
    GETt(large, C);
    GETt(large, D);
    GETt(large, x0);
    GETt(large, y0);
    GETt(large, M);

    vector<Node> trees;

    Node t;
    t.x=x0;
    t.y=y0;
    trees.push_back(t);

    FOR(zzz,n-1)
    {
      t.x = (A*t.x+B)%M;
      t.y = (C*t.y+D)%M;
      trees.push_back(t);
    }

    large count=0;
    FOR(zzz,n-2)
    {
      for(int ww=zzz+1; ww<n-1; ww++)
      {
        for(int dd=ww+1; dd<n; dd++)
        {
	  if( (trees[zzz].x+trees[ww].x+trees[dd].x)%3 == 0 &&
	      (trees[zzz].y+trees[ww].y+trees[dd].y)%3 == 0 )
            count++;
        }
      }
    }

    cout << "Case #" << iii+1 << ": " << count << endl;
  }

  return 0;
}
