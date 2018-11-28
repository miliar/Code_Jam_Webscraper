#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;


struct GROUP
{
	int size;
	int count;
	int first_index;
};

struct GROUP group[1005];


main()
{
	int T,R,N,k,r,CASE=0;
	int i,j,rider,start;
	int cycle_length, cycle_possible;
	__int64 earning,temp;

//	freopen("C-small-attempt0.in","r",stdin);
//	freopen("C-small-attempt0.out","w",stdout);

	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);


	scanf("%d",&T);

	while(T--)
	{
		CASE++;

		scanf("%d %d %d",&R, &k, &N);

		for(i=0; i<N; i++)
		{
			scanf("%d",&j);

			group[i].size = j;
			group[i].count = 0;
			group[i].first_index = 0;
		}

		i = 0;
		r = 0;
		earning = 0;
		while(group[i].first_index != 1 && r+1 <= R)
		{
			rider = 0;
			group[i].first_index++;
			r++;
			start = i;

			while(rider+group[i].size <= k)
			{				
				rider += group[i].size;
				
				group[i].count++;
								
				i = (i+1)%N;

				if(i == start)
					break;
			}
			
			earning += rider;
		}

		for(j=0; j<N; j++)
		{
			group[j].first_index = 0;
			group[j].count = 0;
		}

		if(r != R)//more trips left
		{
			cycle_length = 0;
			temp = 0;
			while(group[i].first_index != 1 && r+1 <= R)
			{
				rider = 0;
				group[i].first_index++;
				r++;
				cycle_length++;
				start = i;

				while(rider+group[i].size <= k)
				{				
					rider += group[i].size;					
					group[i].count++;
					i = (i+1)%N;
					if(i == start)
						break;
				}				

				temp += rider;
			}

			earning += temp;

			if(r != R)
			{
				cycle_possible = (R-r)/cycle_length;

				earning += (cycle_possible*temp);

				r = r + (cycle_possible*cycle_length);

				while(r+1 <= R)
				{
					rider = 0;
					r++;
					start = i;
					while(rider+group[i].size <= k)
					{				
						rider += group[i].size;					
						i = (i+1)%N;
						if(i == start)
							break;
					}				

					earning += rider;
				}
			}
		}

		
		printf("Case #%d: %I64d\n",CASE,earning);

	}




}