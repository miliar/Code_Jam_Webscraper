#include <stdio.h>
#include <stdlib.h>

#define INPUT_FILE "C-large.in"
#define MAX_LINE_SIZE (1<<16)


void FillGroups(unsigned int const N, char const * const line, unsigned int *groups)
{
	unsigned int n, gs, index=0;
	
	//fill an array to hold the group sizes
	for(n=0; n<N; n++)
	{
		//read next group size from line
		sscanf(&line[index], "%u", &gs);
		groups[n] = gs;
		
		//find next 'space'
		while(line[index]!= ' ')
			index++;
		index++;
	}
}


long long int CalcProfit(unsigned int const N, 
						 unsigned int const R, 
						 unsigned int const k, 
						 unsigned int const * const groups)
{
	unsigned int r, first_in_line=0;
	long long int profit = 0;
	
	//take the roller coaster for R runs
	for(r=0; r<R; r++)
	{
		unsigned int passengers=0;
		unsigned int const first_in_coaster = first_in_line;
		
		//fill the roller coaster
		while(groups[first_in_line] <= (k-passengers))
		{
			passengers += groups[first_in_line];
			
			//next group is now first in line
			first_in_line++;
			
			//check if the end of the queue is reached (wrap arround)
			if(first_in_line == N)
				first_in_line = 0;
			
			//check if the next group in line is already in the roller coaster
			if(first_in_line == first_in_coaster)
				break;
		}
		
		profit += passengers;
	}
	
	return profit;
}


int main()
{
	char line[MAX_LINE_SIZE], *line_error;
	unsigned int T, tc, R, k, N;
	unsigned int groups[1000];
	long long int profit;
	
	//read input file
	FILE* fp = fopen(INPUT_FILE, "r");
	if(!fp)
	{	
		fprintf(stderr, "Error opening file!\n");
		return -3;
	}

	//read first line to determine T
	line_error = fgets(line, MAX_LINE_SIZE, fp);
	if(!line_error)
	{	
		fprintf(stderr, "Error reading file!\n");
		return -3;
	}
	sscanf(line, "%d", &T);
	//printf("T: %d\n", T);
	
	//do all T test cases
	for(tc=1; tc<=T; tc++)
	{
		//find R (runs per day), k (roller coaster size) and N (groups)
		line_error = fgets(line, MAX_LINE_SIZE, fp);
		if(!line_error)
		{	
			fprintf(stderr, "Error reading file!\n");
			return -3;
		}
		sscanf(line, "%d %d %d", &R, &k, &N);
		//printf("R, k, N: %d %d %d\n", R, k, N);
		
		//find all group sizes
		line_error = fgets(line, MAX_LINE_SIZE, fp);
		if(!line_error)
		{	
			fprintf(stderr, "Error reading file!\n");
			return -4;
		}
		
		//parse group sizes
		FillGroups(N, line, groups);
		
		//calculate profit
		profit = CalcProfit(N, R, k, groups);
		printf("Case #%u: %lld\n", tc, profit);
	}

	fclose(fp);
	return 0;
}

