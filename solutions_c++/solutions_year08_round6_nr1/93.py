#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int i,j,k,s,t,n,m;
struct node {
	int l,t;
}tmp;
vector <node> a,b;
struct point{
	int w,h,type;
}bird[2000];
int T,I,w,h,m1,m2,tm1,tm2,t1,t2,tt1,tt2;
char ch;
bool cmp(node a,node b){
	return a.l<b.l;
}
char st[200];
main()
{
	scanf("%d",&T);
	for (I=1;I<=T;++I)
	{
		printf("Case #%d:\n",I);
		a.clear();
		b.clear();
		scanf("%d",&n);
		for (i=0;i<n;++i)
		{
			scanf("%d%d",&w,&h);
			bird[i].w=w;
			bird[i].h=h;
			scanf(" %c",&ch);
			gets(st);
			if (ch=='B'){
				tmp.l=h;
				tmp.t=1;
				a.push_back(tmp);
				tmp.l=w;
				tmp.t=1;
				b.push_back(tmp);
				bird[i].type=1;
			}
			else bird[i].type=0;
		}
		sort(a.begin(),a.end(),cmp);
		sort(b.begin(),b.end(),cmp);
		t1=t2=tt1=tt2=-1;
		m1=m2=tm1=tm2=-1;
		if (a.size()>=1)
		{
			m1=a[0].l;
			m2=a[a.size()-1].l;
		}
		if (b.size()>=1)
		{
			tm1=b[0].l;
			tm2=b[b.size()-1].l;
		}
		for (i=0;i<n;++i)
		    if (bird[i].type==0){
				if (bird[i].h>=m1 && bird[i].h<=m2){
					if (bird[i].w>tm2 && (tt2==-1 || tt2>bird[i].w)) tt2=bird[i].w;
					if (bird[i].w<tm1 && tt1<bird[i].w) tt1=bird[i].w;
				}

				else {
					if (bird[i].w>=tm1 && bird[i].w<=tm2){
					if (bird[i].h>m2 && (t2==-1 || t2>bird[i].h)) {t2=bird[i].h;}
					if (bird[i].h<m1 && t1<bird[i].h) t1=bird[i].h;
					}
				}
			}
		int nn;
		scanf("%d",&nn);
		for (i=0;i<nn;++i)
		{
			scanf("%d%d",&w,&h);
			if (h>=m1 && h<=m2 && w>=tm1 && w<=tm2) printf("BIRD\n");
			else {
				bool f=1;
				for (j=0;j<n;++j)
					if (bird[j].type==0 && bird[j].w==w && bird[j].h==h) f=0;
				if (!f || h<=t1 && t1!=-1 || t2!=-1 && h>=t2 || tt1!=-1 && w<=tt1 || tt2!=-1 && w>=tt2) printf("NOT BIRD\n");
				else printf("UNKNOWN\n");
			}
		}
	}
	return 0;
}

			
