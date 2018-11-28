#include<iostream>
#include<string>
using namespace std;

string A = "zyeq ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
string B = "qaoz our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

char trans(char a) {
  for(int i=0; i<A.size(); i++) {
    if(A[i] == a) return B[i];
  }
  return '?';
}

int main() {
  ios_base::sync_with_stdio(false);
  int k;
  cin >> k;
  if(A.size() != B.size()) cerr << "size error!!!" <<endl;
  char buf[105];
  cin.getline(buf,105);
  for(int i=1; i<=k; i++) {
    cin.getline(buf,105);
    string line(buf);
    cout << "Case #"<<i<< ": ";
    for(int j=0; j<line.size(); j++) {
      cout << trans(line[j]);
    }
    cout << endl;
  }
  return 0;
}
