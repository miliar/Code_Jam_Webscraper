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

int main()
{
freopen("small-b1.in","r",stdin);
freopen("b1.out","w",stdout);
int t;
cin>>t;
FOR(test,1,t)
{
    int n,s,p;
    cin>>n>>s>>p;
    vector <int> total(n);
    REP(i,n){cin>>total[i];}
    bool check[n];

    memset(check,false,sizeof(check));

    int ans = 0;
    int best[n];

    REP(i,n){
        if (total[i]%3==0)
        best[i] = total[i]/3;
        else
        best[i] = total[i]/3 + 1;

        if (best[i]>=p)
        check[i] = true;
    }


    REP(i,n)
    {


        if (!s)
        break;


        if (!check[i])
        {
            if (total[i]%3==1);
            else
            {
                if (best[i]+1>=p && best[i]!=0)
                {
                    check[i] = true;
                    s--;
                }
            }
        }

    }

    REP(i,n){if (check[i]) ans++;}
    cout<<"Case #"<<test<<": "<<ans<<endl;
}

return 0;
}
