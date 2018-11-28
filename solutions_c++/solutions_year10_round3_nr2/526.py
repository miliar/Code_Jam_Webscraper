#include <iostream>
#include <cmath>
using namespace std;

int l,p,a,b,c,t;
double res;



int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int q=1; q<=t; q++)
	{
		scanf("%d %d %d",&l, &p, &c);
		int ans=0; 
		a=l; b=p;
		int times;
		for (times=0; a<b; times++) a*=c;
		res= log((double)times)/log((double)2);
		ans=res;
		if (times > pow((double)2,ans)) 
			ans++;
		printf("Case #%d: %d\n",q,ans);
	}
	return 0;
}