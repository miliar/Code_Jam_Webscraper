// Practice.cpp : Defines the entry point for the console application.
//


#include <cmath>
#include <cstring>

#include "stdio.h"
#include "stdlib.h"

#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
	FILE *infp = NULL, *outfp = NULL;
	infp = fopen("c:\\Ashay_Backup\\input.txt","r");
	outfp = fopen("C:\\Ashay_BACKUP\\output.txt", "w+");
	if(infp==NULL || outfp==NULL)
	{
		printf("File read error\n");
		exit(1);
	}

	char buffer[50];
	char* wordptr;	
	
	fgets(buffer, 49, infp);
	long T = atol(buffer);
	long long earnings = 0;

	long R = 0;
	long k = 0;
	int N = 0;
	vector<long> vg;
	vector<pair<int,long>> occupants;
	long seatsremaining;

	for(long i = 1; i <= T; i++)
	{
		earnings = 0;
		if(fgets(buffer, 49, infp) == NULL)
			break;

		wordptr = strtok(buffer, " ");
		R = atol(wordptr);
		wordptr = strtok(NULL, " ");
		k = atol(wordptr);
		wordptr = strtok(NULL, " ");
		N = atoi(wordptr);

		if(fgets(buffer, 49, infp) == NULL)
			break;
		for(int gi = 0; gi < N; gi++)
		{
			if(gi==0)
			{
				wordptr = strtok(buffer, " ");
			}
			else
			{
				wordptr = strtok(NULL, " ");
			}
			vg.push_back( atol(wordptr) );
		}

		int ivg, itvg;
		for(ivg = 0; ivg < N; ivg++)
		{
			if(vg[ivg] > k)
			{
				break; // queue blocked
			}

			// find feasible batch from this group onwards
			seatsremaining = k;			
			for(itvg = ivg;;)
			{
				if(seatsremaining < vg[itvg])
				{
					break;
				}
				else
				{
					seatsremaining -= vg[itvg];
				}
				itvg++;
				if(itvg == N)
				{
					itvg = 0;
				}
				if(itvg == ivg)
				{
					break; // cannot use the same group again
				}
			}
			occupants.push_back(pair<int,long>(itvg,k-seatsremaining));
		}

		ivg = 0;
		for(long iR = 0; iR < R; iR++)
		{
			pair<int,long> nxtindex_occupants_pair = occupants[ivg];
			ivg = nxtindex_occupants_pair.first;
			earnings += nxtindex_occupants_pair.second;
		}

		fprintf(outfp, "Case #%i: %lld\n", i, earnings);
		occupants.clear();
		vg.clear();
	}

	fclose(infp);
	fclose(outfp);

	return 0;
}