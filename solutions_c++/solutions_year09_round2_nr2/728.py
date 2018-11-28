#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>

using namespace std;

#define FR(i, n) for (int i=0; i<n; i++)
#define FOR(i, a, b) for (int i=a; i<=b; i++)

typedef long long LL;

LL num;

vector<int> a;
string st;

void output() {
     FR(i, a.size()) cout << a[i];
     cout << endl;
}

void process() {
     a.clear();

     
     
     FR(i, st.size()) a.push_back(st[i]-'0');
     
     
     int n = a.size();
     
     if (next_permutation (a.begin(),a.begin()+n)) {
     } else {
        a.push_back(0);
        sort(a.begin(), a.end());
        for (int i=1; i<a.size(); i++)
          if (a[i]!=0) {
            swap(a[0], a[i]);
            break;
          }   
     }

     
     /*
     
     bool ok = false;
     for (int i=n-2; i>0; i--)
       if (a[i] < a[i+1]) {
          // i can doi
          
          int tmin = 1000;
          int k = -1;
          for (int j=i+1; j<n; j++)
            if (a[j]>a[i]) {
               if (a[j] < tmin) {
                 k = j;
                 tmin = a[j];
               }
            }
          //cout << a[i] << " " << a[k] << endl;
            
          swap(a[i], a[k]);    
          
          sort(a.begin() + i + 1, a.end());     
          ok = true;
          break;
       }
     
     
     if (!ok) {
              a.push_back(0);
        sort(a.begin(), a.end());
        for (int i=1; i<a.size(); i++)
          if (a[i]!=0) {
            swap(a[0], a[i]);
            break;
          }          
     }*/
     
     output();
}

int main() {
    freopen("b.in", "rt", stdin);
    freopen("b.out", "wt", stdout);
    
    int ntest;
    cin >> ntest;
    FR(i, ntest) {
          cin >> st;
          //cout << st << endl;
          cout << "Case #" << i+1 << ": ";
          process();  
          //cout << endl;
    }    
    
    return 0;
}

