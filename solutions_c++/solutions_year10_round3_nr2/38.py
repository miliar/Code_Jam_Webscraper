#include <stdio.h>

int l,p,c,T;

int main()
{
	freopen("B-small.in","r",stdin);
	freopen("output.txt","wt",stdout);
	int t,cnt,s,point=0;
	for(scanf("%d",&t);t;t--) {
		scanf("%d %d %d",&l,&p,&c);
		s=p; cnt=-1;
		while(s>l) {
			if(s%c==0) s=s/c;
			else s=s/c+1;
			
			cnt++;
		}
		point=0;
		while(cnt) { point++; cnt/=2; }
		printf("Case #%d: %d\n",++T,point);
	}
	return 0;
}

