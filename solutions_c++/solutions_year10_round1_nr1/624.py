#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iomanip>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
const double EPS = 1e-12;
const double PI = acos(-1.0);
const int INF  = 0x3f3f3f3f; // 1061109567, 1*10^9
const LL LINF = 0x3f3f3f3f3f3f3f3fLL; //4557430888798830399, 4*10^18
#define ST(x,b)  memset(x,b,sizeof(x))
#define SZ(x) ((int)(x).size())
#define forn(i,n) for(__typeof(n) i=0;i<n;i++)
#define forab(i,a,b) for(__typeof(a) i=a;i<b;i++)
#define foreach(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();it++)
template<class T>string toString(T s){ostringstream ost;ost<<s;return ost.str();}
template<class T>LL toLL(T s){stringstream st; st<<s; LL ret; st>>ret; return ret;}
template<class T>int toInt(T s){stringstream st; st<<s; int ret; st>>ret; return ret;}

#define READ_FROM_FILE
const string PROBLEM_NAME = "A";
const string SUB_TYPE = "large";
int n,k;
char g[60][60];
bool canR, canB;
int dr[]={-1,-1,-1,0,0,1,1,1};
int dc[]={1,0,-1,1,-1,1,0,-1};
void change(void){
     while(1){
        bool cha = false;
        forn(i,n)
          forn(j,n-1) 
            if(g[i][j]!='.'&&g[i][j+1]=='.'){
               cha = true;
               g[i][j+1] = g[i][j];
               g[i][j] = '.';
            }
        if(!cha)break;
     }
}
void check(void){
     forn(i,n)
       forn(j,n){
          if(!canR){
             for(int kk=0;kk<8;kk++){
                int cnt = 0;
                int cr = i,cc=j;
                while(1){
                   if(cr<0 || cr>=n)break;
                   if(cc<0||cc>=n)break;
                   if(g[cr][cc]!='R')break;
                   cnt++;
                   if(cnt==k)break;
                   cc+=dc[kk];
                   cr+=dr[kk];
                }
                if(cnt==k){canR=true;}
             }
          }
          if(!canB){
             for(int kk=0;kk<8;kk++){
                int cnt = 0;
                int cr = i,cc=j;
                while(1){
                   if(cr<0 || cr>=n)break;
                   if(cc<0||cc>=n)break;
                   if(g[cr][cc]!='B')break;
                   cnt++;
                   if(cnt==k)break;
                   cc+=dc[kk];cr+=dr[kk];
                }
                if(cnt==k){canB=true;}
             }
          }
       }
}
          
int main(){
    #ifdef READ_FROM_FILE
    freopen((PROBLEM_NAME+"-"+SUB_TYPE+".in").c_str(),"r",stdin);
    freopen("out.txt","w",stdout);
    #endif
    int cas; cin>>cas;
    forn(ca,cas) {
       cin>>n>>k;  ST(g,0);
       forn(i,n) scanf("%s",g[i]); canR=false; canB=false;
       change();
       //forn(i,n)puts(g[i]);
       check();
       cout<<"Case #"<<ca+1<<": "; 
       if(canR&&canB)cout<<"Both"<<endl;
       else if(canR&&!canB)cout<<"Red"<<endl;
       else if(!canR&&canB)cout<<"Blue"<<endl;
       else cout<<"Neither"<<endl;
    }
}

