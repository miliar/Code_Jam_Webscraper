#include <iostream>
#include <string>
#include <map>
#include <cmath>
using namespace std;


int calculate (string& num) {
   map<char, int> M;
   int sum = 0;
   unsigned int i = 1, max = 2;
   
   M[num[0]] = 1;
   
   while (M.find(num[i]) != M.end()) {
      i++;
   }
   
   M[num[i]] = 0;
   
   for (i = 2; i < num.size(); i++) {
      if (M.find(num[i]) == M.end()) {
         M[num[i]] = max;
         max++;
      }
   }
   
   for (i = 0; i < num.size(); i++) {
      sum += (M[num[i]])*pow(double(max), double(num.size()-i-1));
   }
   
   return sum;
   
}


int main(int argc, char *argv[]) {
	int c;
   string num;
   
   cin >> c;
   
   for (int i = 1; i <= c; i++) {
      cin >> num;
      cout << "Case #" << i << ": " << calculate(num) << endl;
   }
   
   
	return 0;
}

