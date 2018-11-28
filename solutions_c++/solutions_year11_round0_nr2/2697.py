/* 
 * File:   main.cpp
 * Author: Sreekanth
 *
 * Created on May 7, 2011
 */

#include <stdlib.h>
#include <stdio.h>

/*
 * 
 */
int main()
{
  freopen("I.in","r",stdin);
  freopen("O.op","w",stdout);

  int cases;
  scanf("%d",&cases);
  int caserunning=0;
  while (cases--)
  {
	char prevltr;
	char presltr;
	char out[999999] = {0};
	int outcount = 0;
	char comb[256][3] = {0};
	int combcount = 0;
	char opps[256][2] = {0};
	int oppscount = 0;

	char space;
	char ltr;
	
	int combines = 0;
	scanf("%d",&combines);
	combcount = combines;
	int i = 0;
	while(combines--)
	{
		scanf("%c",&space);
		scanf("%c",&ltr);
		comb[i][0] = ltr;
		scanf("%c",&ltr);
		comb[i][1] = ltr;
		scanf("%c",&ltr);
		comb[i][2] = ltr;
	}

	int opposes = 0;
	scanf("%d",&opposes);
	oppscount = opposes;
	i = 0;
	while(opposes--)
	{
		scanf("%c",&space);
		scanf("%c",&ltr);
		opps[i][0] = ltr;
		scanf("%c",&ltr);
		opps[i][1] = ltr;	
		
	}

	int processltrs = 0;
	scanf("%d",&processltrs);
	scanf("%c",&space);
	while(processltrs--)
	{
		bool processed = false;
		bool toclear = false;
		int j = 0;
		int k = 0;
		scanf("%c",&ltr);
		for(j = 0 ; j < combcount ; j++)
		{
			if(((comb[j][0] == ltr) && (comb[j][1] == out[outcount - 1])) || ((comb[j][1] == ltr) && (comb[j][0] == out[outcount - 1])))
			{
				out[outcount - 1] = comb[j][2];
				processed = true;
				break;
			}
		}
		if(processed)
		{
			continue;
		}
		j = 0;
		for(j = 0 ; j < oppscount ; j++)
		{
			if(opps[j][0] == ltr)
			{
				for(k = 0; k < outcount ; k++)
				{
					if(opps[j][1] == out[k])
					{
						toclear = true;
						break;
					}
				}
			}
			k = 0;
			if(!toclear)
			{
				if(opps[j][1] == ltr)
				{
					for(k = 0; k < outcount ; k++)
					{
						if(opps[j][0] == out[k])
						{
							toclear = true;
							break;
						}
					}
				}
			}
			k = 0;
			if(toclear)
			{
				for(k = 0; k < outcount ; k++)
				{
					out[k] = '0';					
				}
				outcount = 0;
				processed = true;
			}
		}
		if(processed)
		{
			continue;
		}
		out[outcount] = ltr;
		outcount += 1;
	}

	i = 0;
	printf("Case #%d: [",++caserunning);
	//printloop
	for(i = 0; i < outcount ; i++)
	{
		if(i == (outcount - 1))
		{
			printf("%c",out[i]);
		}
		else
		{
			printf("%c, ",out[i]);
		}
	}
	printf("]\n");
	
  }


  return 0;
}

