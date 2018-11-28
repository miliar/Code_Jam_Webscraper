#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <string>
#include <math.h>
#include <algorithm>
#include <queue>
using namespace	std;




int main(){
#ifdef	xDx
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
	int T;
	scanf("%d",&T);
	for(int i= 0 ;i < T; i++){
		int N,Pd,Pg;
		scanf("%d%d%d",&N,&Pd,&Pg);
		bool can = false;
		int D;

		for(int i = 1; i<=N && !can; i++)
		{
			if((Pd*i)%100 == 0)
			{
				can = true;
				D= i;
			}
		}
		
		if(Pg==0 && Pd!=0 || Pg==100 && Pd!=100 )
			can = false;

		printf("Case #%d: ",i+1);
		if(can)
			printf("Possible\n");
		else
			printf("Broken\n");
		
	}

	return 0;
}