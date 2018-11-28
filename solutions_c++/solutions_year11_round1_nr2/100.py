#include<iostream>
#include<algorithm>
using namespace std;
int b2[20000],b3[20000],b4[20000],o[20000];
char w[20000][20],b[20000][20];
bool cmp(int x,int y)
{
	return strcmp(b[x],b[y])<0;
}
int main()
{
	int a,s,d,f,n,m,l,t,x,mx;
	char i[30];
int _,T;
scanf("%d",&T);
for(_=1;_<=T;_++)
{
	scanf("%d%d",&n,&m);
	for(a=0;a<n;a++) scanf("%s",w[a]);
	printf("Case #%d:",_);
//printf("\n");
	for(s=0;s<m;s++)
	{
		scanf("%s",i);
		for(a=0;a<n;a++)
		{
			l=strlen(w[a]);
			for(d=0;d<l;d++) b[a][d]='_';
			b[a][l]=0;
			b2[a]=a;
		}
		sort(b2,b2+n,cmp);
		for(a=0;a<n;a++) o[a]=0;
		for(d=0;d<26;d++)
		{
			for(a=0;a<n;a++){ b3[a]=0; b4[a]=0; }
			t=b2[0];
			for(a=0;a<n;a++)
			{
				x=b2[a];
				if( a>0 ) if( strcmp(b[x],b[b2[a-1]])!=0 ){ t=x; b3[t]=2; }
				l=strlen(w[x]);
				for(f=0;f<l;f++) if( w[x][f]==i[d] ){ b3[t]=1; b4[x]=1; }
//printf("%d %s %s: %d %s %d %d\n",x,w[x],b[x],t,w[t],,b4[x]);
			}
			t=0;
			for(a=0;a<n;a++)
			{
				x=b2[a];
				if( b3[x]==1 ) t=1; else if( b3[x]==2 ) t=0;
				o[x]+=(1-b4[x])*t;
				l=strlen(w[x]);
				for(f=0;f<l;f++) if( w[x][f]==i[d] ) b[x][f]=i[d];
			}
			sort(b2,b2+n,cmp);
		}
		mx=-1;
		t=0;
		for(a=0;a<n;a++)
		{
//printf("%s: %d\n",w[a],o[a]);
			if( o[a]>mx ){ mx=o[a]; t=a; }
		}
		printf(" %s",w[t]);
	}
	printf("\n");
}
	return 0;
}
