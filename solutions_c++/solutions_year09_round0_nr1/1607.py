#include <iostream>
#include <string>
#include <vector>
using namespace std;

int numPattern(vector<string> dic)
{
  string str;
  vector<string> pattern;
  vector<string>::iterator p;

  getline(cin, str);
  int  j = 0;
  bool dete = true;
  for( int i = 0 ; i < str.size() ; ++i ) {
    char c = str[i];
    //cout << "[" << c << "]" << dic.size() << "\n";
    switch( c ) {
    case '(':
      dete = false;
      break;
    case ')':
      dic = pattern;
      pattern.clear();
      ++j;
      dete = true;
      break;
    default:
      if( dete ) {
        for( p = dic.begin() ; p != dic.end() ; ++p ) {
          if( (*p)[j] == c ) {
            //cout << i << "," << j << "," << *p << "\n";
            pattern.push_back(*p);
          }
        }
        dic = pattern;
        pattern.clear();
        ++j;
      } else {
        for( p = dic.begin() ; p != dic.end() ; ++p ) {
          if( (*p)[j] == c ) {
            //cout << i << "," << j << "," << *p << "\n";
            pattern.push_back(*p);
          }
        }
      }
    }
  }
  return dic.size();
}

int main(void)
{
  int l, d, n;
  cin >> l >> d >> n;

  string str;
  vector<string> dic;
  getline(cin, str);
  while( d-- ) {
    getline(cin, str);
    dic.push_back(str);
  };
  vector<string>::iterator p;

  for( int ca = 1 ; ca <= n ; ++ca ) {
    
    cout << "Case #" << ca << ": " << numPattern(dic) << "\n";
  }
  return 0;
}
