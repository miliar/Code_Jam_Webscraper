#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;

char words[5005][20];
char in[1000000];


main()
{
	int L,D,N,CASE=0;
	int i,j,k;

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	vector<string> res, res_temp;

	scanf("%d %d %d",&L,&D,&N);

	for(i=0; i<D; i++)
	{
		scanf("%s",words[i]);
	}

	while(N--)
	{
		CASE++;

		res.clear();
		for(i=0; i<D; i++)
			res.push_back(words[i]);
	
		scanf("%s",in);

		for(i=j=0; i<L; i++,j++)
		{
			res_temp.clear();

			if(in[j] == '(')
			{
				for(j++; in[j] != ')'; j++)
				{
					int total = res.size();
					for(k=0; k<total; k++)
					{
						if(res[k][i] == in[j])
							res_temp.push_back(res[k]);
					}
				}
			}
			else
			{
				int total = res.size();
				for(k=0; k<total; k++)
				{
					if(res[k][i] == in[j])
						res_temp.push_back(res[k]);
				}
			}
			
			res = res_temp;
			
		}

		printf("Case #%d: %d\n",CASE, res.size());

	}




}