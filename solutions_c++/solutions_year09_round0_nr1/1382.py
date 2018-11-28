
//Written by Alex Hamed Ahmadi - alex@hamedahmadi.com

#include <iostream>
#include <cstring>
#include <string>

using namespace std;

const int maxd=6000;
const int maxl=20;

int l;
int d;
int n;

char a[maxd][maxl];

bool good[maxl][256];

int main() {
  cin>>l>>d>>n;
  for (int i=0;i<d;i++)
    cin>>a[i];

  for (int i=0;i<n;i++) {
    memset(good, 0, sizeof good);
    string s;
    cin>>s;
    int k=0;
    for (int j=0;j<l;j++) {
      if (s[k]=='(') {
	k++;
	while (s[k]!=')') good[j][s[k++]]=1;
	k++;
      } else {
	good[j][s[k++]]=1;
      }
    }

    int cnt=0;
    for (int j=0;j<d;j++) {
      for (int k=0;k<l;k++)
	if (!good[k][a[j][k]]) goto next;
	cnt++;
      next:;
    }
    cout<<"Case #"<<i+1<<": "<<cnt<<endl;
  }

  return 0;
}
