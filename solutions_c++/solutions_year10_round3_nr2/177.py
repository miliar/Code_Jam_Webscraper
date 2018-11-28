#include<stdio.h>
#include<iostream>
#include<queue>
#include<map>
#include<vector>
#include<string>
#include<sstream>
#include<math.h>
#include<algorithm>
#define _clr(x) memset(x,-1,sizeof(x))
#define clr(x) memset(x,0,sizeof(x))
#define pb push_back
#define M 1001
#define ll long long
using namespace std;
const int oo=1<<29;
int main()
{
    freopen("in.txt","r",stdin);
    //freopen("in.in","r",stdin);
    freopen("in.out","w",stdout);
    int T;
    scanf("%d",&T);
    int ca=0;
    while(T--)
    {
        int a,b,c;
        scanf("%d%d%d",&a,&b,&c);
        b=(b+a-1)/a;
		a=1;
		int ans=0;
        while((ll)a*c<(ll)b)
        {
            b=(int)ceil(sqrt((double)b));
			ans++;
        }
        printf("Case #%d: %d\n",++ca,ans);
    }
}
