#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main() {
 char rmap[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
 int n;
 ofstream out("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\out.txt");
 cin >> n;

 string str;
 getline(cin, str, '\n');
 for(int i = 0; i < n; i++) {
  getline(cin, str, '\n');
  for(int j = 0; j < str.size(); j++) {
   if(str[j] != ' ') {
    str[j] = rmap[str[j]-'a'];
   }
  }
  out << "Case #" << i+1 << ": " << str << endl;
 }
 return 0;
}
