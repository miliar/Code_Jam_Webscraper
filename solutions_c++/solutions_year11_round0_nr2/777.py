#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
using namespace std;

int main () {
    FILE *fin  = fopen ("Magicka.in", "r");
    FILE *fout = fopen ("MagickaL.out", "w");
    int T;
    fscanf(fin, "%d", &T);
    for(int caseN = 1; caseN<=T; caseN++)
    {
		int C;
		fscanf(fin, "%d", &C);
		char combine[30][30];
		memset(combine, 0, sizeof(combine));
		for(int i=0; i<C; i++)
		{
			char c1, c2, c3;
			fscanf(fin, " %c%c%c", &c1, &c2, &c3);
			combine[c1-65][c2-65] = combine[c2-65][c1-65] = c3;
		}
		
		int O;
		fscanf(fin, "%d", &O);
		bool opposed[30][30];
		memset(opposed, 0, sizeof(opposed));
		for(int i=0; i<O; i++)
		{
			char c1, c2;
			fscanf(fin, " %c%c", &c1, &c2);
			opposed[c1-65][c2-65] = opposed[c2-65][c1-65] = true;
		}
		
		int howMany[30];
		memset(howMany, 0, sizeof(howMany));
		vector<char> elements;
		
		int N;
		fscanf(fin, "%d ", &N);
		//printf("(%d %d %d)\n", C, O, N);
		for(int i=0; i<N; i++)
		{
			char e;
			fscanf(fin, "%c", &e);
			while(e>0)
			{
				//printf("%c", e);
				if(!elements.empty() && combine[e-65][elements.back()-65]>0)
				{
					e=combine[e-65][elements.back()-65];
					howMany[elements.back()-65]--;
					elements.pop_back();
				}
				else
				{
					bool op = false;
					for(int j=0; j<30 && !op; j++)
						op = (howMany[j]>0 && opposed[j][e-65]);
					if(op)
					{
						memset(howMany, 0, sizeof(howMany));
						elements.clear();
						//printf(" OPPOSED");
					}
					else
					{
						elements.push_back(e);
						howMany[e-65]++;
					}
					e=0;
				}
			}
		}	
		int S = elements.size();
		fprintf(fout, "Case #%d: [", caseN);
		if(S>0)
			fprintf(fout, "%c", elements[0]);
		for(int i=1; i<S; i++)
		{
			fprintf(fout, ", %c", elements[i]);
		}
		fprintf(fout, "]\n");
	}
    return 0;
}
