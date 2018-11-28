#include <algorithm>
#include <iostream>
#include <sstream>
#include <cmath>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <vector>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
const double eps = 1e-11;
const double pi = acos(-1.0);
const double inf = 1e17;
#define swap(a,b) {a^=b;b^a=;a^=b;}
#define two(X) (1<<(X))
#define pair <int,int> pii
#define SZ(x) ((int)x.size())
template<class T> T gcd(const T &a,const T &b) {return (b==0)?a:gcd(b,a%b);}
template<class T> T lcm(const T &a,const T &b) {return a*(b/gcd(a,b));}
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }
struct cell{
       char c;
       int a,next;
};
int dx[] = {-1,0,0,1};
int dy[] = {0,-1,1,0};
int T,H,W;
cell maps[100][100];
bool ok(int i,int j){
     if (i>=0 && j>=0 && i<H && j<W) return true;
     return false;
}
int main(){
    int i,j,k,l,x,y,min,tmp;
    char mark,cmark;
    cin>>T;
    for (i=0;i<T;i++){
        mark = 'a';
        cin>>H>>W;
        for (j=0;j<H;j++){
            for (k=0;k<W;k++){
                cin>>maps[j][k].a;
                maps[j][k].next = 0;
                maps[j][k].c = 'A';
            }
        }
        for (j=0;j<H;j++){
            for (k=0;k<W;k++){
                min = maps[j][k].a;
                for (l=0;l<4;l++){
                    x = j + dx[l];
                    y = k + dy[l];
                    if (ok(x,y) && min > maps[x][y].a){
                       maps[j][k].next = l + 1;
                       min = maps[x][y].a;  
                    }
                }
            }
        }
        for (j=0;j<H;j++){
            for (k=0;k<W;k++){
                x = j;
                y = k;
                if (maps[x][y].c == 'A'){
                    while (maps[x][y].next != 0){
                          tmp = maps[x][y].next - 1;
                          x += dx[tmp];
                          y += dy[tmp];
                    }
                    if (maps[x][y].c == 'A'){
                          cmark = mark;
                          mark ++;
                    }else{
                          cmark = maps[x][y].c;
                    }
                    x = j;
                    y = k;
                    while (maps[x][y].next != 0){
                         maps[x][y].c = cmark;
                         tmp = maps[x][y].next - 1;
                         x += dx[tmp];
                         y += dy[tmp];
                    }
                    maps[x][y].c = cmark;
                }
            }
        }
        printf("Case #%d:\n",i+1);
        for (j=0;j<H;j++){
            for (k=0;k<W;k++){
                cout<<maps[j][k].c;
                if (k != W - 1) cout<<" ";
            }
            cout<<endl;
        }              
    }
    return 0;
}
