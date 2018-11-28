/*
ID: Plagapong
LANG: C++
TASK: password
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
#include<set>
#define INF 999999999

using namespace std;
char s[5005];
int k;

set<char> edges[128];
int in[128], out[128];

char leetify(char x) {
  switch (x) {
  case 'o': return '0';
  case 'i': return '1';
  case 'e': return '3';
  case 'a': return '4';
  case 's': return '5';
  case 't': return '7';
  case 'b': return '8';
  case 'g': return '9';
  }
  return x;
}

void preprocess() {
  // Preprocess
  
}

void clearVars() {
  // Clear variables
  for (int i = 0; i < 5005; i++) s[i] = 0;
  for (int i = 0; i < 128; i++) {
    edges[i].clear();
    in[i] = out[i] = 0;
  }
}

void process() {
  // Code here!
  int garbage = scanf("%d", &k);
  garbage = scanf("%s", s);
  int i = 0;
  while(s[i+1]) {
    // Map s[i] to s[i+1]
    char leet1 = leetify(s[i]);
    char leet2 = leetify(s[i+1]);
    edges[s[i]].insert(s[i+1]);
    edges[s[i]].insert(leet2);
    edges[leet1].insert(s[i+1]);
    edges[leet1].insert(leet2);
    i++;
  }
  int e = 0;
  set<char>::iterator itr;
  for (int i = 0; i < 128; i++) {
    for (itr = edges[i].begin(); itr != edges[i].end(); itr++) {
      out[i]++; in[*itr]++; e++;
    }
  }
  int fixme = 0;
  for (int i = 0; i < 128; i++) {
    if (in[i] || out[i]) {
      //printf("%c %d %d\n", i, in[i], out[i]);
      if (in[i] > out[i]) fixme += (in[i] - out[i]);
    }
  }
  if (!fixme) {
    printf("%d", e+1);
  } else {
    printf("%d", (fixme - 1) + e+1);
  }
  
}

int main() {
  preprocess();
  int times;
  cin >> times;
  for (int i = 1; i <= times; i++) {
	cout << "Case #" << i << ": ";
	clearVars();
	process();
	cout << endl;
  }
  return 0;
}
