#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

int main()
{

  int n;

  cin >> n;

  for (int c=1;c<=n;c++) {

    set<pair<int,int> > arr;

    int a,b;
    cin >> a >> b;

    int ndigits = 0;

    int t = 1;
    int cc = a;
    while (cc != 0) {
      cc /= 10;
      ndigits++;
      t *= 10;
    }

    for (int i=a;i<=b;i++) {
      for (int j=1;j<=t;j*=10) {
        int nv = (i/j) + (t/j)*(i%j);
        if ((nv >= a) && (nv <= b) && (nv != i)) {
          arr.insert(pair<int,int>(min(i,nv),max(i,nv)));
        }
      }
    }

    cout << "Case #" << c << ": " << arr.size() << endl;
  }

  return 0;

}
