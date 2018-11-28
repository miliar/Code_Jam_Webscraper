#include <stdio.h>

int cs,ct,T,na,nb,k,needA,needB,inA,inB;
struct Time {
	int s,t,n;
} a[200];

int change(char *s)
{
	return ((s[0]-'0')*10+(s[1]-'0'))*60+((s[3]-'0')*10+(s[4]-'0'));
}

int main()
{
	int i,j;
	char t1[10],t2[10];
	scanf("%d",&cs);
	for (ct=1;ct<=cs;ct++) {
		scanf("%d",&T);
		scanf("%d%d",&na,&nb);
		k=0;
		for (i=0;i<na;i++) {
			scanf("%s%s",t1,t2);
			a[k].s=change(t1);
			a[k].t=change(t2);
			a[k++].n=0;
		}
		for (i=0;i<nb;i++) {
			scanf("%s%s",t1,t2);
			a[k].s=change(t1);
			a[k].t=change(t2);
			a[k++].n=1;
		}
		needA=needB=0;
		inA=inB=0;
		for (i=0;i<1440;i++) {
			for (j=0;j<k;j++)
			if (a[j].t+T==i) {
				if (a[j].n==0) inB++;
				else inA++;					
			}
			for (j=0;j<k;j++)
			if (a[j].s==i) {
				if (a[j].n==0)
					if (inA) inA--;
					else needA++;
				else if (inB) inB--;
					else needB++;
			}
		}
		printf("Case #%d: %d %d\n",ct,needA,needB);
	}
	return 0;
}
