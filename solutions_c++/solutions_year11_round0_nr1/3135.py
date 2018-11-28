#include <stdio.h>
#include <iostream>
#include <cmath>

#define REP(i,n) for(i=0; i < n ; i++)
using namespace std;

int main()
{
	int T, N, i=0, oS=1, bS=1, total=0, ocs=0, bcs=0;
	FILE *iFile, *oFile;
	iFile = fopen("A-large.in", "r+");
	oFile = fopen("output.out", "w+");
	fscanf(iFile, "%d", &T);
	REP(i, T)
	{
		int j=0, P; 
		char R;
		fscanf(iFile, "%d", &N);
		oS=1; bS=1; total=0; ocs=0; bcs=0;
		REP(j, N)
		{
			fscanf(iFile, " %c %d", &R, &P);
			if(R=='O')
			{
				if(oS == P || ocs >= abs((float)(P-oS)))
				{
					total++;
					bcs++;
					ocs=0;
					oS=P;
				}
				else
				{
					if(ocs < abs((float)(P-oS)))
					{
						total+= (abs((float)(P-oS)) - ocs) + 1;
						bcs+= (abs((float)(P-oS)) - ocs) + 1;
					}
					else
					{
						total+= (abs((float)(P-oS))) + 1;
						bcs+= (abs((float)(P-oS))) + 1;
					}
					ocs=0;
					oS=P;
				}
				cout << total << endl;
			}
			else
			{
				if(bS == P || bcs >= abs((float)(P-bS)))
				{
					total++;
					ocs++;
					bcs=0;
					bS=P;
				}
				else
				{
					if(bcs < abs((float)(P-bS)))
					{
						total+= (abs((float)(P-bS)) - bcs) + 1;
						ocs+= (abs((float)(P-bS)) - bcs) + 1;
					}
					else
					{
						total+= (abs((float)(P-bS))) + 1;
						ocs+= (abs((float)(P-bS))) + 1;
					}
					bcs=0;
					bS=P;
				}
				cout << total << endl;
			}
		}
		cout << "-----" << i+1 << endl;
		fprintf(oFile, "Case #%d: %d\n", i+1, total);
	}
	return 0;  
}
