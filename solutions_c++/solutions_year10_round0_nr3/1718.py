#include<stdio.h>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#define INF 99999999
using namespace std;

vector<long long>arrr,ar,chk;
string str;
map<string,long long>mp;

long long i,j,k,num,sum,ans,R,K,N,remain,pos,test,t,diff,rang,kase;

void convert()
{
    str.clear();
    for(k=0;k<N;k++)
    {
        num = ar[k];
        while(num/10)
        {
            str+=(num%10)+48;
            num/=10;
        }
        str+=num+48;
    }

}

void neew()
{
    chk.clear();
    for(k=j;k<N;k++)chk.push_back(ar[k]);
    for(k=0;k<j;k++)chk.push_back(ar[k]);
    ar.clear();
    ar = chk;
}

int main()
{
    freopen("a.txt","r",stdin);
    freopen("b.txt","w",stdout);
    cin>>test;
    while(test--)
    {
        cin>>R>>K>>N;

        ar.clear();
        mp.clear();
        for(i=0;i<N;i++)
        {
            scanf("%lld",&t);
            ar.push_back(t);
        }
        j = N;
        convert();

        arrr.clear();
        arrr.push_back(0);
        mp[str]=0;
        for(i=1;i<=R;i++)
        {

            sum=0;
            for(j=0;j<N;j++)
            {
                if(sum + ar[j] > K)break;
                sum+=ar[j];
            }

            neew();
            convert();

            arrr.push_back(arrr[i-1]+sum);
            pos = mp[str];
            if(pos)break;
            else mp[str] = i;

        }
        ans=arrr[pos];
        sum = arrr[i]-arrr[pos];
        diff = i - pos;
        rang = R - pos;
        ans+=(rang/diff)*sum;
        remain = rang%diff;
        ans+=arrr[pos+remain]-arrr[pos];
        cout<<"Case #"<<++kase<<": "<<ans<<endl;
    }
    return 0;
}
