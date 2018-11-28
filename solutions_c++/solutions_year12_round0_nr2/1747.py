#include <iostream>

using namespace std;


int main()
{
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	for (int ttt=1;ttt<=T; ttt++)
	{
		int ans=0,a,n,s,p,x,l;
		scanf("%d%d%d",&n,&s,&p);
		for (int i=1; i<=n; i++ ) 
		{
			scanf("%d",&x);
			if (x%3==0) { if (x/3>0) l=x/3+1; else l=0; }
			else if (x%3==1) { if (x/3>0) l=x/3+1; else l=0; }
			else l=x/3+2;
			if (x%3==0) a=x/3;
			else if (x%3==1) a=x/3+1;
			else a=x/3+1;
			if (a>=p) ans++;
			else if (s>0 && l>=p) { ans++; s--; }
		}
		printf("Case #%d: %d\n",ttt,ans);
	}
	
	
}