#include<iostream>
#include<stdio.h>
#include<string.h>
#include <vector>
#include <stdlib.h>

#define pii pair<int,int>
#define f first
#define s second
using namespace std;

int main()
{
	int i,p,n,t,j;
	
	
	char *str,*pch;
	scanf("%d\n",&t);
	vector< pii > O,B;
	
	int steps,cb,co,move;
	
	for(p=0;p<t;p++)
	{
		str=new char[1000];
		fgets(str,1000,stdin);
		
		pch = strtok (str," ");
		n=atoi(pch);
		for(i=0;i<n;i++)
		{
			pch = strtok (NULL, " ");
			if(strcmp(pch,"O")==0)
			{
				pch = strtok (NULL, " ");
				O.push_back(pii(atoi(pch),i));
			}
			else if(strcmp(pch,"B")==0)
			{
				pch = strtok (NULL, " ");
				B.push_back(pii(atoi(pch),i));
			}
		}
		steps=0;
		i=j=0;
		cb=co=1;
		while(i<O.size()&&j<B.size())
		{
			if(O[i].s<B[j].s)
			{
				move=abs(O[i].f-co)+1;
				steps+=move;
				if(cb<B[j].f)
				{
					cb=min(cb+move,B[j].f);
				}
				else if(cb>B[j].f)
				{
					cb=max(cb-move,B[j].f);
				}
				co=O[i].f;
				i++;
			}
			else
			{
				move=abs(B[j].f-cb)+1;
				steps+=move;
				if(co<O[i].f)
				{
					co=min(co+move,O[i].f);
				}
				else if(co>O[i].f)
				{
					co=max(co-move,O[i].f);
				}
				cb=B[j].f;
				j++;
			}
		}
		while(i<O.size())
		{
			move=abs(O[i].f-co)+1;
			steps+=move;
			co=O[i].f;
			i++;
		}
		while(j<B.size())
		{
			move=abs(B[j].f-cb)+1;
			steps+=move;
			cb=B[j].f;
			j++;
		}
		printf("Case #%d: %d\n",p+1,steps);
		O.clear();
		B.clear();
	}
}