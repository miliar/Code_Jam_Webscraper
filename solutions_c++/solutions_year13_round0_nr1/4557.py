/*Accepted*/
#include<cstdio>
#include<cstring>
#include<cctype>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<stack>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<utility>
#define f0(i,a) for(__typeof(a)i=0;i<a;i++)
#define f1(i,a) for(__typeof(a)i=1;i<=a;i++)
#define fa0(i,a) for(__typeof(a)i=a;i>=0;i--)
#define pf printf
#define sf scanf
#define si(a) scanf("%d",&a)
#define sd(a) scanf("%lf",&a)
#define G getchar()
#define sl strlen
#define nl printf("\n")
#define memo(str,a) memset(str,a,sizeof(str))
#define max(a,b) (a>b)?a:b
#define min(a,b) (a<b)?a:b
#define ll long long
#define pb push_back
#define srt(arr,n) sort(arr,arr+n)
#define rev(arr,n) reverse(arr,arr+n)
#define pi acos(-1.0)
#define popc __builtin_popcount
#define gcd __gcd
#define pii pair<int ,int >
#define all(a) a.begin(),a.end()
using namespace std;
int main()
{
	//freopen("d:\\input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int t,dot,cx,res=1,ct,co;
	char arr[4][4];
	cin>>t;
	f1(cs,t)
	{
	    dot=0,res=0;
	    f0(i,4)
	    {
	        cx=0,co=0,ct=0;
	        f0(j,4)
	        {
	            cin>>arr[i][j];
                if(arr[i][j]=='.') dot++;
                else if(arr[i][j]=='X') cx++;
                else if(arr[i][j]=='T') ct++;
                else if(arr[i][j]=='O') co++;
            }
            if((cx+ct)==4) res=1;
            else if((ct+co)==4) res=2;
	    }
	    if(res==0)
	    f0(j,4)
	    {
	        cx=0,co=0,ct=0;
	        f0(i,4)
	        {
	            if(arr[i][j]=='X') cx++;
                else if(arr[i][j]=='T') ct++;
                else if(arr[i][j]=='O') co++;
	        }
	        if((cx+ct)==4) res=1;
            else if((ct+co)==4) res=2;
	    }
	    if(res==0)
        {
            cx=0,co=0,ct=0;
            f0(j,4)
	        {
	            if(arr[j][j]=='X') cx++;
                else if(arr[j][j]=='T') ct++;
                else if(arr[j][j]=='O') co++;
	        }
	        if((cx+ct)==4) res=1;
            else if((ct+co)==4) res=2;
        }
        if(res==0)
        {
            cx=0,co=0,ct=0;
            for(int i=0,j=3;i<4,j>=0;i++,j--)
	        {
	            if(arr[i][j]=='X') cx++;
                else if(arr[i][j]=='T') ct++;
                else if(arr[i][j]=='O') co++;
	        }
	        if((cx+ct)==4) res=1;
            else if((ct+co)==4) res=2;
        }
        if(res==1) pf("Case #%d: X won\n",cs);
        else if(res==2) pf("Case #%d: O won\n",cs);
        else if(dot==0) pf("Case #%d: Draw\n",cs);
        else  pf("Case #%d: Game has not completed\n",cs);
	}
	return 0;
}
