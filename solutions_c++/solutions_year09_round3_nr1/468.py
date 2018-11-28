#include <string>
#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>
#include <stdio.h>
using namespace std;

int trans[1000000],cnt=2;

int main()
{
    freopen("d:\\in.txt","r",stdin);
    freopen("d:\\out.txt","w",stdout);
    int T,i,cas;
    string s;
    
    cin>>T;
    for (cas=1;cas<=T;cas++)
    {
        cin>>s;
        memset(trans,0xff,sizeof(trans));
        cnt=2;
        trans[s[0]]=1;
        for (i=1;i<s.length();i++)
        {
            if (s[i]!=s[0])
            {
                trans[s[i]]=0;
                break;
            }
        }
        for (i=1;i<s.length();i++)
        {
            if (trans[s[i]]==-1)
            {
                trans[s[i]]=cnt;
                cnt++;
            }
        }
        long long res=0;
        for (i=0;i<s.length();i++)
        {
            res*=cnt;
            res+=trans[s[i]];
        }
        cout<<"Case #"<<cas<<": "<<res<<endl;
    }
    return 0;
}
