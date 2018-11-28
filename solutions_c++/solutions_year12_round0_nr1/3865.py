#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <string>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
//---------- macros ----------
#define fp(i,a,b) for(int i=a; i<b; i++)
#define fm(i,a,b) for(int i=a; i>b; i--)

using namespace std;

int main()
{
  map <char, char> replace; string str[3], ostr[3];
   str[0]=   "ejp mysljylc kd kxveddknmc re jsicpdrysi";
   ostr[0] = "our language is impossible to understand";
   str[1] =  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
   ostr[1] = "there are twenty six factorial possibilities";
   str[2] =   "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    ostr[2] = "so it is okay if you want to just give up";
  fp(i,0,3)

    fp(j,0,str[i].length())
     {  replace[str[i][j]] = ostr[i][j];  //replace[ostr[i][j]] = str[i][j];
     }
     //cout << replace.size() << endl;
     replace['q'] = 'z';
     replace['z'] = 'q';
     
     int T = 0;  string s;
     cin >> T; getline(cin,s);
     int kase = 1;
     while(kase <=T)
     {
     getline(cin,s); int  n = s.length();
     fp(i,0,n) s[i] = replace[s[i]];
     cout  << "Case #"<<kase << ": "<< s << endl;
     kase++;
     }
//-----------------------------
   //cout << endl;
   //system("pause");
   return 0;
}
