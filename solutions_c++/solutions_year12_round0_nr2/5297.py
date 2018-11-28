#include <stdio.h>
#include <conio.h>


int main()
 {
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
    
	int nn;
	scanf("%d",&nn);

	for(int ni=0;ni<nn;ni++)
{
	printf("Case #%d: ",ni+1);
	int n,s,p;
	int answer=0;
	scanf("%d %d %d",&n,&s,&p);
	for(int i=0;i<n;i++)
	{
		int score;
		scanf("%d",&score);
		if(score == 0)
		{
			if(p == 0)
			{ answer++; }

		} else if(score == 30 || score == 29)
		{
			answer++;
		} else if(score%3 == 0)
		{
			if(score/3 >=p)
				answer++;
			else if(s>0 && score/3+1 >= p)
			{
				answer++;
				s--;
			}
		} else if(score%3 == 1)
		{
			if(score/3+1>=p)
				answer++;
		} else if(score%3 == 2)
		{
			if(score/3+1>=p)
				answer++;
			else if(s>0 && score/3+2 >= p)
			{
				answer++;
				s--;
			}
		}
	}
	
	printf("%d\n",answer);
}
	return 0;
 }