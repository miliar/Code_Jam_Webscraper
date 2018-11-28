#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
using namespace std;
int t,d,lx,rx,lo,ro;
int x[10],o[10],xx[10],oo[10];
char s[1000];
int main()
{
	scanf("%d",&t);
	for (int l=1;l<=t;l++)
	{
		memset(x,0,sizeof(x));
		memset(o,0,sizeof(o));
		memset(xx,0,sizeof(xx));
		memset(oo,0,sizeof(oo));
		d=0; lx=0; rx=0; lo=0; ro=0;
		getchar();
		for (int i=1;i<=4;i++)
		{
			gets(s);
			for (int j=0;j<=3;j++)
			{
				if (s[j]=='X') {x[i]++; xx[j]++;}
				if (s[j]=='O') {o[i]++; oo[j]++;}
				if (s[j]=='.') d++;
				if (s[j]=='T') {x[i]++; xx[j]++; o[i]++; oo[j]++;}
				if (j==i-1)
				{
					if (s[j]=='O') lo++;
					if (s[j]=='X') lx++;
					if (s[j]=='T') {lo++; lx++;}
				}
				if (j==3-i+1)
				{
					if (s[j]=='O') ro++;
					if (s[j]=='X') rx++;
					if (s[j]=='T') {ro++; rx++;}
				}
			}
		}
		int p=0;
		if (ro==4 || lo==4) {printf("Case #%d: O won\n",l); p=1;}
		if (rx==4 || rx==4) {printf("Case #%d: X won\n",l); p=1;}
		for (int i=1;i<=4;i++)
		{
			if (x[i]==4 || xx[i-1]==4) {printf("Case #%d: X won\n",l); p=1; break;}
			if (o[i]==4 || oo[i-1]==4) {printf("Case #%d: O won\n",l); p=1; break;}
		}
		if (p==0 && d!=0) printf("Case #%d: Game has not completed\n",l);
		if (p==0 && d==0) printf("Case #%d: Draw\n",l);
	}
	return 0;
}
