#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int freq;
string welcome = "welcome to code jam";

void search(string &word, int index, int strpos);

int main() {
   string word;
   int tests;
   cin >> tests;
   int index = 0;
   getline(cin, word);

   for (int i = 0; i < tests; i++) {
      freq = 0;
      //cin >> word;
      getline(cin, word);
      search(word, 0, 0);
      cout << "Case #" << i+1 << ": ";
      printf("%4.4d", freq);
      cout << endl;
   }
}

void search(string &word, int index, int strpos) {
   if (index == welcome.length()) {
      freq = (freq + 1) % 10000;
      return;
   }
   int stridx = word.find(welcome[index], strpos);
   while (stridx != string::npos) {
      search(word, index+1, stridx);
      stridx = word.find(welcome[index], stridx+1);
   }
   
   if (stridx != string::npos)
      search(word, index+1, stridx);
}
