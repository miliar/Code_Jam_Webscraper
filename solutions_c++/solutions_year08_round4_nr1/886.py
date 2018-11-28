// Was build with STL libraries of standard MS VisualStudio 2005 SP1
// Target application was console win 32 application with multibite character set setting. 
// Used software were licensed to Align Technology Inc

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <math.h>
#include <queue>
#include <set>
#include <list>
#define M_PI       3.14159265358979323846

/////////////////////////////////////////////////////////////////

struct NODE
{
	int G, C, I;
	NODE *L, *R;
	int MC[2];
	void build()
	{
		if(L)
		{
			L->build();
			R->build();
			if(G == 0)
			{
				I = ((L->I) | (R->I));
			}
			else
			{
				I = ((L->I) & (R->I));
			}
			MC[I] = 0;
			MC[1-I] = -1;
			for(int OP1 = 0; OP1 < 2; OP1++)
			{
				if(C == 0 && OP1 ==1)
					continue;
				int GM = G;
				if(OP1)
					GM = 1-GM;
				for(int OP2 = 0; OP2 < 2; OP2++)
				{
					int I1 = L->I;
					if(OP2)
						I1 = 1-I1;
					for(int OP3 = 0; OP3 < 2; OP3++)
					{
						int I2 = R->I;
						if(OP3)
							I2 = 1-I2;
						int RS;
						if(GM == 0)
							RS = I1|I2;
						else
							RS = I1&I2;
						int CNT = - 1;
						if(RS == 1-I && L->MC[I1]!= -1&&R->MC[I2]!=-1)
						{
							CNT = L->MC[I1] + R->MC[I2];
							if(OP1)
								CNT++;
							if(MC[1-I] == -1 || MC[1-I] > CNT)
								MC[1-I] = CNT;
						}
					}
				}
			}
		}
		else
		{
			MC[I] = 0;
			MC[1-I] = -1;
		}
	}
};

int main(int argc, char* argv[])
{
	int numOfCases;
	scanf("%d", &numOfCases);
	for(int cn = 0; cn < numOfCases; cn++)
	{
		int nodesCount, desired;
		scanf("%d%d", &nodesCount, &desired);

		std::vector<NODE> nodes(nodesCount);
		for(int i = 0; i < nodesCount; i++)
		{
			if(i < (nodesCount-1)/2)
			{
				nodes[i].L = &(nodes[i*2+1]);
				nodes[i].R = &(nodes[i*2+2]);
				scanf("%d%d", &(nodes[i].G), &(nodes[i].C));
			}
			else
			{
				nodes[i].L = 0;
				nodes[i].R = 0;
				scanf("%d", &(nodes[i].I));
			}
		}

		nodes[0].build();
		if(nodes[0].MC[desired]!=-1)
		{
			std::cout << "Case #" << (cn+1) << ": " << nodes[0].MC[desired] << "\n";
		}
		else
		{
			std::cout << "Case #" << (cn+1) << ": IMPOSSIBLE\n";
		}
	}
	return 0;
}

