#include <iostream>
#include <vector>
#include <string>

using namespace std;


int main() {
  int N;
  cin >> N;
  for( int i = 0 ;  i < N  ; i++ ) {
    int P, Q;
    cin >> P >> Q;

    vector<int> q;
    for( int j = 0 ; j < Q ; j++ ) {
      int index;
      cin >> index;
      q.push_back(index);
    }


    long long mx = LONG_LONG_MAX;
    do {
#if 0
      cerr << "P:";
      for(size_t i = 0 ; i <q.size() ; i++ ) {
        cerr << q[i] << ",";
      }
      cerr <<endl;
#endif
      vector<int> cells(P,1);

      int coin = 0;
      for(size_t j = 0 ; j < q.size() ; j++ ) {
        //cerr << "#" << q[j] << ":" << cells[q[j]] << endl;
        int index = q[j]-1;
        cells[index] = 0;
        for(int k=index-1; 0 <= k ; k-- ) {
          if(!cells[k]) {
            break;
          }
          coin++;
        }
        //cerr << "a" << coin << std::endl;
        for( int k = index+1; k < P ; k++ ) {
          if(!cells[k]) {
            break;
          }
          coin++;
        }
        //cerr << coin << std::endl;
      }

      if( coin < mx ) { mx = coin; }
    } while(next_permutation(q.begin(),q.end()));
    cout << "Case #" << i+1 << ": " << mx << endl;
  }
}
