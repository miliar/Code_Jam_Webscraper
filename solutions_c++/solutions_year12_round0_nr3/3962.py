#include<iostream>
#include<cassert>
#include<cstdlib>
#include<cstring>
#include<utility>
#include<sstream>
#include<algorithm>
#include<cstdio>
#include<vector>
#include<string>
#include<cctype>
#include<queue>
#include<deque>
#include<stack>
#include<cmath>
#include<ctime>
#include<list>
#include<map>
#include<set>
#define pi (acos(-1.0))
#define Abs(a) (((a)<0) ? (-(a)) :(a) )
#define rep(i,n) for((i)=0;(i)<(n);(i)++)
#define rrep(i,n) for((i)=(n);(i)>=0;(i)--)
#define PB push_back
using namespace std;
typedef long long mint;
typedef unsigned long long umint;
int main()
{
    //clock_t st=clock(),en;
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	int t,T,a,b,tnp,cnt,tmp,i,j;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		cnt=0;
		tnp=1;
		scanf("%d%d",&a,&b);
		tmp=a;
		while(tmp>=10)
		{
		    tnp*=10;
		    tmp/=10;
		}
		for(i=a;i<b;i++)
		{
		    tmp=i;
		    do
		    {
		        tmp=tnp*(tmp%10)+tmp/10;
		        if(tmp==i)
                    break;
                if(tmp>i&&tmp<=b)
                    cnt++;
		    }while(true);
		}
		printf("Case #%d: ",t);
		printf("%d\n",cnt);
	}
	//en=clock();
	//cout<<(en-st)/CLOCKS_PER_SEC;
	return 0;
}


