#include<iostream>
#include<stdio.h>
#include<map>
#include<algorithm>
using namespace std;
int main()
{
	int t,c,d,n,i,j,k;
	char ss[200],ans[200],top;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		map<pair<char,char>,char> cc;
		map<pair<char,char>,char>::iterator cit;
		map<char,char> dd;
		map<char,char>::iterator dit;
		scanf("%d",&c);
		top=-1;
		for(i=0;i<c;i++)
		{
			scanf("%s",ss);
			cc[pair<char,char>(ss[0],ss[1])]=ss[2];
			cc[pair<char,char>(ss[1],ss[0])]=ss[2];
		}
		scanf("%d",&d);
		for(i=0;i<d;i++)
		{
			scanf("%s",ss);
			dd[ss[0]]=ss[1];
			dd[ss[1]]=ss[0];
		}
		scanf("%d%s",&n,ss);
		for(i=0;i<n;i++)
		{
			if(top==-1)
				ans[++top]=ss[i];
			else	if((cit=cc.find(pair<char,char>(ss[i],ans[top])))!=cc.end())
				ans[top]=cit->second;
			else if((dit=dd.find(ss[i]))!=dd.end())
			{
				for(j=0;j<=top;j++)
					if(ans[j]==dit->second)
						break;
				if(j<=top)
					top=-1;
				else
					ans[++top]=ss[i];			
			}
			else
				ans[++top]=ss[i];
		}
		printf("Case #%d: [",k);
		if(top>=0)
		{
			printf("%c",ans[0]);
			for(i=1;i<=top;i++)
				printf(", %c",ans[i]);
		}
		printf("]\n");
	}
	return 0;
}
/*
5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW
*/
