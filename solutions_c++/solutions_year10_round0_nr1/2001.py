#include <iostream>

using namespace std;

int main() {

  int n;
  cin >> n;

  for (int i=1;i<=n;i++) {

    int nbits;
    int val;

    cin >> nbits >> val;

    bool onoff = false;

    for (int j=0;j<nbits;j++) {

      if (!(val%2)) {
	onoff = true;
	break;
      };

      val = val / 2;

    };

    cout << "Case #" << i << ": ";

    if (onoff) {
      cout << "OFF" << endl;
    } else {
      cout << "ON" << endl;
    };
    
  };

  return 0;

};
