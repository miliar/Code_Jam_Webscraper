#include <cstdio>
#include <iostream>
#include <math.h>
using namespace std;

int p, q, a[200], pp[200], qq[200],curp, curq, tp, tq;

int main () {
	freopen("A-large.in-1.txt", "r", stdin);
	freopen("A-large.in-1.out.txt", "w", stdout);
	char ch[2];
	int i, T, n, t, time=0, l1, l2, Case=0, tt;
	scanf("%d", &T);
	while(T--) {
		Case++;
		scanf("%d", &n);
		curp=curq=1;
		l1=l2=0;
		p=q=0;
		time=0;
		for(i=0;i<n;i++) {
			scanf("%s %d", &ch, &t);
			if(ch[0]=='O') {
				a[i]=0;
				pp[l1++]=t;
			}
			else {
				a[i]=1;
				qq[l2++]=t;
			}
		}
		for(i=0;i<n;i++) {
			if(a[i]==0) {
				tp=pp[p++];
				t=abs(tp-curp)+1;
				curp=tp;
				time+=t;
				if(q==l2)
					continue;
				tq=qq[q];
				tt=abs(tq-curq);
				if(t>=tt)
					curq=tq;
				else {
					tt=curq>tq?-1:1;
					curq=curq+tt*t;
				}
			}
			else {
				tq=qq[q++];
				t=abs(tq-curq)+1;
				curq=tq;
				time+=t;
				if(p==l1)
					continue;
				tp=pp[p];
				tt=abs(tp-curp);
				if(t>=tt)
					curp=tp;
				else {
					tt=curp>tp?-1:1;
					curp=curp+tt*t;
				}
			}
		}
		printf("Case #%d: %d\n", Case, time);
	}
	return 0;
}