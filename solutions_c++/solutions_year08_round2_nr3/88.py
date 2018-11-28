#include <iostream>
#include <vector>

#define For(i,n) for(int i=0;i<(n);++i)

using namespace std;

void debug(vector<int> &v, vector<int> &v2, vector<int> &good) {
  For(i,v.size()) cerr << v[i] << " ";
  cerr << endl;
  For(i,v2.size()) cerr << v2[i] << " ";
  cerr << endl;
  For(i,good.size()) cerr << good[i] << " ";
  cerr << endl;
  cerr << endl;
}


int main() {

  int n;
  cin >> n;
  For(c,n) {
    cout << "Case #" << (c+1) << ": ";
    
    int K, Q;
    cin >> K >> Q;
    vector<int> good(K);

    vector<int> v[2];
    v[0].resize(K, 0);
    v[1].resize(K, 0);

    For(i, K) v[0][i] = i;

    int count = 0;
    int j = 0;
    int deck = 0;
    int ot = 0;
    For(i, K) {
      while (j<v[deck].size() and count<i) {
	//debug(v[deck], v[(deck+1)%2], good);
	v[(deck+1)%2][ot] = v[deck][j];
	++j;
	++ot;
	++count;
      }
      if (j == v[deck].size()) {
	++deck;
	deck%=2;
	v[deck].resize(ot);
	ot = 0;
	j = 0;
	--i;
      }
      else {
	good[v[deck][j]] = i;
	++j;
	count = 0;
      }
    }

    For(i, Q) {
      int d;
      cin >> d;
      cout << (good[d-1]+1);
      if (i<Q-1) cout << " ";
    }
    cout << endl;
  }
}
