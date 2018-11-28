#include <iostream>
#include <cstring>
#include <string>

#define MAX 40

using namespace std;

int m[MAX][MAX];
int inc[MAX][MAX];
int count[MAX];
int q[150];
int next;

int main() {
  int tt;
  string str;
  int c;
  cin >> tt;
  for (int t = 1; t<=tt;t++) {
    memset(m, -1, sizeof(m));
    memset(inc, 0, sizeof(inc));    
    memset(count, 0, sizeof(count));
    next = 1;
    q[0] = 30;
    cin >> c;
    for (int i = 0; i<c; i++) {
      cin >> str;
      m[str[0]-'A'][str[1]-'A'] = str[2]-'A';
      m[str[1]-'A'][str[0]-'A'] = str[2]-'A';
    }
    cin >> c;
    for (int i = 0; i<c; i++) {
      cin >> str;
      inc[str[0]-'A'][str[1]-'A'] = 1;
      inc[str[1]-'A'][str[0]-'A'] = 1;
    }
    
    cin >> c;
    cin >> str;
    
    for (int i = 0; i<c; i++) {
      q[next++] = str[i]-'A';
      count[q[next-1]]++;
      
      while (m[q[next-1]][q[next-2]]>=0) {
	count[q[next-1]]--;
	count[q[next-2]]--;
	q[next-2] = m[q[next-1]][q[next-2]], next--;
	count[q[next-2]]++;
      }
      for (int i = 0; i<26;i++)
	if (inc[i][q[next-1]] && count[i] && count[q[next-1]]) {
	  next = 1;
	  memset(count, 0, sizeof(count));
	}
    }
    
    cout << "Case #" << t << ": [";
    for (int i = 1; i<next; i++)
      cout << (i>1?", ":"") << (char)(q[i]+'A');
    cout << "]" << endl;
  }
  return 0;
}
