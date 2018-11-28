#include <iostream>
#include <string>
#include <map>

#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

map<char,char> charMap;
void doMapping(string a, string b)
{
   for(int i = 0; i < a.size(); i++) {
      if(a[i] == ' ') continue;
      if(charMap.find(a[i])==charMap.end()) {
         charMap[a[i]]=b[i];
        // charMap[b[i]]=a[i];
      }
   }
}
void prepareMap()
{
   doMapping("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
   doMapping("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
   doMapping("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
   doMapping("z","q");
   doMapping("a","y");
   doMapping("o","e");
   doMapping("q","z");
}
int main()
{
   freopen("A-small-attempt4.in","r",stdin);
   freopen("A-small-attempt4.text","w",stdout);
   prepareMap();
//for(char c='a';c<='z';c++) cout<<charMap[c]<<endl;
   int T;

   cin>>T;
 cin.ignore();

   for(int tc = 1; tc <= T; tc++) {

      string str;
      getline(cin,str);

      cout<<"Case #"<<tc<<": ";
      for(int i= 0; i < str.size(); i++) {
         char ch = str[i];
         if(str[i] != ' ') ch = charMap[str[i]];
         cout<<ch;
      }
      cout<<endl;

   }

   return 0;
}
