#include <stdio.h>
#include <memory.h>
#include <algorithm>

using namespace std;

struct data
{
	int depart, arrive;
	bool used, type;
};

int compare(data *n1, data *n2) {
   return n1->depart > n2->depart;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int cases, turn, na, nb, houra, hourb, minutea, minuteb, i, max, used, j, idx;
	int traina, trainb, loop, last, num = 1, ctr;
	data all[200], tmp;

	scanf("%i\n", &cases);
	while(cases--)
	{
		scanf("%i %i %i", &turn, &na, &nb);

		for(ctr = 0; ctr < na; ctr++)
		{
			scanf("%2d:%2d %2d:%2d\n", &houra, &minutea, &hourb, &minuteb);
			all[ctr].depart = houra * 60 + minutea;
			all[ctr].arrive = hourb * 60 + minuteb;
			all[ctr].used = 0;
			all[ctr].type = 0;
		}
		for(i = 0; i < nb; i++)
		{
			scanf("%2d:%2d %2d:%2d\n", &houra, &minutea, &hourb, &minuteb);
			all[ctr].depart = houra * 60 + minutea;
			all[ctr].arrive = hourb * 60 + minuteb;
			all[ctr].used = 0;
			all[ctr].type = 1;
			ctr++;
		}

		// sort data
		max = na + nb;
		for(i = 0; i < max; i++)
		{
			idx = i;
			for(j = i + 1; j < max; j++)
			{
				if(all[idx].depart > all[j].depart)
					idx = j;
			}

			if(i != idx)
			{
				tmp = all[idx];
				all[idx] = all[i];
				all[i] = tmp;
			}
		}

		used = 0;		
		traina = trainb = loop = 0;
		last = -1;
		while(used < max)
		{
			if(all[loop].used == 0)
			{
				if(last == -1)
				{
					last = loop;
					all[loop].used = 1;
					used++;
					if(all[loop].type == 0) traina++;
					else trainb++;
				}
				else
				{
					if(all[loop].type != all[last].type)
					{
						if(all[loop].depart >= all[last].arrive + turn)
						{
							all[loop].used = 1;
							last = loop;
							used++;
						}
					}
				}
			}

			loop++;
			if(loop == max) 
			{
				last = -1;
				loop = 0;
			}
		}
		printf("Case #%i: %i %i\n", num, traina, trainb);
		num++;
	}

	return 0;
}