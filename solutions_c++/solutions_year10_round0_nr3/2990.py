// Rollercoaster.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	int T;					//Number of Test Cases
	
	int R;					//Roller Coaster Goes
	long int k;					//Capacity of Coaster
	int N;					//Space Seperated Ints

	FILE *input = fopen("C-small-attempt0.in","r");
	FILE *output = fopen("C-small-attempt0.out","w");

	fscanf(input,"%d",&T);	//Read Number of Test Cases

	/////////////// LOOP THROUGH TEST CASES
	for(int t=0;t<T;t++)
	{
		fscanf(input,"%d",&R); fscanf(input,"%ld",&k); fscanf(input,"%d",&N);

		int *Queue = (int*)malloc(sizeof(int)*N);
		for(int n=0;n<N;n++)
		{
			int group_size; 
			fscanf(input,"%d",&group_size);
			*(Queue+n) = group_size;
		}
		printf("\n");

		/////////////////////////////////////
		// Begin Logic
		/////////////////////////////////////
		int total = 0;
		int next=0;						//n specifes next group
		
		for(int r=0;r<R;r++)			//Number of Times Rollercoaster Goes
		{
			int current_capacity = k;		//Current Capacity of Ride = Total Capacity
			int group_count=0;				//Keep Track of Groups on Coaster
			// if next < total cap
			// take passengers decrease total cap
			// repeat

			while(1)
			{
				int Queue_n = *(Queue+next);
				
				if( *(Queue+next) <= current_capacity )	// take passengers
				{
					total = total + *(Queue+next);
					current_capacity = current_capacity - *(Queue+next);
					next++;							//increment next;
					group_count=group_count+1;
					if(next==N)						//if next reaches upper limit
						next=0;						//reset next=0
					if(group_count==N)				// All Groups have gone
					{
						group_count==0;
						break;
					}
				}
				else
					break;
			}
		}
		fprintf(output,"Case #%d: %d\n",(t+1),total);
		free(Queue);
	}
	
	fclose(input);
	fclose(output);
	return 0;
}

