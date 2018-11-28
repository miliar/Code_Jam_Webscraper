#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;

main()
{
	int i,j,k;
	int N, CASE=0;
	char in[10000];
	char src[] = "welcome to code jam";
	vector <int> pos[19];
	vector <int> count[19];

	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);


	N = atoi(gets(in));

	while(N--)
	{
		CASE++;

		gets(in);

		for(i=0; i<19; i++)
		{
			pos[i].clear();
			count[i].clear();
		}

		for(i=0; i<19; i++)
		{
			for(j=0; in[j]; j++)
				if(in[j] == src[i])
				{
					pos[i].push_back(j);
					count[i].push_back(0);
				}
		}

		for(i=0; i<count[0].size(); i++)
			count[0][i] = 1;

		for(i=1; i<19; i++)
		{
			for(j=0; j<pos[i-1].size(); j++)
			{
				for(k=0; k<pos[i].size(); k++)
				{
					if(pos[i][k] > pos[i-1][j])
						count[i][k] = (count[i][k]+count[i-1][j]) % 10000;
				}
			}
		}

		for(i=j=0; i<count[18].size(); i++)
			j = (j+count[18][i]) % 10000;

		if(j < 10)
			sprintf(in,"000%d",j);
		else if(j < 100)
			sprintf(in,"00%d",j);
		else if(j < 1000)
			sprintf(in,"0%d",j);
		else
			sprintf(in,"%d",j);

		printf("Case #%d: %s\n",CASE,in);

	}

}
