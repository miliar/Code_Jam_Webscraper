#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>

using namespace std;

bool isUgly(__int64 d)
{
    if(d==0)
        return true;
    if(d<0)
        d=0-d;
    if(d%2==0||d%3==0||d%5==0||d%7==0)
        return true;
    else
        return false;
}

int countUgly(__int64 cnt,__int64 d,int dl)
{
    int ans=0;
    if(isUgly(cnt+d))
        ans++;
    if(dl<=1)
        return ans;

    __int64 j;
    __int64 i=1;
    for(int k=1;k<dl;k++)
        i*=10;
    i-=1;
    int k=0;
    for(;i>0;i/=10)
    {
        /*if(i>d)
            continue;*/
        j=i+1;
        k++;
        ans += countUgly( cnt+d/j,d%j,dl-k);
        ans += countUgly( 0-cnt-d/j,d%j,dl-k);
    }
    return ans;
}

int main()
{
    int N;
    __int64 d;
    int ans;
    string str;

    cin>>N;
    for(int i=1;i<=N;i++)
    { 
        cin>>str;
        d=_atoi64(str.data());
        ans = countUgly(0,d,str.length());

        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}