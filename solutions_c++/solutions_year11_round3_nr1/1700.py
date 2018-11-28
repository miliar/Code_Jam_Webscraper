#include <stdio.h>
#include <string.h>
#include <stdlib.h> 

#define INPUT_FILE_NAME "A-large (1).in"
#define OUTPUT_FILE_NAME "A-large (1).out"

static FILE *input_file;
static FILE *output_file;

int get_case_num();
void solve_case(int n);


void main()
{
	   int n;
   long elapsed_seconds;
   char line[80];

     int test_num;

	int i;
	
   input_file = fopen (INPUT_FILE_NAME, "r");  /* open the file for reading */
   output_file = fopen (OUTPUT_FILE_NAME, "w"); 


	n =get_case_num();

	i=0;
   while(n>i)
   {
	   solve_case(i);

	   	 i++;
   }
   fclose(input_file);  /* close the file prior to exiting the routine */
  
   fclose(output_file);	
}

int get_case_num()
{
	char line[80];
	int case_num;
	fgets(line, 80, input_file);
	sscanf(line, "%d", &case_num);
	return case_num;
}
#define MAX_LINE_LEN	12
void solve_case(int n)
{

	char line[MAX_LINE_LEN];
	long N_max=0,p_P[200],p_Prev,v_V[200];
    int* in;
		int team_num,i=0,j=0,k=0,l=0,tmp;
			double sum_2=0;
			char table[50][50];
			double result[100];
			double result_wp[100];
			double result_owp[100];
			double result_oowp[100];
			double total_games[100];
			double total_win[100];
			int c_C,r_R;
	//char *line_new;
	//char delimiter[501];
	//char input_char;

//	int* store_items;
//	int select_low=1;
//	int select_high=2;
//	int last_word_end=0,i=0,j=0,r,k,l=0;
//	bool is_o = false;
//	char num_of_last=11;
//	int o_prev=1,b_prev=1;

	fgets(line, MAX_LINE_LEN, input_file);
	
//	build_sorted();
	sscanf(line,"%d %d",&r_R,&c_C);
	
//fgets(line, MAX_LINE_LEN, input_file);
//fgetc(input_file);
	//	sscanf(line,"%d %d",&p_P[0],&v_V[0]);
		//sscanf(line,"%d",&v_V);

i=0;
j=0;
while(i<r_R)
	{
		j=0;
		while(j<c_C)
		{
		  table[i][j]=fgetc(input_file);
		  j++;
		}
		fgetc(input_file);
		i++;
	}
i=0;
j=0;
while(i<r_R)
{
	j=0;
	while(j<c_C)
		{
		  
			if(table[i][j]=='#')
			{
				if((j==c_C-1)||(i==r_R-1)||(table[i+1][j]!='#')||(table[i+1][j+1]!='#')||(table[i][j+1]!='#'))
				{
				
				fprintf(output_file,"Case #%d: \n",n+1);
					fprintf(output_file,"Impossible\n",n+1);
					return;
				}
				else
				{
				table[i][j]='/';
				table[i][j+1]='\\';
					table[i+1][j]='\\';
					table[i+1][j+1]='/';
				}
			
			}

		  j++;
		}
i++;
}
i=0;
fprintf(output_file,"Case #%d: \n",n+1);
while(i<r_R)
{
	
	j=0;
	while(j<c_C)
		{
					fprintf(output_file,"%c",table[i][j]);
								
			

		  j++;
		}
		fprintf(output_file,"\n");
i++;
}
   //fprintf(output_file,"%4.6f\n",sum);
	//free(in);
}

