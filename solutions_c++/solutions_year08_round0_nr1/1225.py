#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;
int a[100][1000],n,i,k,j,l,h,m,s,sp,q,qp,posl[1001];
char mass[100][101],qr[101],tmp;
bool theend=false;
bool equal(int t)
{
	int v,p;
	v=strlen(mass[t]);
	if (v!=strlen(qr))
	{
		return(false);
	}
	else
	{
		for(p=0;p<v;p++)
		{
			if(qr[p]!=mass[t][p]) {return(false);}
		}
		return(true);
	}
}
int main()
{
	freopen("a-large.in","r",stdin);
	scanf("%d\n",&n);
	freopen("a-large.out","w",stdout);
	for(h=1;h<=n;h++)
	{
		scanf("%d\n",&s);
		for(i=0;i<s;i++) 
		{
			scanf("%c",&tmp);
			j=0;
			while (tmp!='\n')
			{
				mass[i][j]=tmp;
				j++;
				scanf("%c",&tmp);
			}
			mass[i][j]='\0';
		}
		scanf("%d\n",&q);
		for(i=0;i<q;i++) 
		{
			scanf("%c",&tmp);
			j=0;
			while (tmp!='\n')
			{
				qr[j]=tmp;
				j++;
				scanf("%c",&tmp);
			}
			qr[j]='\0';
			for(j=0;j<s;j++)
			{
				if(equal(j))
				{
					posl[i]=j;
					break;
				}
			}
		}
		sp=0;
		qp=0;
		theend=false;
		for(i=0;i<s;i++)
		{
			a[i][0]=0;
			m=0;
			while((m<q)&&(posl[m]!=i)) {m++;}
			if (m>a[i][0]) {a[i][0]=m;}
			if (a[i][0]==q) {theend=true;}
		}
		while (!theend)
		{
			qp++;
			for(i=0;i<s;i++){a[i][qp]=0;}
			for(sp=0;sp<s;sp++)
			{
				for(i=0;i<s;i++)
				{
					m=a[i][qp-1];
					while ((m<q)&&(posl[m]!=sp)) {m++;}
					if (m>a[sp][qp]) {a[sp][qp]=m;}
				}
				if (a[sp][qp]==q) {theend=true;}
			}
		}
		printf("Case #%d: %d\n",h,qp);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
