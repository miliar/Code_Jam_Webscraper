#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
int a,b,c,d,f,g,h,i,j,k,m,n,tcase;
int w[100010];
char s[200];
int v[200];
long long mi[200],x;
long long y;
int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	scanf("%d",&tcase);
	mi[0]=1;
	for (i=1;i<=61;i++) mi[i]=mi[i-1]*2;
	for (f=1;f<=tcase;f++){
		printf("Case #%d: ",f);
		scanf("%s",s);
		h=strlen(s);
		long long e=0;
		c=0;
		for (i=h-1;i>=0;i--){
			if (s[i]=='?') {
				c++;v[c]=i;} else
			if (s[i]=='1') {
			//	printf("# %d\n",i);
				e=e+mi[h-i-1];}}
		//cout<<e<<endl;
		for (i=0;i<mi[c];i++){
			x=e;
			for (j=1;j<=c;j++) if ( (i&(1<<(j-1)))>0)
				x=x+mi[h-1-v[j]];
			y=(long long) sqrt(x);
			if ((y-1)*(y-1)==x || (y*y)==x || (y+1)*(y+1)==x) {
			//	cout<<x<<endl;
			//	printf("%.6lf\n",y);
				for (j=1;j<=c;j++)  if ( (i&(1<<(j-1)))>0)
					s[v[j]]='1'; else s[v[j]]='0';
				break;}
			}
		cout<<s<<endl;
		}
	return 0;
}
