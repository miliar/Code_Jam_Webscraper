#include <iostream>
#include <string>
#include <sstream>
#include <cstdlib>
using namespace std;


string ConvertToString(int);

int main() {
   string num;
   int cases, count;
   int m, n;
   int output_count;
   cin >> count;
   for (cases = 1; cases <= count; cases++){
      output_count = 0;
      

      cin >> n >> m;
      for (int j = n; j <= m; j++) {
         num = ConvertToString(j);
         int orginal = atoi(num.c_str());

         for (int i = 0; i < num.size() - 1; i++){
            num.push_back(num[0]);
            num.erase(num.begin());
            int int_num = atoi(num.c_str());
            if (orginal == int_num) continue;
            if (n <= int_num && int_num <= m) {
               output_count++;
               //cout << orginal << " " << int_num << endl;
            }
         }
      }
      cout << "Case #" << cases << ": " << output_count/2 << endl;
   }
   return 0;
}

string ConvertToString(int value) {
  stringstream ss;
  ss << value;
  return ss.str();
}
