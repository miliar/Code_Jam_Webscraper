#include<iostream>
#include<cstring>
#include<cmath>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;


void main(){

#ifdef INPUT_VAR
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
#endif
	int T,n,s,p,d;
	scanf("%d",&T);
	for (int I=1;I<=T;I++)
	{
		int rez=0,a1,a2;
		scanf("%d%d%d",&n,&s,&p);
		a1=max(3*p-2,0);
		a2=max(3*p-4,2);
		for (int j=0;j<n;j++)	
		{
			scanf("%d",&d);
			if (d>=a1)rez++;
			else
				if (d>=a2&&s)
				{
					rez++;
					s--;
				}
		}
		printf("Case #%d: %d\n",I,rez);		
	}
}