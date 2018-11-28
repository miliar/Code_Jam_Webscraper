#include <iostream>
#include <string>
#include <sstream>
using namespace std;

char trans_letter(char c) {
     switch (c) {
            case 'a': return 'y';   
            case 'b': return 'h';
            case 'c': return 'e';
            case 'd': return 's';    
            case 'e': return 'o';        
            case 'f': return 'c';
            case 'g': return 'v';
            case 'h': return 'x';
            case 'i': return 'd';   
            case 'j': return 'u';
            case 'k': return 'i';
            case 'l': return 'g';  
            case 'm': return 'l';        
            case 'n': return 'b';
            case 'o': return 'k';
            case 'p': return 'r';
            case 'q': return 'z';
            case 'r': return 't';
            case 's': return 'n';
            case 't': return 'w';
            case 'u': return 'j';      
            case 'v': return 'p';
            case 'w': return 'f';
            case 'x': return 'm';
            case 'y': return 'a';
            case 'z': return 'q';
            default: break;
     }     
}

string translate(string s) {
  string k = s;
  for (int i=0; i<k.size(); i++) {
      k[i] = trans_letter(k[i]);    
  }
  return k;       
}

int main() {
 int t;
 cin >> t;
 string aux;
 getline(cin,aux);
 for (int i=0; i<t; i++) {
     string s;
     getline(cin,s);
     stringstream ss(s);
     cout << "Case #" << i+1 << ":";
     while (ss >> s) {
         cout << ' ';
         cout << translate(s);  
     }
     cout << endl;
 }   
}
