#include<iostream>
#include<fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
		
	freopen("B-large.in","rt",stdin);
	freopen("output2.out","wt",stdout);
	int totalCases;
	scanf("%d",&totalCases);
	char ch;
	
	int score,N,S,p;
	scanf("%c",&ch);	
	for(int i=0;i<totalCases;i++)
	{
		scanf("%d",&N);
		scanf("%c",&ch);
		scanf("%d",&S);
		scanf("%c",&ch);
		scanf("%d",&p);
		int times=0;
		int output=0;
		for(int j=0;j<N;j++)
		{
			scanf("%c",&ch);
			scanf("%d",&score);
			if(score<(p+(p-2)+(p-2))||  score < p)
			{
				continue;
			}	
			if(S>0)
			{	
				if(score== (p+(p-2)+(p-2))|| score == (p+(p-2)+(p-1)))
				{	
					S--;
				}				
				output=output+1;
				continue;
			}
			else
			{
				if(score== (p+(p-2)+(p-2))|| score == (p+(p-2)+(p-1)))
				{						
					continue;
				}
				output=output+1;
				continue;
			}
			
		}
		printf("Case #%d: %d",(i+1),output);
		printf("\n");
	}
}
