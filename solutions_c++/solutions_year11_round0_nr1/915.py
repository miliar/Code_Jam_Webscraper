#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int T,n,ar[1000];
char ch[1000][3];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for (int test=1;test<=T;test++)
	{
		scanf("%d",&n);
		for (int i=0;i<n;i++)
		{
			scanf("%s%d",ch[i],&ar[i]);
			ar[i]--;
		}
		int pos[2];
		pos[0]=pos[1]=0;
		int p1=0,p2=0;
		while(p1 < n && ch[p1][0] != 'O')
			p1++;
		while(p2 < n && ch[p2][0] != 'B')
			p2++;
		int res = 0;
		while(p1 < n || p2 < n)
		{
			bool b1=0,b2=0;
			res++;
			if (p1 < n && ar[p1] != pos[0])
			{
				if (ar[p1] > pos[0])
					pos[0]++;
				else
					pos[0]--;
				b1=1;
			}
			if (p2 < n && ar[p2] != pos[1])
			{
				if (ar[p2] > pos[1])
					pos[1]++;
				else
					pos[1]--;
				b2=1;
			}
			if (!b1 && p1 < p2 && ar[p1] == pos[0])
			{
				p1++;
				while(p1 < n && ch[p1][0] != 'O')
					p1++;
				continue;
			}
			if (!b2 &&p2 < p1 && ar[p2] == pos[1])
			{
				p2++;
				while(p2 < n && ch[p2][0] != 'B')
					p2++;
				continue;
			}
		}
		printf("Case #%d: %d\n",test,res);
	}
}