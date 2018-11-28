#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#define REP(i,a,b) for(int i=a;i<b;++i)
#define rep(i,n) REP(i,0,n)
const int n=4;
using namespace std;
void func(vector<string>& a)
{
    rep(i,n) REP(j,i+1,n) swap(a[i][j],a[j][i]);
    rep(i,n) reverse(a[i].begin(),a[i].end());
}
bool func2(vector<string> a, char t)
{
    rep(i,n) rep(j,n) if(a[i][j]=='T') a[i][j]=t;
    rep(i,n) if (count(a[i].begin(),a[i].end(),t)==n) return true;
    int c=0; rep(i,n) if (a[i][i]==t) c++;
    return c==n;
}
string func3(vector<string> a)
{
    if (func2(a,'O')) return "O won";
    if (func2(a,'X')) return "X won";
    func(a);
    if (func2(a,'O')) return "O won";
    if (func2(a,'X')) return "X won";
    rep(i,n) rep(j,n) if(a[i][j]=='.') return "Game has not completed";
    return "Draw";
}
int main()
{
    int T; cin>>T;
    for(int t=1;t<=T;++t) {
        vector<string> a(n);
        rep(i,n) cin>>a[i];
        cout<<"Case #"<<t<<": "<<func3(a)<<endl;
    }
    return 0;
}
