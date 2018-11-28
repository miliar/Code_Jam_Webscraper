#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

int T;
char c[100];
bool flag;
typedef long long LL;
LL sqr(int x) {return (LL)x*x;}
void dfs(int x,LL sum) {
     if (flag) return ;
     if (!c[x]) {
        if (sqr(int(sqrt(sum)+1e-8))==sum) {
           for (int i=0;i<x;++i) cout<<c[i];
        cout<<"\n";
        flag=true;
        }
        return ;
     }
     if (c[x]!='?') dfs(x+1,sum*2+c[x]-'0');
     else {c[x]='0';dfs(x+1,sum*2);c[x]='1';dfs(x+1,sum*2+1);c[x]='?';}
}
int main(){
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    cin>>T;
    for (int t=1;t<=T;++t) {
        cout<<"Case #"<<t<<": ";
        gets(c);
        if (strlen(c)==0) gets(c);
        flag=false;
        dfs(0,0);
    }
    return 0;
}
