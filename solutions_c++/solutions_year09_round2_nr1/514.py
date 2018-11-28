#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <sstream>
#include <set>
#define f(i, n) for(int i = 0; i < n; i++)
#define s(n) scanf("%d", &n)
#define sc(n) scanf("%s", &n)
#define fill(a, v) memset(a, v, sizeof a)
#define inf (int)1e9
using namespace std;

int node, parent;
double w[110];
string name[110];
vector <int> v[110];
int stack[1100], ptr;
map <string, int> m;

double getd(string s)
{
         int len = s.length();
         double wt = 0;
         int p = 0;
         //stack[ptr++] = parent;
         while(s[p] > '9' || s[p] < '0') p++;
         wt += s[p++] - 48; p++;
         double div = 10;
         while(s[p] >= '0' && s[p] <= '9') {wt += (s[p] - '0') / div; div *= 10; p++;}
         return wt;
}

string getn(string s)
{
       int len = s.length(), i = 0;
       for(i = 0; i < len; i++) if(isalpha(s[i])) break;
       if(i == len) return "";
       
       int p = 0;
       while(isalpha(s[i + p])) p++;
       
       return s.substr(i, p);
}

main()
{
	int t, zz = 1;
	s(t);
	while(t--)
	{
         m.clear();
         f(i, 110) v[i].clear();
         parent = node = ptr = 0;
         
         int l;
         string s;
         s(l); l--; getline(cin, s);
         getline(cin, s);
         w[node] = getd(s);
         name[node++] = getn(s);
         stack[++ptr] = 0;
         
         while(l--)
         {
              getline(cin, s);
              int len = s.length();
              bool bb = false;
              f(i, len) if(isdigit(s[i])) {bb = true; break;}
              if(!bb) { ptr--; continue;}
              
              do
              {
                      parent = stack[ptr--];
              }while(v[parent].size() > 1);
              
              v[parent].push_back(node);
              w[node] = getd(s);
              name[node] = getn(s);
              
              stack[++ptr] = parent;
              if(s[len - 1] != ')') stack[++ptr] = node;
              node++;
         }
         
         //f(i, node) cout << w[i] << " " << name[i] << endl; cout << endl;
         //f(i, node){cout << i << " : "; f(j, v[i].size()) cout << v[i][j] << " "; cout << endl;} cout << endl;
         
         int no; s(no);
         int n;
         string prop[110];
         printf("Case #%d:\n", zz++);
         while(no--)
         {
               cin >> s >> n;
               f(i, n) cin >> prop[i];
               
               double ans = 1;
               int cur = 0;
               while(1)
               {
                    ans *= w[cur];
                    if(!v[cur].size()) break;
                    bool xx = false;
                    f(i, n)
                         if(name[cur] == prop[i]) 
                         {
                                cur = v[cur][0];
                                xx = true;
                                break;
                         }
                    if(!xx) cur = v[cur][1];
               }
               printf("%.7lf\n", ans);
         }
    }
}
