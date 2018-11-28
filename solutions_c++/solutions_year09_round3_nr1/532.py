#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
#include <sstream>
#include <fstream>
#include <set>

using namespace std;

#define FR(i, n) for (int i=0; i<n; i++)
#define FOR(i, a, b) for (int i=a; i<=b; i++)

#define MAXN 100000

typedef long long LL;

string st;
int n;
int c[100];
int so[100];
int done[100];

void dien(char ch, int x) {
     FR(i, n)
       if (!done[i] && st[i]==ch)
       {
         done[i] = 1;
         so[i] = x;
       }
}

void process() {
     memset(c, 0, sizeof(c));
     memset(done, 0, sizeof(done));
     memset(so, 0xff, sizeof(so));
     
     n = (int)st.size();
     FR(i, n)
           if ('0'<=st[i] && st[i]<='9') c[st[i]-'0']++;
           else c[st[i]-'a'+10]++;
     int cnt = 0;
     FR(i, 50) if (c[i]>0) cnt++;
     
     int dem = 0;
     FR(i, n) {           
           if (done[i]) continue;
           dem++;           
           if (dem==1) dien(st[i], 1);
           else
             if (dem==2) dien(st[i], 0);
             else dien(st[i], dem-1);
     }           
     
     cnt = max(cnt, 2);
     /*
     FR(i, n) {
           cout << so[i] << "-";
           if (so[i]<0) cout << "Shit!";
     }
     cout << " ";*/
     
     
     
     
     LL ret = 0;
     FR(i, n) ret=ret*cnt + so[i];
     cout << ret << endl;
}

int main() {
    freopen("a.in", "rt", stdin);
    freopen("a.out", "wt", stdout);
    

    
    
    int ntest;
    cin >> ntest;
    
    string temp;
    getline(cin, temp);    
    FR(u, ntest) {
          getline(cin, st);
          cout << "Case #" << u+1<<": ";
          process();
    }    
    
    return 0;
}

