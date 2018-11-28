#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <set>
#include <map>
#include <queue>

using namespace std;

#define pb push_back
#define FOR(i,a,b) for(int i=a; i<=b; ++i)
#define REP(i,b) for(int i=0; i<b; i++)


typedef long long ll;
typedef vector<int> vint;
typedef pair<int,int> pii;

string a[111],b[111]; int s;

int men(string &s1,string &s2,int p)
{
    p++; 
    while (s1[p]!='/' && s2[p]!='/' && s1[p]==s2[p]) p++;
    if (s1[p]<s2[p]) return 1; else
    if (s1[p]>s2[p]) return -1; else
    return 0;
}

void mak(int l1,int r1,int l2,int r2,int p)
{
    //cout<<l1<<' '<<r1<<' '<<l2<<' '<<r2<<' '<<p<<endl;
    int i1,i2;
    while (l2<=r2 && b[l2].length()<=p+1) l2++;
    while (l1<=r1 && a[l1].length()<=p+1) l1++;
    while (l2<=r2)
    {
        while (l1<=r1 && men(a[l1],b[l2],p)==1) l1++;
        i2=l2;
        while (i2<r2 && men(b[i2],b[i2+1],p)==0) i2++;        
        s++;
        int p1=p+1; while (b[l2][p1]!='/') p1++;
        
        if (l1<=r1 && men(a[l1],b[l2],p)==0)
        {
            s--;
            i1=l1;
            while (i1<r1 && men(a[i1],a[i1+1],p)==0) i1++;
            mak(l1,i1,l2,i2,p1);
            l1=i1+1;
        }
        else mak(l1,l1-1,l2,i2,p1);
        l2=i2+1;
    }
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t,n,m;
	scanf("%d",&t);
	FOR(r,1,t)
	{
        printf("Case #%d: ",r);
        scanf("%d%d",&n,&m);
        FOR(i,0,n-1) { cin>>a[i]; a[i]+='/'; }
        FOR(i,0,m-1) { cin>>b[i]; b[i]+='/'; }
        sort(a,a+n); sort(b,b+m);
        //FOR(i,0,n-1) cout<<a[i]<<endl;
        //cout<<endl;
        //FOR(i,0,m-1) cout<<b[i]<<endl;
        
        s=0; mak(0,n-1,0,m-1,0);
        printf("%d\n",s);        
    }
	return 0;
}
