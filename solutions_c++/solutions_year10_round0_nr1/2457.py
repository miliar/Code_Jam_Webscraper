#include<iostream>
#include<algorithm>
#include<string>
#include<math.h>
#include<vector>
#include<map>
using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,k,t,n;
	scanf("%d",&t);
	for(int ca=1;ca<=t;ca++)
	{
		scanf("%d%d",&n,&k);
		int nn=0,max=(1<<n);
		k%=max;
		while(k)
		{
			if(k%2)nn++;
			else break;

			k/=2;
		}
		printf("Case #%d: ",ca);
		if(nn==n)printf("ON\n");
		else printf("OFF\n");
	}
}
