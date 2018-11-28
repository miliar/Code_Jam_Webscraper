#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

bool happy(int base, int n) {
   int sum = 0;

   if (base == 2)
      return true;
   if (base == 4)
      return true;

   if (base == 3) {
      while (n != 1 && n != 2 && n != 5 && n != 8 && n != 4) {
	 sum = 0;
	 while (n > 0) {
	    sum += (n % base) * (n % base);
	    n /= base;
	 }
	 n = sum;
      }
   }
   
   else if (base == 5) {
      while (n != 1 && n != 4 && n != 13 && n != 18 && n != 16 && n != 10) {
	 sum = 0;
	 while (n > 0) {
	    sum += (n % base) * (n % base);
	    n /= base;
	 }
	 n = sum;
      }
   }
   
   else if (base == 6) {
      //      while (n != 1 && n != 20 && n != 13 && n != 5 && n != 25 && n != 17 && n != 29 && n != 
      while (n != 1 && n != 5 && n != 29) {
	 sum = 0;
	 while (n > 0) {
	    sum += (n % base) * (n % base);
	    n /= base;
	 }
	 n = sum;
      }
   }

   else if (base == 7) {
      while (n != 1 && n != 2 && n != 25 && n != 10 && n != 17 && n != 45 && n != 32) {
	 sum = 0;
	 while (n > 0) {
	    sum += (n % base) * (n % base);
	    n /= base;
	 }
	 n = sum;
      }
   }
 
   else if (base == 8) {
      while (n != 1 && n != 4 && n != 5 && n != 26 && n != 20 && n != 52) {
	 sum = 0;
	 while (n > 0) {
	    sum += (n % base) * (n % base);
	    n /= base;
	 }
	 n = sum;
      }
   }
 
   else if (base == 9) {
      while (n != 1 && n != 50 && n != 53 && n != 41 && n != 68) {
	 sum = 0;
	 while (n > 0) {
	    sum += (n % base) * (n % base);
	    n /= base;
	 }
	 n = sum;
      }
   }
 
   else if (base == 10) {
      while (n > 100) {
	 sum = 0; 
	 while (n > 0) {
	    sum += (n % 10) * (n % 10);
	    n /= 10;
	 }
	 n = sum;
      }
      if (n == 1 || n == 7 || n == 10 || n == 13 || n == 19 || n == 23 || n == 28 || n == 31 || n == 32 || n == 44 || n == 49 || n == 68 || n == 70 || n == 79 || n == 82 || n == 86 || n == 91 || n == 94 || n == 97) {
	 return true;
      } else return false;
   }
 
   if (n == 1)
      return true;
   else
      return false;
   
}

int main() {
   int T;
   cin >> T;
   string basestr;
   istringstream bss;
   vector<int> bases;
   int base;
   getline(cin, basestr);

   for (int i = 0; i < T; i++) {
      getline(cin, basestr);
      bss.str(basestr);
      bss >> base;
      while (!bss.fail()) {
	 bases.push_back(base);
	 bss >> base;
      }
      
      int happynum = 1;
      bool ishappy = false;
      do {
	 happynum++;
	 ishappy = true;
	 for (int j = 0; j < bases.size(); j++) {
	    if (!happy(bases[j], happynum))
	       ishappy = false;
	    //cout << "(" << bases[j] << " " << happynum << ")" << endl;
	 }
      } while (!ishappy);
      
      cout << "Case #" << i+1 << ": " << happynum << endl;
      bases.clear();
      bss.clear();
   }

   
}
