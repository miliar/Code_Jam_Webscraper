#include <iostream>
#include <math.h>
#include <list>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <memory.h>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <stdio.h>
#include <assert.h>

using namespace std;
#define SET(a,n) memset(a,n,sizeof(a));
#define FOR(a,b,c) for(int a=b;a<c;++a)
#define GN(a) scanf("%d",&a)

typedef long long int LL;
typedef vector<int> VI;

using namespace std;
LL notes[10002];

int main()
{
    freopen("i.txt","r",stdin);
    freopen("o.txt","w",stdout);

    int t;
    cin>>t;
    FOR(test,1,t+1)
    {
        int N;
        LL L,H;
        cin>>N>>L>>H;
        FOR(i,0,N)cin>>notes[i];
        bool found = 0;
        LL ans;
        for(LL i = L; i<H+1; ++i)
        {
            bool valid = 1;
            FOR(j,0,N)
            {
                if(notes[j]<=i)
                {
                    if(i%notes[j]!=0)
                    {
                        valid = 0;
                        break;
                    }
                }
                else
                {
                    if(notes[j]%i!=0)
                    {
                        valid = 0;
                        break;
                    }
                }
            }
            if(valid)
            {
                ans = i;
                found = 1;
                break;
            }
        }
        cout<<"Case #"<<test<<": ";
        if(!found)cout<<"NO"<<endl;
        else cout<<ans<<endl;
    }
    return 0;
}

