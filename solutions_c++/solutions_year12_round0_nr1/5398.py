#include <cstdio> 
#include <vector> 
#include <iostream> 
#include <string> 
#include <sstream> 
#include <algorithm> 
#include <map> 
#include <cmath> 
#include <cstdlib> 
using namespace std; 
#define sz size() 
#define pb push_back 
#define all(a) a.begin(),a.end() 
#define FOR(i,s,n) for(int i=s;i<n;++i) 

#define FORZ(i,n) FOR(i,0,n) 
#define inf (INT_MAX/2) 
typedef pair<int,int> ii; 
map<int,vector<int> > dp;
char trans[300];

void generate_tr_table() { 
trans['y'] = 'a';
trans['n'] = 'b';
trans['f'] = 'c';
trans['i'] = 'd';
trans['c'] = 'e';
trans['w'] = 'f';
trans['l'] = 'g';
trans['b'] = 'h';
trans['k'] = 'i';
trans['u'] = 'j';
trans['o'] = 'k';
trans['m'] = 'l';
trans['x'] = 'm';
trans['s'] = 'n';
trans['e'] = 'o';
trans['v'] = 'p';
trans['z'] = 'q';
trans['p'] = 'r';
trans['d'] = 's';
trans['r'] = 't';
trans['j'] = 'u';
trans['g'] = 'v';
trans['t'] = 'w';
trans['a'] = 'y';
trans['h'] = 'x';
trans['q'] = 'z';
}

void translate(string& googlerese) {
	FORZ(i,googlerese.length())
	  if(googlerese[i] != ' ')
	    googlerese[i] = trans[googlerese[i]];
}

int main() {
  generate_tr_table();
  string line;
  int t,c; 
  scanf("%d\n", &t);
  FOR(c,1,t+1) { 
    getline(cin, line);
    translate(line);
    cout << "Case #" << c << ": " << line;
    if( c != t)
      cout << endl;
  }
}
