#include<assert.h>
#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>

using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size

typedef long long INT;

#define sf scanf
#define pf printf


int main()
{
    int t;
    sf("%d",&t);
    int kase=1;
    int fam[1000];
    bool flagged[1000];
    int r,k,n;
    while ( t--)
    {
        sf("%d %d %d",&r,&k,&n);
        int i;
        for(i=0;i<n;i++)
            sf("%d",&fam[i]);
        long long total=0;
        for(i=0;i<n;i++)
            total+=fam[i];
        if ( total <=k )
        {
            cout<<"Case #"<<kase<<": "<<(total*r)<<endl;
            kase++;
            co;
        }
        int cur=0;
        fill(flagged,flagged+1000,false);
        long long sum=0;
        while ( flagged[cur] == false && r )
        {
            long long onboard=0;
            flagged[cur] = true;
            while ( onboard < k )
            {
                if ( onboard + fam[cur] > k ) break;
                onboard+=fam[cur];
                sum += fam[cur]; // sum
                cur = (cur+1)%n;
            }
            r--;
        }
        if ( r==0)
        {
            pf("Case #%d: ",kase++);
            cout<<sum<<endl;
            continue;
        }
        else
        {
            long long locsum=0;
            int len=0;
            int start=cur;
            do
            {
                long long onboard=0;
                while ( onboard<k)
                {
                    if( onboard+fam[cur] > k ) break;
                    onboard+=fam[cur];
                    locsum+=fam[cur];
                    cur = (cur+1)%n;
                }
                len++;
            }while ( cur != start);
            long long one=1;
            sum = sum + one*r/len*locsum;
            r = r%len;
            while ( r--)
            {
                int onboard = 0;
                while ( onboard<k)
                {
                    if ( onboard+fam[cur]> k) br;
                    onboard+=fam[cur];
                    sum+=fam[cur];
                    cur = (cur+1)%n;
                }
            }
            pf("Case #%d: ",kase++);
            cout<<sum<<endl;
        }
    }
    return 0;
}
