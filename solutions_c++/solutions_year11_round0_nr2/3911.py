#include <iostream>
#include <string>

using namespace std;

typedef struct pair{
  char one;
  char two;
  char result;
  struct pair *next;
} mpair;
typedef mpair* mypair;


mypair combines, opposed;

char combine(char a, char b) {
  mypair p = combines;
  while(p != NULL) {
    if((p -> one == a && p -> two == b) ||
       (p -> one == b && p -> two == a)) {
      return p -> result;
    }
    p = p -> next;
  }
  return 0;
}

char oppose(char c) {
  mypair p = opposed;
  while(p != NULL) {
    if(p -> one == c) {
      return p -> two;
    } else if (p -> two == c) {
      return p -> one;
    }
    p = p -> next;
  }
  return 0;   
}

string clear(string s, char c) {
  char op = oppose(c);
  if(op && s.find(op) != string::npos) {
    return "";
  }
  return s + c;
}

string update(string s, char c) {
  if(s.length() == 0) {
    s = c;
    return s;
  }
  char d = s[s.length() - 1];
  char co =  combine (c, d);
  if(co) {
    s = s.substr(0, s.length() - 1) + co;
    return s;
  }
  return clear(s, c);
}

int main() {
  int T;
  cin >> T;
  for(int t=1; t<=T; t++) {
    string s = "";
    combines = NULL;
    opposed = NULL;
    mypair p;
    int C, D, N;
    cin >> C;
    for(int i = 0; i < C; i ++) {
      p = new mpair;
      cin >> p->one;
      cin >> p->two;
      cin >> p->result;
      p->next = combines;
      combines = p;
    }
    cin >> D;
    for(int i = 0; i < D; i++) {
      p = new mpair;
      cin >> p->one;
      cin >> p->two;
      p->next = opposed;
      opposed = p;
    }
    cin >> N;
    char c;
    for(int i = 0; i < N; i++) {
      cin >> c;
      s = update(s,c);
    }


    cout << "Case #" << t << ": [";
    if(s.length() > 0) {
      for(int i = 0; i < s.length() - 1; i ++) {
	cout << s[i] << ", ";
      }
      cout << s[s.length() - 1];
    }
    cout << "]" << endl;
  }
  return 0;
}
