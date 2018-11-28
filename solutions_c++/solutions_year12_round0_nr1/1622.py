#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<vector>
using namespace std;
#define rep(i,n) for(i=0;i<n;i++)
#define FOR(i,j,k) for(i=j;i<=k;i++)
#define FORD(i,j,k) for(i=j;i>=k;i--)
#define met(i,j) memset(i,j,sizeof(i))
#define PB push_back
#define sz size()
#define oo 0x7fffffff
#define Abs(a) (a>0?a:-(a))
typedef long long LL;
typedef unsigned long long ULL;

int main()
{
    freopen("sr.in","r",stdin);
    freopen("sc.out","w",stdout);
    int i,j,n;
    string st,d="yhesocvxduiglbkrztnwjpfmaq";
    cin>>n;getchar();
    FOR(j,1,n)
    {
        getline(cin,st);
        printf("Case #%d: ",j);
        rep(i,(int)st.sz)if(st[i]==' ')cout<<" ";else cout<<d[st[i]-'a'];
        cout<<endl;
    }
}
