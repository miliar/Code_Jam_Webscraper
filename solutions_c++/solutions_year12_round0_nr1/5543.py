/**
 * Speaking in Tongues
 * Author: Sohail Munir Khan (sohail.munir@gmail.com)
 **/
#include <iostream>
#include <map>
#include <string>
using namespace std;

map<char, char> cMappings;

string convert(string input) {
  string output = "";
  for (unsigned int i = 0; i < input.length(); ++i) {
	output += cMappings.find(input[i])->second;
  }
  return output;
}

int main() {

  cMappings.insert ( pair<char,char>(' ',' ') );
  cMappings.insert ( pair<char,char>('a','y') );
  cMappings.insert ( pair<char,char>('b','h') );
  cMappings.insert ( pair<char,char>('c','e') );
  cMappings.insert ( pair<char,char>('d','s') );
  cMappings.insert ( pair<char,char>('e','o') );
  cMappings.insert ( pair<char,char>('f','c') );
  cMappings.insert ( pair<char,char>('g','v') );
  cMappings.insert ( pair<char,char>('h','x') );
  cMappings.insert ( pair<char,char>('i','d') );
  cMappings.insert ( pair<char,char>('j','u') );
  cMappings.insert ( pair<char,char>('k','i') );
  cMappings.insert ( pair<char,char>('l','g') );
  cMappings.insert ( pair<char,char>('m','l') );
  cMappings.insert ( pair<char,char>('n','b') );
  cMappings.insert ( pair<char,char>('o','k') );
  cMappings.insert ( pair<char,char>('p','r') );
  cMappings.insert ( pair<char,char>('q','z') );
  cMappings.insert ( pair<char,char>('r','t') );
  cMappings.insert ( pair<char,char>('s','n') );
  cMappings.insert ( pair<char,char>('t','w') );
  cMappings.insert ( pair<char,char>('u','j') );
  cMappings.insert ( pair<char,char>('v','p') );
  cMappings.insert ( pair<char,char>('w','f') );
  cMappings.insert ( pair<char,char>('x','m') );
  cMappings.insert ( pair<char,char>('y','a') );
  cMappings.insert ( pair<char,char>('z','q') );

  // Process Googlerese.
  int T;
  cin >> T;
  string g;
  getline(cin,g);
  for (int prob = 1; prob <= T; prob++) {	
	getline(cin,g);
	cout << "Case #" << prob << ": " << convert(g) << endl;
  }

  return 0;
}
