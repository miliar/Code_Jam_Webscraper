#include <iostream>
#include <vector>
using namespace std;

int tens[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};

int count_digits(int A) {
  int digits = 0;
  while(A > 0) {
	A /= 10;
	digits++;
  }
  return digits;
}

int rotate(int n, int digits) {
  return (n % 10) * tens[digits-1] + (n / 10);
}

int pairs(int A, int B) {
  int digits = count_digits(A);
  int p = 0;
  vector<int> dups;
  for(int n=A;n<=B;n++) {
	dups.clear();
	int m = n;
	for(int r=0;r<digits-1;r++) {
	  m = rotate(m, digits);
	  bool is_dup = false;
	  for(int d=0;d<dups.size();d++) {
		if(dups[d] == m) {
		  is_dup = true;
		  break;
		}
	  }
	  if(!is_dup && n < m && m <= B) {
		dups.push_back(m);
		p++;
	  }
	};
  }
  return p;
}

int main()
{
  int T;
  cin >> T;
  for(int C=1;C<=T;C++) {
	int A, B;
	cin >> A >> B;
	int p = pairs(A, B);
	cout << "Case #" << C << ": " << p << "\n";
  }
  return 0;
}
