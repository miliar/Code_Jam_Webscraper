#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
using namespace std;

int next(int x) {
   stringstream ss;
   string num, part, partMax;
   bool flag = false;
   int xx, l;
   char temp;
   
   ss << x;
   ss >> num;
   
   for (int i = 2; i <= num.size() && !flag; i++) {
      part = num.substr(num.size()-i, num.size());
      partMax = part; sort(partMax.begin(), partMax.end()); reverse(partMax.begin(), partMax.end());
      if (part == partMax) continue;
      else {
         for (int j = part.size()-1; j >= 0 && !flag; j--) {
            for (int k = j-1; k >= 0 && !flag; k--) {
               if (part[j] > part[k]) {
                  temp = part[j];
                  part[j] = part[k];
                  part[k] = temp;
                  flag = true;
                  sort(part.begin()+k+1, part.end());  
               }
            }
         }
      }
   }
   if (flag) {   
      num.erase(num.end()-part.size(), num.end());
      num.insert(num.end(), part.begin(), part.end());
   }
   else {
      sort(num.begin(), num.end());
      for (l = 0; l < num.size(); l++) {
         if (num[l] != '0') break;
      }
      if (l>0) {
         num.erase(num.begin(), num.begin()+l);
      }
      
      for (int i = 0; i < l; i++) {
         num.insert(num.begin()+1, '0');
      }
      
      num.insert(num.begin()+1, '0');
   }
   ss.clear();
   ss << num;
   ss >> xx;   
   return xx;
   
   
   
}

int main(int argc, char *argv[]) {
	//*
   int c, x;
   
   cin >> c;
   
   for (int i = 0; i < c; i++) {
      cin >> x;
      cout << "Case #" << i+1 << ": " << next(x) << endl;     
   }
   //*/
     
   
	return 0;
}

