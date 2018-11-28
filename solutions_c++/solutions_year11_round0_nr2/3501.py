#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;


main()
{
	int T,CASE=0;
	int i,j,k,l;

	int C,D,N;
	char comb[50][4];
	char oppose[50][3];
	char invoke[200];

	char buf[200];

	vector <char> out;

	char c1, c2;
	int done;


//	freopen("B-small-attempt0.in","r",stdin);
//	freopen("B-small-attempt0.out","w",stdout);

//	freopen("B-large.in","r",stdin);
//	freopen("B-large.out","w",stdout);


	scanf("%d",&T);

	while(T--)
	{
		CASE++;

		scanf("%s",buf);
		sscanf(buf,"%d",&C);
		for(i=0; i<C; i++)
			scanf("%s",comb[i]);

		scanf("%s",buf);
		sscanf(buf,"%d",&D);
		for(i=0; i<D; i++)
			scanf("%s",oppose[i]);

		scanf("%s",buf);
		sscanf(buf,"%d",&N);
		scanf("%s",invoke);


		out.clear();
		for(i=0; i<N; i++)
		{
			out.push_back(invoke[i]);

			if(out.size() > 1)
			{
				c1 = out[out.size()-2];
				c2 = out[out.size()-1];

				done = 0;

				for(j=0; j<C && !done; j++)
					if( (comb[j][0] == c1 && comb[j][1] == c2) || (comb[j][0] == c2 && comb[j][1] == c1) )
					{
						out.pop_back();
						out.pop_back();

						out.push_back(comb[j][2]);
						
						done = 1;
					}		

				for(j=0; j<D && !done; j++)
					for(k=out.size()-2; k>=0 && !done; k--)
						if( (c2 == oppose[j][0] && out[k] == oppose[j][1]) || (c2 == oppose[j][1] && out[k] == oppose[j][0]) )
						{
							out.clear();
							done = 1;
						}

			}

		}


		printf("Case #%d: [",CASE);

		for(i=0; i<out.size(); i++)
		{
			if(i == 0)
				printf("%c",out[i]);
			else
				printf(", %c",out[i]);
		}
		
		printf("]\n");

	}




}