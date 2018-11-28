#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class TR {
public:
  int dep;
  int arr;
  bool isA;

  TR(int dep, int arr, bool isA)
    : dep(dep), arr(arr), isA(isA) {}

  bool operator<(const TR& lhr) const {
    return lhr.dep > dep;
  }
};

typedef vector<TR> Table;

void fetchTrains(Table &Q, TR &tmp, int T){
  while(!Q.empty()) {
    if (tmp.isA) {
      for(int i=0;i<(int)Q.size();i++) {
        if (!Q[i].isA && Q[i].dep >= tmp.arr+T) {
          tmp = Q[i];
          Table::iterator it = Q.begin()+i;
          Q.erase(it);
          break;
        }
      }
      if (tmp.isA) break;
    }

    if (!tmp.isA) {
      for(int i=0;i<(int)Q.size();i++) {
        if (Q[i].isA && Q[i].dep >= tmp.arr+T) {
          tmp = Q[i];
          Table::iterator it = Q.begin()+i;
          Q.erase(it);
          break;
        }
      }
      if (!tmp.isA) break;
    }

  }
}

int main()
{
  int N; cin>>N;
  for(int i=1;i<=N;i++) {

    Table Q;
    int T, NA, NB; cin>>T>>NA>>NB;
    int a,b,c,d, dep, arr;
    cin.ignore();
    for(int j=0;j<NA;j++) {
      scanf("%d:%d %d:%d", &a, &b, &c, &d);
      dep = a*60+b;
      arr = c*60+d;
      Q.push_back( TR(dep,arr,true) );
    }

    for(int j=0;j<NB;j++) {
      scanf("%d:%d %d:%d", &a, &b, &c, &d);
      dep = a*60+b;
      arr = c*60+d;
      Q.push_back( TR(dep,arr,false) );
    }

    int A=0,B=0;
    while(!Q.empty()) {
      sort(Q.begin(), Q.end());
      TR tmp = Q[0]; Q.erase(Q.begin());

      if (tmp.isA) A++; else B++;
      fetchTrains(Q, tmp, T);
    }

    cout << "Case #" << i << ": " << A << " " << B << endl;
  }
}
