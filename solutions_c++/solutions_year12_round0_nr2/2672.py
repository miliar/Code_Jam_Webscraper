#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

int t[10], n, k, p;

bool can(int num)
{
    int ans=0;
    while(num)
    {
        if(num&1) ans++;
        num/=2;
    }
    if(ans==k) return true;
    else return false;
}

int solve(int num)
{
    int i, ans=0;
    for(i=0; i<n; i++)
    {
        if( num&( 1<<i ) )
        {
            if(t[i]<=1) {return 0;}
            else if(t[i]>=29) return 0;
            else if( (t[i]+1)/3+1 >= p ) ans++;
        }
        else
        {
            if( (t[i]+2)/3 >= p ) ans++;
        }
        //cout<<"  ++ "<<i<<' '<<num<<' '<<( num&( 1<<i ) )<<' '<<ans<<endl;
    }
    return ans;
}

int main()
{
    freopen("C:\\Users\\Administrator\\Downloads\\B-small-attempt4.in","r",stdin);
    freopen("test.out","w",stdout);
    int cas, i, ans, j;
    scanf("%d", &cas);
    for(i=1; i<=cas; i++)
    {
        scanf("%d%d%d", &n, &k, &p);
        ans = 0;
        for(j=0; j<n; j++)
        {
            scanf("%d", &t[j]);
        }
        int num = 1<<n;
        for(j=0; j<num; j++)
        if(can(j))
        {
            int tmp = solve(j);
            //cout<<j<<' '<<tmp<<endl;
            ans = max(ans, tmp);
        }
        printf("Case #%d: %d\n", i, ans);
    }
	return 0;
}
