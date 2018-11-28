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

int comb[123][123];
int opp[123][123];
int arr[200],cc;

void adjust()
{
    if(cc>=2)
    {
        if(comb[arr[cc-1]][arr[cc-2]]!=-1)
        {
            arr[cc-2]=comb[arr[cc-1]][arr[cc-2]];
            cc--;
        }
        else
        {
            FOR(i,0,cc)FOR(j,i+1,cc)
            {
                if(opp[arr[i]][arr[j]])
                {
                    cc=0;
                    return;
                }
            }
        }
    }
    return;
}

int main()
{
    freopen("i.txt","r",stdin);
    freopen("B-large.txt","w",stdout);
    int t,c,d,n;
    cin>>t;
    FOR(test,1,t+1)
    {
        int p,q,r;
        string str;
        cin>>c;
        SET(comb,-1);
        FOR(i,0,c)
        {
            cin>>str;
            p = str[0];
            q = str[1];
            r = str[2];
            comb[p][q]=comb[q][p]=r;
        }
        cin>>d;
        SET(opp,0);
        FOR(i,0,d)
        {
            cin>>str;
            p = str[0];
            q = str[1];
            opp[p][q]=opp[q][p]=1;
        }
        cin>>n;
        cin>>str;
        cc = 0;
        FOR(i,0,n)
        {
            arr[cc++]=str[i];
            adjust();
        //    FOR(i,0,cc)cout<<(char)arr[i];
          //  cout<<endl;
        }
        cout<<"Case #"<<test<<": [";
        FOR(i,0,cc)
        {
            cout<<(char)arr[i];
            if(i!=cc-1)cout<<", ";
        }
        cout<<"]\n";
    }
    return 0;
}

