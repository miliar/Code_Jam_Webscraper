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

typedef long long LL;

struct dnode {
       double p;
       string f;              
};

dnode tree[10000];
bool dong, mo;
string aname;
int len;
int used[10000];
set<string> features;

double td;
string ts;
int L, n;
bool dautien;

string loai(string s) {
       dong = false;
       mo = false;
       string ret = "";
       FR(i, s.size()) {
             if (s[i]==')') dong = true;
             if (s[i]=='(') mo = true;
             
             if (s[i]!='(' && s[i]!=')')
             ret += s[i];
       }
       
       bool ok = false;
       FR(i, s.size()) if (s[i]!=' ') ok = true;
       
       if (!ok) return "";
       
       return ret;
}

void process() {
     int i = 1;
     double ret = 1;
     
     while (true) {
           ret *= tree[i].p;           
           if (tree[i].f.size()==0) break;           
           if (features.count(tree[i].f) > 0) {
             i=i*2;
           } else i=i*2+1;
     }
     
     printf("%.7f\n", ret);
}

int main() {
    freopen("a.in", "rt", stdin);
    freopen("a.out", "wt", stdout);
    
    int ntest;
    cin >> ntest;
    
    string temp;
    getline(cin, temp);    
    FR(i, ntest) {
          memset(used, 0, sizeof(used));
          cin >> L; getline(cin, temp);
          
          dautien = true;
          cout << "Case #" << i+1 << ":\n";
          
          int id = 1, i = 0;
          while (i<L) {
                getline(cin, temp);i++;                
                temp = loai(temp);
                if (mo) {
                    if (!dautien) id*=2;                
                    dautien = false;
                    istringstream iss(temp);
                    ts = "";
                    iss >> td >> ts;
                    if (used[id]) id++;
                    tree[id].p = td;
                    tree[id].f = ts;
                    used[id]=1;
//                    cout << id << " " << td << " " << ts << endl;
                }
                if (dong) id/=2;
          }    
          
          cin >> n;
          FR(i, n) {
                cin >> aname >> len;
                features.clear();
                FR(j, len) {
                      cin >> temp;
                      features.insert(temp);
                }                
                process();
          }
    }    
    
    return 0;
}

