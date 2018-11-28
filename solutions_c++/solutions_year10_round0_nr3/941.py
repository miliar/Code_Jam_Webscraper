#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>

#define outln(x) (cout<<#x<<" "<<x<<endl)
using namespace std;

typedef long long LL;

const int N = 10001000;

LL r,k,n;
LL v[N];
LL result;
LL array[N];
LL earn[N];


    void inputing()
    {
        result = 0;
        cin>>r>>k>>n;
        for ( LL i=0;i<n;i++ )
        cin>>array[i];
        for ( LL i=0;i<=n;i++ )
        v[i] = 0;
    }

    void add( LL & now )
    {
        LL start = now;
        LL sum = 0;
        do
        {
            if ( sum + array[now]> k ) break;
            sum += array[now];
            result += array[now];
            now ++;
            if ( n == now ) now = 0;
        }while (now != start);
    }

    void work()
    {
        LL i,j;
        earn[0] = 0;
        LL now = 0;
        LL circle = -1;
        for ( i=1;i<=r;i++ )
        {
            if ( v[now] !=0 )
            {
                circle = i - v[now];
//                printf("FIND CIRCLE! %d  last:%d   circle: %d\n",now,v[now],circle);//debug
                break;
            }
            v[now] = i;
            add(now);
            earn[i] = result;
//            printf("times: %d   now: %d  result: %d\n",i,now,result);//debugs
        }
        LL left = r - i+1;
        LL c1 = left / circle;
        left %= circle;
        LL earn_circle = earn[i-1] - earn[v[now]-1];
        result +=((LL)c1)* earn_circle;
//        outln(left);outln(c1);cout<<"earn_circle: "<<earn_circle<<endl;cout<<"result : "<<result<<endl;
        result += earn[v[now]-1+left] - earn[ v[now]-1 ];
//        outln(result);
    }


int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cas;
    cin>>cas;
    for ( LL i=1;i<=cas;i++ )
    {
        inputing();
        work();
        cout<<"Case #"<<i<<": "<<result<<endl;
    }
    return 0;
}
