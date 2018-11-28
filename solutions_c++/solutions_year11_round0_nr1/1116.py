#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int pa[101],pb[101],na[101],nb[101];
int a,b,c,d,e,f,g,h,i,j,k,m,n,testcase;
char tem,ch;
int main()
{
	//freopen("A.in","r",stdin);
	//freopen("A.out","w",stdout);
	scanf("%d",&testcase);
	for (f=1;f<=testcase;f++){
		printf("Case #%d: ",f);
		scanf("%d",&n);
		a=0;b=0;
		for (i=1;i<=n;i++){
			scanf("%c%c",&tem,&ch);
			//printf("#%c#",ch);
			if (ch=='O') {a++;scanf("%d",&pa[a]);na[a]=i;} else{
						  b++;scanf("%d",&pb[b]);nb[b]=i;}
			}
		//for (i=1;i<=a;i++) printf("%d %d\n",pa[i],na[i]);printf("\n");
		//for (i=1;i<=b;i++) printf("%d %d\n",pb[i],nb[i]);printf("\n");
		na[a+1]=n+1;nb[b+1]=n+1;
		pa[a+1]=0;pb[b+1]=0;
		g=1;h=1;c=1;d=1;
		int ans=0;
		while (g<=a || h<=b){
			//printf("%d %d %d %d\n",g,h,c,d);
			if (c==pa[g] && na[g]<nb[h] && g<=a){
				g++;ans++;
				if (pb[h]>d) d++; else 
				if (pb[h]<d) d--;
				} else
			if (d==pb[h] && nb[h]<na[g] && h<=b){
				h++;ans++;
				if (pa[g]>c) c++; else 
				if (pa[g]<c) c--;
				} else
			if (na[g]<nb[h]){
				m=abs(pa[g]-c);
				c=pa[g];ans+=m;
				if (abs(pb[h]-d)<=m) d=pb[h]; else{
					if (pb[h]>d) d+=m; else 
					if (pb[h]<d) d-=m;}
				} else{
				m=abs(pb[h]-d);
				d=pb[h];ans+=m;
				if (abs(pa[g]-c)<=m) c=pa[g]; else{
					if (pa[g]>c) c+=m; else 
					if (pa[g]<c) c-=m;}
				}
			}
		printf("%d\n",ans);
		}
	return 0;
}
