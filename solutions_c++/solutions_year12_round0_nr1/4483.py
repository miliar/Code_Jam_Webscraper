#include <iostream>
#include <stdio.h>
#include <map>
using namespace std;

map<char, char> mapping;

void build(char *a, char *b) {
   mapping['q'] = 'z';
   while(*a) {
      mapping[*a] = *b;
      a++;
      b++;
   }
}

void decode (int i, string s) {
   cout << "Case #" << i << ": ";
   for(int i = 0; i < s.length(); i++) {
      cout << mapping[s[i]];
   }

   cout << "\n";
}

int main(int argc, char** argv) {
   char buff[512];
   int T;

   build("a zoo", "y qee");
   build("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
   build("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
   build("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");

   scanf("%d\n", &T);
   for(int i = 0; i < T; i++) {
      string s;
      getline(cin, s);
      decode((i+1), s);
   }
}
