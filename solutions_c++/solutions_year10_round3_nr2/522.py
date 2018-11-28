#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<iostream>
#include<math.h>
//using namespace std;

#define e 2.7182818284

int main()
{
	int i,j,k,tc,T,ans,l,p,c;
	int mm=100;
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d", &T);
	for(tc=1; tc<=T; tc++)
	{
		scanf("%d%d%d", &l,&p,&c);
		ans=0;
		int tmp=l*c;
		while(tmp<p)
		{
			tmp*=c;
			ans++;
		}
		if(ans!=0)
			ans=ceil( log((double)(1.0*(ans+1)))/log(2.0) );
		printf("Case #%d: %d\n", tc,ans);
	}
	return 0;	
}

