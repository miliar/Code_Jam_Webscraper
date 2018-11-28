#include <stdio.h>
#include <string.h>
#include <stdlib.h> 

#define INPUT_FILE_NAME "A-large.in"
#define OUTPUT_FILE_NAME "A-large.out"

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
#define MAX_LINE_LEN	5
void solve_case(int n)
{

	char line[MAX_LINE_LEN];
	unsigned long N_max;
    int* in;
		int team_num,i=0,j=0,k=0,l=0,tmp;
			double sum_2;
			char table[100][100];
			double result[100];
			double result_wp[100];
			double result_owp[100];
			double result_oowp[100];
			double total_games[100];
			double total_win[100];
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
	sscanf(line,"%d",&team_num);
	//i_in = get_case_num();
	//in = (int*)malloc(i_in*sizeof(int));
	//fscanf(input_file,"%dl",&N_max);
	//fscanf(input_file,"%d",&P_D);
	//fscanf(input_file,"%d",&P_G);

    while(team_num>i)
	{
		total_games[i]=0;
		total_win[i]=0;
		j=0;
		while(team_num>j)
		{
			table[i][j]=fgetc(input_file);
			
			if(table[i][j]!='.')
			{
				total_games[i]++;
				if(table[i][j]=='1')
					total_win[i]++;
			}
			
			j++;
		}
fgetc(input_file);
		//fscanf(input_file,"%d ",&in[i]);
		
		i++;
	}
	fprintf(output_file,"Case #%d: \n",n+1);
	while(team_num>k)
	{
		i=0;
		j=0;
		sum_2 =0.0;
		while(team_num>i)
		{
			if(table[k][i]=='1')
			{
				sum_2+=(total_win[i]/(total_games[i]-1));
			}
			else if (table[k][i]=='0')
			{
				sum_2+=((total_win[i]-1)/(total_games[i]-1));
			}

			//fscanf(input_file,"%d ",&in[i]);
			
			i++;
		}

		result_owp[k]=sum_2/total_games[k];
		k++;
	}
	k=0;
	while(team_num>k)
	{
		i=0;
		j=0;
		sum_2 =0.0;
		while(team_num>i)
		{
			if(table[k][i]!='.')
			{
				sum_2+=(result_owp[i]);
			}
						//fscanf(input_file,"%d ",&in[i]);
			
			i++;
		}

		result_oowp[k]=sum_2/total_games[k];
		k++;
	}
k=0;
	while(team_num>k)
	{
		
		sum_2 =(total_win[k]/total_games[k])/4 + result_owp[k]/2 +result_oowp[k]/4;
		fprintf(output_file,"%4.11f\n",sum_2);
		k++;
	}

    //fprintf(output_file,"%4.6f\n",sum);
	//free(in);
}

