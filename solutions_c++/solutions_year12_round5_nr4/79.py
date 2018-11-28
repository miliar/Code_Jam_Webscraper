#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>

using namespace std;

string leet="48cd3f9h1jklmn0pqr57uvwxyz";

int main() {
  int T;
  scanf("%d", &T);
  for (int tc=1; tc<=T; tc++) {
    int k;
    string S;
    scanf("%d", &k);
    cin>>S;
    set<string>se;
    for (int i=1; i<(int)S.size(); i++) {
      string x=S.substr(i-1, 2), y;
      se.insert(x);
      y=x;
      y[0]=leet[y[0]-'a'];
      se.insert(y);
      y[1]=leet[y[1]-'a'];
      se.insert(y);
      y=x;
      y[1]=leet[y[1]-'a'];
      se.insert(y);
    }

    int a[2][256];
    for (int i=0; i<256; i++) a[0][i]=a[1][i]=0;

    for (__typeof(se.end())it=se.begin(); it!=se.end(); it++) {
      a[0][(*it)[0]]++;
      a[1][(*it)[1]]++;
    }

    int ans=2*se.size();
    for (int i=0; i<256; i++) {
      int m=min(a[0][i], a[1][i]);
      ans-=m;
      a[0][i]-=m;
      a[1][i]-=m;
    }
    ans++;
    for (int i=0; i<256; i++) {
      if (a[0][i]!=0) {
	ans--;
	break;
      }
    }

    printf("Case #%d: %d\n", tc, ans);
  }

  return 0;
}
