#include <iostream>

using namespace std;

int main(){

  int t, a, b, n, n2, m, count=0;
  int p,q,r,s;
  cin >> t;
  for (int i=0; i<t; i++) {
    count = 0;
    cin >> a >> b;
    for (n = a; n <= b; n++) {
      n2 = n;
      while (n2!=0) {
	p = n2%10;
	n2 = n2/10;
	q = n2%10;
	n2 = n2/10;
	if (n2 == 0) break;
	r = n2%10;
	n2 = n2/10;
	if(n2 == 0) break;
	s = n2%10;
	n2 = s/10;
      }
      if (10 <=a && a < 100) {
	if ((n <  p*10 + q) && (p*10 + q <= b)) count++;
      }
      else if (100 <=a && a < 1000) {
	if ((n < q*100 + p*10 + r) && (q*100 + p*10 + r <= b)) count++;
	if ((n < p*100 + r*10 + q) && (p*100 + r*10 + q <= b)) count++;
      }
      
    }
    cout << "Case #" << i+1 << ": "<< count << endl;
  }
 
  return 0;
} 
      
