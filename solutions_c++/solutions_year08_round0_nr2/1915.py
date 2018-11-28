#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<string>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;

int cas;

struct Node {
	int be,end;
} a[1000],b[1000];

int na,nb,t;
char str[30];

struct Tim {
	int t, in;
	bool operator<(const Tim& ti) const {
		if(t==ti.t) return in==1;
		return t<ti.t;
	}
} p[1000];

int convert(char* st)
{
	int h=(st[0]-'0')*10+st[1]-'0';
	int m=(st[3]-'0')*10+st[4]-'0';
	return h*60+m;
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&cas);
	int lv,i;
	for(lv=1;lv<=cas;lv++) {
		scanf("%d%d%d",&t,&na,&nb);
		for(i=0;i<na;i++) {
			scanf("%s",str);
			a[i].be=convert(str);
			scanf("%s",str);
			a[i].end=convert(str);
		}
//		for(i=0;i<na;i++) printf("%4d %4d\n", a[i].be, a[i].end); printf("\n");

		for(i=0;i<nb;i++) {
			scanf("%s",str);
			b[i].be=convert(str);
			scanf("%s",str);
			b[i].end=convert(str);
		}
//		for(i=0;i<nb;i++) printf("%4d %4d\n", b[i].be, b[i].end); printf("\n");
		int acnt, bcnt, n, s;
		n=na+nb;

		for(i=0;i<na;i++) {
			p[i].t=a[i].be;
			p[i].in=-1;
		}
		for(;i<n;i++) {
			p[i].t=b[i-na].end+t;
			p[i].in=1;
		}
		sort(p,p+n);
//		for(i=0;i<n;i++) printf("%3d %2d\n",p[i].t, p[i].in); printf("\n");
		acnt=0; s=0;
		for(i=0;i<n;i++) {
			s+=p[i].in;
			if(s<0) acnt++,s=0;
		}

		for(i=0;i<nb;i++) {
			p[i].t=b[i].be;
			p[i].in=-1;
		}
		for(;i<n;i++) {
			p[i].t=a[i-nb].end+t;
			p[i].in=1;
		}
		sort(p,p+n);
//		for(i=0;i<n;i++) printf("%3d %2d\n",p[i].t, p[i].in); printf("\n");
		bcnt=0; s=0;
		for(i=0;i<n;i++) {
			s+=p[i].in;
			if(s<0) bcnt++,s=0;
		}

		printf("Case #%d: %d %d\n", lv, acnt, bcnt);
	}
	return 0;
}