#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<string.h>
#include<set>
#include<stack>
#include<iostream>
#include<math.h>
#include<map>
#include<memory.h>
#include<algorithm>
using namespace std;
#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<set>
#include<stack>
#include<iostream>
#include<math.h>
#include<map>
#include<memory.h>
#include<algorithm>
using namespace std;
int ans;
int c;
int ll,pp;
int xxj(int gs)
{
	int i=1;
	int cnt=0;
	while(i*2<=gs){ cnt++;i=i*2;}
	return cnt+1;
}
int main()
{
    freopen("B-small-attempt3.in","r",stdin);
	freopen("B.txt","w",stdout);
	int t,i,j,n;
	scanf("%d",&t);
	int cas=1;
	while(t--)
	{
		ans=0;
		scanf("%d %d %d",&ll,&pp,&c);	
		int tmp=pp/ll;
		if(pp%ll) tmp++;
		int py=ll;
		    while(ll*c<pp)
		    {
		    	ll=ll*c;
				ans++;
			}
			if(ans)
		    printf("Case #%d: %d\n",cas++,xxj(ans));
		    else
		    printf("Case #%d: %d\n",cas++,0);
	}
	return 0;
}
