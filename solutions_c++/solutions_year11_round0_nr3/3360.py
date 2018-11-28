#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<cstring>
using namespace std;

int add(int a, int b)
{
    int res=0, c,d,e,i;
    for(i=0;i<20;i++)
    {
        c=a&(1<<i);
        d=b&(1<<i);
        e=c^d;
        if(e)
            res|=(1<<i);

    }
    return res;
}
int cal(vector <int> &val)
{
    int s=val.size(), sum=0,i;
    for(i=0;i<s;i++)
        sum=add(sum,val[i]);
    return sum;
}
int main()
{
    int T,tt,N,i,j,ss,pp,ans=-1;
    vector <int> sean, arr, pat;
    //cout<<add(7,9)<<endl;
    //cout<<add(5,4);
    cin>>T;
    for(tt=1;tt<=T;tt++)
    {
        cin>>N;
        arr.clear();
        arr.resize(N);
        ans=-1;
        for(i=0;i<N;i++)
            cin>>arr[i];
        for(i=0;i< (1<<N) ; i++)
        {
            sean.clear(), pat.clear();
            for(j=0;j<N;j++)
            {
                if(i&(1<<j))
                    sean.push_back(arr[j]);
                else pat.push_back(arr[j]);
            }
            ss=cal(sean);
            pp=cal(pat);
            if(ss==pp && sean.size() && pat.size())
            {
                int alu=0;
                for(int k=0;k<sean.size();k++)
                    alu+=sean[k];
                ans=max(ans,alu);
            }
        }
        cout<<"Case #"<<tt<<": ";
        if(ans==-1)
            cout<<"NO\n";
        else cout<<ans<<endl;

    }
    return 0;
}
