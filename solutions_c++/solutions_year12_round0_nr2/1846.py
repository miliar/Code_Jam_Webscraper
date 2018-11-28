#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int list[105];

main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	int T,t,i,j,k,S,P,N,n;
	scanf(" %d",&T);
	for(t=0;t<T;t++){
		scanf(" %d %d %d",&N,&S,&P);
		for(n=0;n<N;n++)
			scanf(" %d",&list[n]);
		int ans = 0,p = 0,s = 0;
		for(n=0;n<N;n++){
			int x;
			if(list[n]<P)
				continue;
			if(list[n]%3==0){
				x = list[n]/3;
			}
			else{
				x = list[n]/3 + 1;
			}
			if(x>=P)
				p++;
			else{
				list[n] -= 2;
				if(list[n]>=0){
					if(list[n]%3==0){
						x = list[n]/3 + 2;
					}
					else{
						x = list[n]/3 + 2;
					}
					if(x>=P)
						s++;
				}
			}
		}
		s = s>S ? S : s;
		ans = p+s;
		printf("Case #%d: %d\n",t+1,ans);
	}
}