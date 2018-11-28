#include <stdio.h>
#include <string.h>
#include <stdlib.h> 

#define INPUT_FILE_NAME "A-large.in"
#define OUTPUT_FILE_NAME "A-large.out"

//#define INPUT_FILE_NAME "A-large-practice.in"
//#define OUTPUT_FILE_NAME "A-large-practice.out"


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
     char stuff[25];
     int test_num;

	int i;
	 gets(stuff);
   output_file = fopen (OUTPUT_FILE_NAME, "w"); 
   input_file = fopen (INPUT_FILE_NAME, "r");  /* open the file for reading */
	n =get_case_num();
	printf ("number of cases: %d\n", n);
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
	printf("hello world %s",stuff);


	 scanf("file name:%s",stuff);
	 while(0);
}

int get_case_num()
{
	char line[80];
	int case_num;
	fgets(line, 80, input_file);
	sscanf(line, "%d", &case_num);
	return case_num;
}
int time_to_get_n_do(int prev,int next)
{
	return ((prev-next)>0)?(prev-next+1):(next-prev+1);
}
static int o_extra_time=0,b_extra_time=0;

static int total_time;
int algo(int prev,int next,bool is_o)
{
	
	int step_time=0;
	if(is_o)
	{
		step_time = ((time_to_get_n_do(prev,next)-o_extra_time>0)?(time_to_get_n_do(prev,next)-o_extra_time):1);
		b_extra_time +=step_time;
		o_extra_time=0;
	}
	else	{
		step_time = ((time_to_get_n_do(prev,next)-b_extra_time>0)?(time_to_get_n_do(prev,next)-b_extra_time):1);
		o_extra_time +=step_time;
		b_extra_time=0;
	}
	return step_time;
}
void solve_case(int n)
{
	char line[1000];
	char *line_new;
	char delimiter[501];
	char input_char;
	int i_in;
	int* store_items;
	int select_low=1;
	int select_high=2;
	int last_word_end=0,i=0,j=0,r,k,l=0;
	bool is_o = false;
	char num_of_last=11;
	int o_prev=1,b_prev=1;
	//fgets(line, 1000, input_file);
	fprintf(output_file,"Case #%d: ",n+1);
	fscanf(input_file,"%d",&i_in);
   total_time=0;
   o_extra_time=0;
   b_extra_time=0;
	for(i=0;i<i_in;i++ )
	{
		if(fgetc(input_file)==' ')
		{
			if(fgetc(input_file)=='O')
				is_o=true;
			if(fgetc(input_file)==' ')
			{
				fscanf(input_file,"%d",&select_low);
				total_time+=algo(is_o?o_prev:b_prev,select_low,is_o);
				if(is_o)
					o_prev=	select_low;
				else
					b_prev=	select_low;
			}
			is_o=false;
		}	
	}
	fprintf(output_file,"%d\n",total_time);
}

