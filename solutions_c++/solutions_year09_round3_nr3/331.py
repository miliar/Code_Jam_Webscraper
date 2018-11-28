#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <string.h>
#include <string>

#define PI 3.14159265358979
#define PB(x) push_back(x)
using namespace std;
typedef long long LL;
void debug_array(int i,int j,int data[]){while (i<j){cout<<"     [ "<<i<<" ] : "<<data[i];i++;}cout<<endl;}

const int N = 200;

int n;
int data[N];
bool v[N];
int ans;
int p;

    int cal(int j)
    {
        int left,right,i;
        for ( i=j;i>=0;i-- )
        if (v[i])
        break;
        if ( -1 == i )
        left = 1;
        else left = data[i]+1;

        for ( i=j;i<n;i++ )
        if (v[i])
        break;
        if ( n == i )
        right = p;
        else right = data[i]-1;
//        printf(" ( %d , %d ) \n",left,right);//debug
        return right - left +1 -1;
    }

    void work(int deep,int now)
    {
        if ( now >= ans )
        return ;
        if ( deep >=n )
        {
            ans = min(ans,now);
//            printf("  ANS = %d\n",ans);//debug
            return ;
        }

        int i;
        for ( i=0 ; i<n;i++ )
        if ( !v[i] )
        {

            int temp = cal(i);
//            printf("use %d  %d  = %d\n",i,data[i],temp);//debug
            v[i] = 1;
            work(deep+1,now + temp);
            v[i] = 0;
//            printf("not use %d  %d\n",i,data[i]);//debug
        }
    }

    void inputing()
    {
        int i;
        scanf("%d%d",&p,&n);
        for ( i=0;i<n;i++)
        scanf("%d",&data[i]);
    }

int main()
{
//    freopen("inputing","r",stdin);
//    freopen("outputing","w",stdout);
    int cas;
    scanf("%d",&cas);
    int i;
    for ( i=1;i<=cas;i++ )
    {
        inputing();
        memset(v,0,sizeof(v));
        ans = 1<<27;
        work(0,0);
        printf("Case #%d: %d\n",i,ans);
    }

    return 0;
}

