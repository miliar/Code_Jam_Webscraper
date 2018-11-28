#include<cstdio>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<bitset>
#include<iostream>
#include<sstream>
#include<queue>
#include<cassert>
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
using namespace std;

typedef vector<int> VI;
typedef VI::iterator VIit;
typedef pair<int,int> PII;
typedef map<int,int> MII;
typedef MII::iterator MIIit;
typedef set<int> SI;
typedef SI::iterator SIit;
typedef long long LL;
const int DX[8]={1,-1,0,0,1,1,-1,-1};
const int DY[8]={0,0,1,-1,1,-1,1,-1};
const int intmax=0x7fffffff;
const int mod=1000000007;
int n,s,p;
vector<int> f;
int main()
{
    freopen("f3.in","r",stdin);
    freopen("f3.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int mt=1;mt<=t;mt++)
    {
        int cnt1=0,cnt2=0;
        scanf("%d%d%d",&n,&s,&p);
        for(int ii=0;ii<n;ii++)
        {
            int nn=0;
            scanf("%d",&nn);
            bool sur=0,saf=0;
            for(int i=0;i<=10;i++)
            for(int j=0;j<=10;j++)
            {
                int k=nn-i-j;
                if (k<0||k>10) continue;
                f.clear();
                f.PB(i);f.PB(j);f.PB(k);
                int ret=max(i,j);
                ret=max(ret,k);
                if (ret<p) continue;
                sort(f.begin(),f.end());
                if (f[2]-f[0]>2) continue;
                if (f[2]-f[0]==2) sur=1;
                if (f[2]-f[0]<2) saf=1;
            }
            if (saf) cnt1++;
            if (!saf&&sur) cnt2++;
        }
        int ans=cnt1+min(cnt2,s);
        printf("Case #%d: %d\n",mt,ans);
    }
}
