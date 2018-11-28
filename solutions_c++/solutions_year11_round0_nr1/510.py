#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct robot{
	int pos;
}r[2];

int n;

int ABS(int x) {
	if(x>=0)return x;
	return (-x);
}

int main(){
	//freopen("d:\\A-small-attempt1.in","r",stdin);freopen("d:\\A-small-attempt1.out","w",stdout);
	//freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	//freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("d:\\A-large.in","r",stdin);freopen("d:\\A-large.out","w",stdout);
	int cse, g=1, x, i, ti, pre, tp;
	char ro[2], p;
	scanf("%d",&cse);
	while(cse--) {
		scanf("%d",&n);
		ti = pre = 0;
		r[0].pos = r[1].pos = 1;
		p = -1;
		for(i=0;i<n;++i) {
			scanf("%s %d",ro,&x);
			if(strcmp(ro,"O")==0) {
				tp = ABS(x - r[0].pos);
				if(p == 1) {
					if(tp >= pre) tp -= pre;
					else
						tp = 0;
				}
				ti += tp + 1;
				if(p == 1) pre = tp + 1;
				else
					pre += tp + 1;
				p = 0;
				r[0].pos = x;
			}
			else if(strcmp(ro,"B")==0) {
				tp = ABS(x - r[1].pos);
				if(p == 0) {
					if(tp >= pre) tp -= pre;
					else
						tp = 0;
				}
				ti += tp + 1;
				if(p == 0) pre = tp + 1;
				else
					pre += tp + 1;
				p = 1;
				r[1].pos = x;
			}
		}
		printf("Case #%d: %d\n", g++, ti);
	}
	//system("PAUSE");
	return 0;
}