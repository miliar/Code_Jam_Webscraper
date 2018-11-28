#define forr(x,y,z)for(int (x)=(y);(x)<(z);(x)++)
#include <string>
#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int main() {

  long long tcase, n, angka[1005];
  cin >> tcase;
  forr(i,1,tcase+1) {
    cin >> n;
    long long hasil = 0,min=10000000,total = 0;
    forr(j,0,n) {
      cin >> angka[j];
      hasil ^= angka[j];
      if(min > angka[j]) min = angka[j];
      total += angka[j];
    }

    if(hasil == 0) {
      cout << "Case #" << i << ": " << total-min << "\n";
    } else {
      cout << "Case #" << i << ": NO\n";
    }
  }

  return 0;
}

