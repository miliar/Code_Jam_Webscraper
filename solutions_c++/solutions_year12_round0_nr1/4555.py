#include <fstream>
#include <iostream>
#include <cctype>
using namespace std;

int MAP[26];

void set(char from, char to)
{
  MAP[from-'a'] = (to-'a');
}

char map(char from)
{
  if(!isalpha(from)) return from;
  return MAP[from-'a'] + 'a';
}

int main(int argc, char* argv[])
{
  set('a','y');
  set('b','h');
  set('c','e');
  set('d','s');
  set('e','o');
  set('f','c');
  set('g','v');
  set('h','x');
  set('i','d');
  set('j','u');
  set('k','i');
  set('l','g');
  set('m','l');
  set('n','b');
  set('o','k');
  set('p','r');
  set('q','z');
  set('r','t');
  set('s','n');
  set('t','w');
  set('u','j');
  set('v','p');
  set('w','f');
  set('x','m');
  set('y','a');
  set('z','q');

  ifstream in(argv[1]);
  ofstream out("output");

  int T;
  string str;

  in >> T;
  getline(in,str); //gobble up to newline
  

  for(int t = 0;t < T;++t)
  {
    getline(in,str);
    for(int i = 0;i < str.length();++i)
      str[i] = map(str[i]);
    out << "Case #" << (t+1) << ": " << str << endl;
  }

  in.close();
  out.close();

  return 0;
}
