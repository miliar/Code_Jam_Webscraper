#include<iostream>
using namespace std;
int countbit(int a){return a?1+countbit(a&(a-1)):0;}
int main()
{
	freopen("A-Large.in","r",stdin);
	freopen("A-Large.out","w",stdout);
	int sum,cs,css,i,j,n,k;
	scanf("%d",&cs);
	for(css=1;css<=cs;css++)
	{
		scanf("%d%d",&n,&k);
		sum=1<<n;
		k%=sum;
		if(countbit(k)==n)printf("Case #%d: ON\n",css);
		else printf("Case #%d: OFF\n",css);
	}
	return 0;
 }