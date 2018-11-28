#include <stdio.h>
#include <queue>
#include <algorithm>
#include <string.h>
#include <string>
#include <map>
#include <iostream>

using namespace std;

long long r,n,k,i,j,test,in,t=0,cost[200001001],array[100001],barray[100001],c,q,cnt,start;
long long end,ans,x,y,cycle_cost;
map<string,long long >nayim;
char a[10000];
string s1,s2;

void decode()
{
    c=-1;
    for(q=j;q<n;++q)
        barray[++c]=array[q];
    for(q=0;q<j;++q)
        barray[++c]=array[q];
    for(q=0;q<n;++q)
        array[q]=barray[q];
}

//111111110

int main()
{
    freopen("a.txt","r",stdin);
    freopen("b.txt","w",stdout);
    scanf("%lld",&test);
    while(test--)
    {
        nayim.clear();
        cnt=0;
        scanf("%lld %lld %lld",&r,&k,&n);
        for(i=0;i<n;++i)
            scanf("%lld",&array[i]);
        for(i=1;;++i)
        {
            ////////
            s2.clear();
            for(q=0;q<n;++q)
            {
                sprintf(a,"%lld",array[q]);
                s1=a;
                s2+=s1;
            }
            //cout<<s2<<endl;
            if(nayim[s2]!=0)
            {
                start=nayim[s2];
                end=++cnt;
                break;
            }
            else
                nayim[s2]=++cnt;
            ////////////
            in=0;
            for(j=0;j<n;++j)
            {
                if(in+array[j]<=k)
                    in+=array[j];
                else
                    break;
            }
            cost[cnt]=in;
            decode();
        }
        ans=0;
        if(r<start)
        {
            for(i=1;i<=r;++i)
                ans+=cost[i];
            cout<<"Case #"<<++t<<": "<<ans<<endl;
        }
        else
        {
            for(i=1;i<start;++i)
                ans+=cost[i];
            cycle_cost=0;
            for(i=start;i<end;++i)
                cycle_cost+=cost[i];
            x=(r-start)/(end-start);
            y=(r-start)%(end-start);
            ans+=cycle_cost*x;
            for(i=start;i<=y+start;++i)
                ans+=cost[i];
            cout<<"Case #"<<++t<<": "<<ans<<endl;
        }

        //printf("%ld %ld\n",start,end);
    }
    return 0;
}




