#include <string>
#include <iostream>
using namespace std;

static const char map[26] = {'y', 'h', 'e', 's', 'o' , 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

static string encode(const string in){
  int len = in.length();
  string buf = "";
  for(int i=0; i<len; i++){
    if(in[i] >= 'a' && in[i] <= 'z')
      buf += map[in[i]-'a'];
    else
      buf += in[i];
  }
  return buf;
}

int main(int argc, char** argv){
  int cases;
  cin >> cases;
  getc(stdin); //chomp first \n
  string input;
  char c;
  for(int i=0; i<cases; i++){
    input = "";
    while((c = getc(stdin)) != '\n')
      input += c; 
    printf("Case #%i: %s\n", i+1, encode(input).c_str());
  }
}