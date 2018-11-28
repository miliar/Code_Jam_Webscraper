#include <iostream>
#include <string>
using namespace std;

char dic[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};


int main()
{
     int t;
     cin >> t;
     cin.get();
     for (int i=1; i<=t; i++) {
          string str;
          getline(cin, str);
          for (int j=0; j<str.size(); j++) {
               if (str[j] != ' ') {
                    str[j] = dic[str[j] - 'a'];
               }
          }
          cout << "Case #" << i << ": " << str << endl;
     }
     return 0;
}
