#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define SETMIN(a,b) a = min(a,b)
#define SETMAX(a,b) a = max(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define CLR(x,a) memset(x,a,sizeof(x))
#define BEND(v) v.begin(),v.end()
#define MP make_pair
#define A first
#define B second

typedef unsigned long long int ull;
typedef long double ld;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

   int t,n;
   string str;
    cin>>t;int x=0;
    while(t--)
    {
         vector <double> wp;
        vector< double> owp;
        vector <double> oowp;
        x++;
        cin>>n;
        vector <string> match;
        for(int i=0;i<n;i++)
        {
            cin>>str;
            match.push_back(str);
        }

        for(int i=0;i<n;i++)
        {
            double w=0.0,tot=0.0;
            for(int j=0;j<n;j++)
            {
                if(match[i][j]=='1')w++;
                if(match[i][j]!='.')tot++;

            }
            double wpp=w/tot;
            wp.push_back(wpp);
        }
        for(int i=0;i<n;i++)
        {
            double sum=0;
            int count=0;
            for(int j=0;j<n;j++)
            {if(i==j||match[i][j]=='.')continue;
            double w=0,tot=0;
            count++;
                for(int k=0;k<n;k++)
                {
                    if(k==i)continue;
                    if(match[j][k]=='1')w++;
                    if(match[j][k]!='.')tot++;
                }
                sum+=(w/(tot));
            }
            owp.push_back(sum/count);
        }
        for(int i=0;i<n;i++)
        {
            double sum=0;
            int count=0;
            for(int j=0;j<n;j++)
            {
                if(j==i||match[i][j]=='.')continue;
                sum+=owp[j];count++;
            }
            oowp.push_back(sum/count);
        }
        cout<<"Case #"<<x<<":\n";
        for(int i=0;i<n;i++)
        {
            double ans=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
       cout<<ans<<"\n";
        }
    }
    return 0;
}





