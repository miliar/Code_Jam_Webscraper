#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<set>
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
int a,b;
string c;

string trans(int v)
{
    string st="";
    while(v)
    {
        st=(char)(v%10)+st;
        v/=10;
    }
    return st;
}

int calc(int v)
{
    int i,q=0;
    set<string> pc;
    string st,s1,s2,s3;
    st=trans(v);
    if(st.sz==1)return 0;
    if(st[0]=='0')return 0;
    FOR(i,0,(int)st.sz-2)
    {
        s1=st.substr(0,i+1);
        s2=st.substr(i+1,st.sz-i-1);
        s3=s2+s1;
        if(s3[0]!='0'&&s3>st&&s3<=c)
        {
            if(!pc.count(s3))
            {
                q++;
                pc.insert(s3);
            }
        }
    }
    return q;
}

int main()
{
    int i,T,j;
    LL ans=0;
    freopen("sr.in","r",stdin);
    freopen("sc.out","w",stdout);
    scanf("%d",&T);
    FOR(i,1,T)
    {
        scanf("%d%d",&a,&b);
        c=trans(b);
        ans=0;
        FOR(j,a,b-1)ans+=calc(j);
        printf("Case #%d: ",i);
        cout<<ans<<endl;
    }
}
