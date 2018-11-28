#include <fstream>
#include <set>
#include <string>
using namespace std;

void add(string &s, set<string> &folders) {
  string f;
  for(int i=1; i<s.size(); i++) {
    if(s[i]=='/') folders.insert(f); 
	f+=s[i];
  }
  folders.insert(f);
}

int main() {
  ifstream cin("input.txt");
  ofstream cout("output.txt");
  int t;
  cin >> t;
  for(int tc=1; tc<=t; tc++) {
    int n,m;
	cin >> n >> m;
    string s;
	set<string> folders;
	for(int i=0; i<n; i++) {
	  cin >> s;
	  add(s, folders);
	}
	for(int i=0; i<m; i++) {
	  cin >> s;
	  add(s, folders);
	}
	cout << "Case #" << tc << ": " << folders.size()-n << endl; 
  }
  return 0;
}