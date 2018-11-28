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

    freopen("A-large(2).in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,x=0,r,c,cnt,ans,f;
    cin>>t;
    while(t--)
    {
        x++;
        cin>>r>>c;
        string str;
        f=0;
        vector <string> pat;
        for(int i=0;i<r;i++)
        {
            cin>>str;
            pat.push_back(str);
        }
        cnt=0;
        int tot=0;
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                if(pat[i][j]=='#') tot++;
                if(pat[i][j]=='#'&&pat[i][j+1]=='#'&&j<c)
                {
                    if(i+1<r&&pat[i+1][j]=='#'&&pat[i+1][j+1]=='#')
                    {
                        pat[i][j]='/';
                        pat[i][j+1]='\\';
                        pat[i+1][j]='\\';
                        pat[i+1][j+1]='/';
                        cnt++;
                        tot+=3;
                    }
                }
            }
        }
        if(tot!=cnt*4) { cout<<"Case #"<<x<<": "; cout<<"\nImpossible\n"; continue;}
        cout<<"Case #"<<x<<": ";
        cout<<"\n";
        for(int i=0;i<r;i++) cout<<pat[i]<<endl;

    }

    return 0;
}

