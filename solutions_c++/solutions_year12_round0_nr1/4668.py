#include<cstdio>
#include<string>
#include<iostream>

using namespace std;

string conv(const string &t){
  string ret;
  for(int i = 0; i < (int)t.length(); ++i){
    switch(t[i]){
    case 'a': ret += 'y'; break;
    case 'b': ret += 'h'; break;
    case 'c': ret += 'e'; break;
    case 'd': ret += 's'; break;
    case 'e': ret += 'o'; break;
    case 'f': ret += 'c'; break;
    case 'g': ret += 'v'; break;
    case 'h': ret += 'x'; break;
    case 'i': ret += 'd'; break;
    case 'j': ret += 'u'; break;
    case 'k': ret += 'i'; break;
    case 'l': ret += 'g'; break;
    case 'm': ret += 'l'; break;
    case 'n': ret += 'b'; break;
    case 'o': ret += 'k'; break;
    case 'p': ret += 'r'; break;
    case 'q': ret += 'z'; break;
    case 'r': ret += 't'; break;
    case 's': ret += 'n'; break;
    case 't': ret += 'w'; break;
    case 'u': ret += 'j'; break;
    case 'v': ret += 'p'; break;
    case 'w': ret += 'f'; break;
    case 'x': ret += 'm'; break;
    case 'y': ret += 'a'; break;
    case 'z': ret += 'q'; break;
    default: ret += t[i];
    }
  }
  return ret;
}

int main()
{
  int T;
  cin >> T;
  string s;
  getline(cin,s);
  for(int tc=1;tc<=T;++tc){
    getline(cin,s);
    cout << "Case #" << tc << ": " << conv(s) << endl;
  }
  return 0;
}
