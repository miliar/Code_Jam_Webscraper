#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<vector>
using namespace std;

int main()
{
	int i,j,k,p,t,n;
	bool opp[26][26];
	char comb[26][26];
	char *str,*pch;
	scanf("%d\n",&t);
	vector<char> sim;
	int C,D;
	for(p=0;p<t;p++)
	{
		for(i=0;i<26;i++)
		{
			fill(opp[i],opp[i]+26,false);
			fill(comb[i],comb[i]+26,' ');
		}
		str=new char[1000];
		fgets(str,1000,stdin);
		pch = strtok (str," ");
		C=atoi(pch);

		for(i=0;i<C;i++)
		{
			pch = strtok (NULL, " ");
			comb[pch[0]-65][pch[1]-65]=pch[2];
			comb[pch[1]-65][pch[0]-65]=pch[2];
		}
		pch = strtok (NULL," ");
		D=atoi(pch);

		for(i=0;i<D;i++)
		{
			pch = strtok (NULL, " ");
			opp[pch[0]-65][pch[1]-65]=true;
			opp[pch[1]-65][pch[0]-65]=true;
		}
		pch = strtok (NULL," ");
		n=atoi(pch);

		pch = strtok (NULL," ");
		//pch is input string
		for(i=0;i<n;i++)
		{
			
			if(sim.empty())
			{
				sim.push_back(pch[i]);
				continue;
			}
			
			j=sim.size()-1;
			if(comb[sim[j]-65][pch[i]-65]!=' ')
			{
				sim[j]=comb[sim[j]-65][pch[i]-65];
				continue;
			}
			while(j>=0)
			{
				if(opp[sim[j]-65][pch[i]-65])
					break;
				j--;
			}
			if(j<0)
				sim.push_back(pch[i]);
			else
				sim.clear();
		}
		printf("Case #%d: [",p+1);
		if(sim.empty())
			printf("]\n");
		else
		{
			for(i=0;i<sim.size()-1;i++)
				printf("%c, ",sim[i]);
			printf("%c]\n",sim[i]);
		}
		if(!sim.empty())
			sim.clear();
	}
	return 0;
}