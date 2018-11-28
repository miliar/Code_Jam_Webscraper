#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<cmath>
#include<queue>
#include<cstdio>
#include<set>
#include<map>
#include<cstdlib>
#include<cstring>
#include<stack>

#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define ABS(a) (a>0?a:-a)

#define SZ(a) ((int)a.size())
#define PB(a) push_back(a)
#define ULL unsigned long long
#define LL long long
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define REP(i,n) FOR(i,0,(int)(n-1))

using namespace std;
int num_len;

int rotate(int n)
{
    return (n/10 + (n%10)*(num_len));
}

int main()
{
freopen("large-c.in","r",stdin);
freopen("largec.out","w",stdout);
int t;
cin>>t;

FOR(test,1,t)
{
    int a,b;
    cin>>a>>b;
    int cnt = 0;
    for (num_len=1;a/num_len;num_len*=10,cnt++);
    set<pair<int,int> > s;
    num_len /=10;
    cnt--;

    FOR(i,a,b)
    {
        int temp = i;
        REP(j,cnt)
        {
            temp = rotate(temp);

            if (temp>=a && temp<=b && temp!=i)
            {
                pair<int,int> p;
                p.first = i;
                p.second = temp;
                s.insert(p);
            }
        }
    }

    cout<<"Case #"<<test<<": "<<(s.size()>>1)<<endl;
}

return 0;
}
