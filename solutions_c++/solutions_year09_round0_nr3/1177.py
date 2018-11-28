#include <iostream>
#include <string>
#include <cstdio>

#define MAX_S 501
#define MAX_P 20
#define MOD 10000
using namespace std;

string p = "welcome to code jam";

int v[MAX_P];

int main() {
  int n;
  string str;
  scanf("%d\n", &n); 
  for (int t=1;t<=n;t++) {
    getline(cin, str);
    memset(v, 0, sizeof(v));
    //cout << str << endl;
    for (size_t i=0;i<str.length();i++)
      for (size_t j=0;j<p.length();j++)
	if (str[i]==p[j]) {
	  if (j==0)
	    v[0]=(v[0]+1)%MOD;
	  else
	    v[j]=(v[j]+v[j-1])%MOD;
	}
    printf("Case #%d: %04d\n", t, v[p.length()-1]);
  }
  return 0;
}
