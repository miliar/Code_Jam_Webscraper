#include<stdio.h>
#include<stdlib.h>
#include<memory.h>
#include<iostream>
using namespace std;
int cc,dd,n;
char c[40][4];
char d[30][3];
char e[101];
int j;
char inc(char x,char y)
{
	for(int i=0;i<cc;i++)
	{
		if((c[i][0]==x && c[i][1]==y)
		 ||(c[i][0]==y && c[i][1]==x))
		 	return c[i][2];
	}
	return '@';
}

bool ind(char x)
{
	for(int i=0;i<dd;i++)
	{
		if(x==d[i][0])
			for(int k=0;k<j;k++)
				if(e[k]==d[i][1]) return true;
		if(x==d[i][1])
			for(int k=0;k<j;k++)
				if(e[k]==d[i][0]) return true;
	}
	return false;
}

int main()
{
	freopen("B-large.in","r",stdin); 
	freopen("B.out","w",stdout);
	int cas=0;
	scanf("%d",&cas);
	for(int ca=1;ca<=cas;ca++)
	{
		char a[101];
		scanf("%d",&cc);
		for(int i=0;i<cc;i++) scanf("%s",c[i]);
		scanf("%d",&dd);		
		for(int i=0;i<dd;i++) scanf("%s",d[i]);
		scanf("%d %s",&n,a);
		memset(e,0,sizeof(e));
		j=0;
		for(int i=0;i<n;i++)
		{
			if(j==0)
			{
				e[0]=a[i];
				j++;
				continue;
			}
			char tmp=inc(a[i],e[j-1]);
			if(tmp!='@')
			{
				e[j-1]=tmp;
				continue;
			}
			else
			{
				bool ans=ind(a[i]);
				if(ans==true) j=0;
				else{ e[j]=a[i]; j++;}
			}
		}
		cout<<"Case #"<<ca<<": [";
		if(j!=0) cout<<e[0];
		for(int i=1;i<j;i++)
		{
			cout<<", "<<e[i];
		}
		cout<<"]"<<endl;
	}
	return 0;
}

/*
100
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW
0 1 QR  3 FQR
*/
