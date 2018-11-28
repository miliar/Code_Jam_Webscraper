#include <stdio.h>
#include <string.h>
#include <stdlib.h> 

#define SMALL_INPUT_FILE_NAME "D-small-attempt1.in"
#define SMALL_OUTPUT_FILE_NAME "D-small-attempt1.out"

#define LARGE_INPUT_FILE_NAME "D-large.in"
#define LARGE_OUTPUT_FILE_NAME "D-large.out"


static FILE *input_file;
static FILE *output_file;

int get_case_num();
void solve_case(int n);


void main()
{
	   int n;
   long elapsed_seconds;
   char line[80];
   //FILE *fp;
     int stuff=1;
     int test_num;

	int i;
	//scanf("input type:%d",&stuff);
if(stuff==0)
{
   //output_file = fopen (SMALL_OUTPUT_FILE_NAME, "w"); 
   //input_file = fopen (SMALL_INPUT_FILE_NAME, "r");  /* open the file for reading */
}
else
{
   output_file = fopen (LARGE_OUTPUT_FILE_NAME, "w"); 
   input_file = fopen (LARGE_INPUT_FILE_NAME, "r");  /* open the file for reading */
}
	n =get_case_num();
	//printf ("number of cases: %d\n", n);
   /* elapsed.dta is the name of the file */
   /* "rt" means open the file for reading text */
	i=0;
   while(n>i)
   {
	   solve_case(i);

	   	 i++;
   }
   fclose(input_file);  /* close the file prior to exiting the routine */
  
   fclose(output_file);	
	//printf("hello world %s",stuff);


	 //scanf("file name:%s",stuff);
	// while(0);
}

int get_case_num()
{
	char line[80];
	int case_num;
	fgets(line, 80, input_file);
	sscanf(line, "%d", &case_num);
	return case_num;
}
void solve_case(int n)
{
	//char line[1000];
	//int sorted_arr[1000];
    int* in;
	//char *line_new;
	//char delimiter[501];
	//char input_char;
	int i_in,i=0,tmp;
//	int* store_items;
//	int select_low=1;
//	int select_high=2;
//	int last_word_end=0,i=0,j=0,r,k,l=0;
//	bool is_o = false;
//	char num_of_last=11;
//	int o_prev=1,b_prev=1;
	float sum=0;
	//fgets(line, 1000, input_file);
	fprintf(output_file,"Case #%d: ",n+1);
//	build_sorted();
	//fscanf(input_file,"%d",&i_in);
	i_in = get_case_num();
	in = (int*)malloc(i_in*sizeof(int));
    while(i_in>i)
	{
		fscanf(input_file,"%d ",&in[i]);
		in[i]--;
		if(i!=in[i])
		{
			sum++;
		}
		i++;
	}
	
    fprintf(output_file,"%4.6f\n",sum);
	free(in);
}

