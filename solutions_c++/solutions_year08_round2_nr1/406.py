#include <iostream>
#include <vector>

using namespace std;

typedef unsigned long long ull;

int main(){
  int Casos;
  cin >> Casos;
  for (int c=1; c<=Casos; ++c){
    cout << "Case #"<<c<<": ";
    int n;
    ull a, b, c, d, x, y, m;
    cin >> n >> a >> b >> c >> d >> x >> y >> m;
    vector<pair<ull, ull> > p;
    p.push_back(make_pair(x, y));
    for (int i = 1; i<n; ++i){
      x = (((a%m) * (x%m)) % m + (b % m)) % m;
      y = (((c%m) * (y%m)) % m + (d % m)) % m;
      p.push_back(make_pair(x, y));
    }
    int r = 0;
    for (int i=0; i<n; ++i){
      for (int j=i+1; j<n; ++j){
        for (int k=j+1; k<n; ++k){
          if ( ((p[i].first + p[j].first + p[k].first) % 3 == 0) &&
               ( (p[i].second + p[j].second + p[k].second) % 3 == 0) ){
            ++r;
          }

        }
      }
    }
    cout << r << endl;
  }
  return 0;
}
