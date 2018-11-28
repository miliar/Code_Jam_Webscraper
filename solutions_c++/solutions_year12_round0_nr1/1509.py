#include <iostream>
#include <string>
#include <cstdlib>
#include <map>
#include <vector>
#include <algorithm>
#include <fstream>
#include <ctime>

using namespace std;

string freqmap1 = "etaoinshrdlcumwfgypbvkjxqz";
string freqmap2 = "isteoaunrlpgybfwdkxjvcmhqz";

class Entry {
 public:
   Entry(char a, int i): _a(a), _i(i) {
   }
   char _a;
   int _i;
   bool operator < (const Entry& e) const {
      return _i > e._i;
   }
};

void change(map<char, char>& m, map<char, char>& rm, char m1, char m2);
void randomMap(map<char, char>& m, map<char, char>& rm, string m1, string m2);


int main(int args, char** argc) {
   srand(time(NULL));
   int n = 0;
   string buf;
   ifstream file(argc[1]);
   getline(file, buf);
   n = atoi(buf.c_str());
   string* content = new string[n];
   int freq[26] = {0};
   for (int i = 0; i < n; ++i) {
      getline(file, content[i]);
      for (int j = 0; j < content[i].size(); ++j) {
         if (content[i][j] - 'a' >= 0) {
            ++freq[content[i][j] - 'a'];
         }
      }
   }
/*
   for (int i = 0; i < n; ++i) {
      cerr << content[i] << endl;
      for (int j = 0; j < 26; ++j) {
         cerr << (char)('a' + j) << ":" << freq[j] << " ";
      }
      cerr << endl;
   }
*/

   vector<Entry> data;
   for (int i = 0; i < 26; ++i) {
      data.push_back(Entry(i + 'a', freq[i]));
   }
   sort(data.begin(), data.end());
   map<char, char> result;
   map<char, char> rev;
   for (int i = 0; i < 26; ++i) {
      result[data[i]._a] = freqmap2[i];
      rev[freqmap2[i]] = data[i]._a;
   }

   // know data
   change(result, rev, 'a', 'y');
   change(result, rev, 'c', 'e');
   change(result, rev, 'd', 's');
   change(result, rev, 'e', 'o');
   change(result, rev, 'f', 'c');
   change(result, rev, 'g', 'v');
   change(result, rev, 'h', 'x');
   change(result, rev, 'i', 'd');
   change(result, rev, 'j', 'u');
   change(result, rev, 'k', 'i');
   change(result, rev, 'l', 'g');
   change(result, rev, 'm', 'l');
   change(result, rev, 'n', 'b');
   change(result, rev, 'p', 'r');
   change(result, rev, 'q', 'z');
   change(result, rev, 'r', 't');
   change(result, rev, 's', 'n');
   change(result, rev, 't', 'w');
   change(result, rev, 'u', 'j');
   change(result, rev, 'v', 'p');
   change(result, rev, 'w', 'f');
   change(result, rev, 'x', 'm');
   change(result, rev, 'y', 'a');

   change(result, rev, 'o', 'k');
   change(result, rev, 'b', 'h');
   string rand1 = "bz";
   string rand2 = "hq";
//   randomMap(result, rev, rand1, rand2);
//   change(result, rev, 'q', 'q');

   for (int i = 0; i < n; ++i) {
      cout << "Case #" << i + 1 << ": ";
      for (int j = 0; j < content[i].size(); ++j) {
         if (content[i][j] == ' ') {
            cout << " ";
         } else {
            cout << result[content[i][j]];
         }
      }
      cout << endl;
   }
/*
   while (getline(cin, buf)) {
      if (buf[0] == '$') {
         randomMap(result, rev, rand1, rand2);
      } else {
         char t1 = rev[buf[0]];
         char t2 = rev[buf[1]];
         result[t1] = buf[1];
         result[t2] = buf[0];
         rev[buf[0]] = t2;
         rev[buf[1]] = t1;
      }
      for (int i = 0; i < n; ++i) {
         cout << "Case #" << i + 1 << ": ";
         for (int j = 0; j < content[i].size(); ++j) {
            if (content[i][j] == ' ') {
               cout << " ";
            } else {
               cout << result[content[i][j]];
            }
         }
      cout << endl;
      }
   }
   for (int i = 0; i < 26; ++i) {
      cout << result[data[i]._a];
   }
   cout << endl;
*/
   return 0;
}


void change(map<char, char>& m, map<char, char>& rm, char m1, char m2) {
   char t1 = rm[m2];
   char t2 = m[m1];
   m[m1] = m2;
   m[t1] = t2;
   rm[m2] = m1;
   rm[t2] = t1;
}

void randomMap(map<char, char>& m, map<char, char>& rm, string m1, string m2) {
   string tm1, tm2;
   bool tmp1[m1.size()], tmp2[m2.size()];
   for (int i = 0; i < m1.size(); ++i) {
      tmp1[i] = false;
   }
   for (int i = 0; i < m2.size(); ++i) {
      tmp2[i] = false;
   }

   while (1) {
      bool br = true;
      for (int i = 0; i < m1.size(); ++i) {
         br &= tmp1[i];
      }
      if (br) {
         break;
      }
      int r = rand() % m1.size();
      if (!tmp1[r]) {
         tm1 += m1[r];
         tmp1[r] = true;
      }
   }
   while (1) {
      bool br = true;
      for (int i = 0; i < m2.size(); ++i) {
         br &= tmp2[i];
      }
      if (br) {
         break;
      }
      int r = rand() % m2.size();
      if (!tmp2[r]) {
         tm2 += m2[r];
         tmp2[r] = true;
      }
   }
   for (int i = 0; i < m1.size(); ++i) {
      m[tm1[i]] = tm2[i];
      rm[tm2[i]] = tm1[i];
   }
}

