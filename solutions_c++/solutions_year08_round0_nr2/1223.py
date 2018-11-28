#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;
int h,i,j,k,l,m,n,a,b,t,na,nb,mass[500];
char tmp;
int main()
{
	freopen("b-large.in","r",stdin);
	freopen("b-large.out","w",stdout);
	scanf("%d",&n);
	for(h=1;h<=n;h++)
	{
		scanf("%d",&t);
		scanf("%d%d\n",&na,&nb);
		for(i=0;i<na;i++)
		{
			scanf("%c",&tmp);
			m=(tmp-'0')*60000;
			scanf("%c",&tmp);
			m+=(tmp-'0')*6000;
			scanf("%c",&tmp);
			scanf("%c",&tmp);
			m+=(tmp-'0')*1000;
			scanf("%c",&tmp);
			m+=(tmp-'0')*100;
			m+=50;
			mass[i*2]=m;
			scanf("%c",&tmp);
			scanf("%c",&tmp);
			m=(tmp-'0')*60000;
			scanf("%c",&tmp);
			m+=(tmp-'0')*6000;
			scanf("%c",&tmp);
			scanf("%c",&tmp);
			m+=(tmp-'0')*1000;
			scanf("%c\n",&tmp);
			m+=(tmp-'0')*100;
			m+=t*100;
			mass[i*2+1]=m;
		}
		for(i=0;i<nb;i++)
		{
			scanf("%c",&tmp);
			m=(tmp-'0')*60000;
			scanf("%c",&tmp);
			m+=(tmp-'0')*6000;
			scanf("%c",&tmp);
			scanf("%c",&tmp);
			m+=(tmp-'0')*1000;
			scanf("%c",&tmp);
			m+=(tmp-'0')*100;
			m+=51;
			mass[i*2+2*na]=m;
			scanf("%c",&tmp);
			scanf("%c",&tmp);
			m=(tmp-'0')*60000;
			scanf("%c",&tmp);
			m+=(tmp-'0')*6000;
			scanf("%c",&tmp);
			scanf("%c",&tmp);
			m+=(tmp-'0')*1000;
			scanf("%c\n",&tmp);
			m+=(tmp-'0')*100;
			m+=1+t*100;
			mass[i*2+1+2*na]=m;
		}
		k=(na+nb)*2;
		a=0;
		b=0;
		sort(mass,mass+k);
		na=0;
		nb=0;
		for(i=0;i<k;i++)
		{
			if ((mass[i]%100)==0) {nb++;}
			else {
				if ((mass[i]%100)==1) {na++;}
				else {
					if ((mass[i]%100)==50) {if (na!=0){na--;} else {a++;}}
					else {if (nb!=0){nb--;} else {b++;}}
				}
			}
		}
		printf("Case #%d: %d %d\n",h,a,b);
	}
	fclose(stdin);
	fclose(stdout);
}
