#include <functional>
#include <algorithm>
#include <utility>
#include <cassert>
#include <cmath>
#include <ctime>

#include <numeric>
#include <iomanip>
#include <complex>
#include <float.h>
#include <cfloat>

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <cstdio>

#include <cstring>
#include <string>

#include <iterator>
#include <vector>
#include <bitset>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

#define foreach(it, v, type) for( type::iterator it = v.begin(); it != v.end() ; it++)
#define forn(i, st, en) for(int i = (int)(st); i <= (int)(en); i++)
#define ford(i, en, st) for(int i = (int)(en); i >= (int)(st); i--)
#define zero(a, w) memset(a, w, sizeof(a))
#define all(a) a.begin(), a.end()
#define sz(a) a.size()

#define msg(x) cout << #x << " = " << x << endl;

bool war[110][110];
char change[110][110];

int main() {
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);

 int kTest;
 cin >> kTest;

 for(int indexTest = 1; indexTest <= kTest; ++indexTest) {

  memset(war, 0, sizeof(war));
  memset(change, -1, sizeof(change));

  int tempLen;
  string tempStr;
  tempStr = "";

  cin >> tempLen;
  for(int i = 0; i < tempLen; ++i) {
   string temp;
   cin >> temp;
   tempStr += temp;
  }
  // if(tempLen > 0) cin >> tempStr;

  for(int i = 0; i < tempLen; ++i) {
   change[tempStr[i * 3]][tempStr[i * 3 + 1]] = tempStr[i * 3 + 2];
   change[tempStr[i * 3 + 1]][tempStr[i * 3]] = tempStr[i * 3 + 2];
  }

  tempStr = "";
  cin >> tempLen;
  for(int i = 0; i < tempLen; ++i) {
   string temp;
   cin >> temp;
   tempStr += temp;
  }
  //if(tempLen > 0) cin >> tempStr;

  for(int i = 0; i < tempLen; ++i) {
   war[tempStr[i * 2]][tempStr[i * 2 + 1]] = true;
   war[tempStr[i * 2 + 1]][tempStr[i * 2]] = true;
  }

  int Len;
  string Str;

  Str = "";
  cin >> Len;
  if(Len > 0) cin >> Str;

  vector<char> Result;
  Result.clear();

  for(int i = 0; i < Len; ++i) {
   Result.push_back(Str[i]);

   if(Result.size() >= 2 && change[Result[Result.size() - 1]][Result[Result.size() - 2]] != -1) {
    char tempChar = change[Result[Result.size() - 1]][Result[Result.size() - 2]];
    Result.pop_back();
    Result.pop_back();
    Result.push_back(tempChar);
   }

   for(int j = 0; j < Result.size() - 1; ++j)
    if(war[Result[j]][Result.back()]) {
     Result.clear();
     break;
    }
  }

  cout << "Case #" << indexTest << ": ";    
  cout << "[";

  if(Result.size() > 0)
   cout << Result[0];

  for(int i = 1; i < Result.size(); ++i)
   cout << ", " << Result[i];

  cout << "]" << endl;

 }


 return 0;
}

