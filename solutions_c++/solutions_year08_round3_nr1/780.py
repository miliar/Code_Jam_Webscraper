#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <map>
#include <vector>
#include <string>

using namespace std;

int compare(const void *v1, const void *v2)
{
	int *e1 = (int*) v1;
	int *e2 = (int*) v2;
	if(*e1== *e2) return 0;
	if(*e1< *e2) return 1;
	if(*e1> *e2) return -1;
}

void usage(char *exename)
{
	printf("Usage:\n");
	printf("%s <input file>\n", exename);
}

class V
{
public:
	int m_x;
	int m_y;

	V(int vx, int vy):m_x(vx),m_y(vy){};
};


int P, K, L;
int *narr;


int solve()
{
	int i;
	qsort(narr, L, sizeof(int), compare);
	int factor = 1;
	int counter = 0;

	for(i=0; i<L; i++)
	{
		counter+=narr[i]*factor;				
		if((i+1)%K==0) factor++;
	}

	return counter;
}

int main(int argc, char *argv[])
{
	if(argc!=2)
	{
		usage(argv[0]);
		return 1;
	}

	FILE *inf;
	int i, j;
	FILE *outf;
	int iNcases;

	inf = fopen(argv[1], "r");
	if(inf==NULL) return 1;

	char line[128];
	fgets(line, 128, inf);
	sscanf(line, "%d", &iNcases);
	int k;
	int nn;
	int ans;

	for(k=0; k<iNcases; k++)
	{
		fgets(line, 128, inf);
		sscanf(line, "%d %d %d", &P, &K, &L);

		narr = new int[L];
		for(i=0; i<L; i++)
		{
			fscanf(inf, "%d ", &nn);
			narr[i] = nn;
		}
			
		ans = solve();
		printf("Case #%d: %d\n", k+1, ans);
	}

}
