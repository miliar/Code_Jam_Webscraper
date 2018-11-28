#include <stdio.h>
#include <string.h>
#include <stdlib.h> 

#define INPUT_FILE_NAME "B-small-attempt2.in"
#define OUTPUT_FILE_NAME "B-small-attempt2.out"

//#define INPUT_FILE_NAME "B-large-practice.in"
//#define OUTPUT_FILE_NAME "B-large-practice.out"


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
static char cobined[26][2];
static char opossit[2][26];
void update_data()
{
	int num_of_cmb;
	int num_of_ops;
memset(cobined,'\0',52);
memset(&opossit[0][0],'\0',26);
memset(&opossit[1][0],0,26);
	//fgetc(input_file);

fscanf(input_file,"%d",&num_of_cmb);
fgetc(input_file);
while(num_of_cmb>0)
{
	char a,b;
	a= fgetc(input_file);
	b= fgetc(input_file);
	cobined[a-'A'][0]=b;
cobined[b-'A'][0]=a;
    cobined[b-'A'][1]=fgetc(input_file);
	cobined[a-'A'][1]=cobined[b-'A'][1];
   fgetc(input_file);
   num_of_cmb--;
}
//fgetc(input_file);

fscanf(input_file,"%d",&num_of_ops);

fgetc(input_file);
while(num_of_ops>0)
{
	char a,b;
	a= fgetc(input_file);
	b= fgetc(input_file);
	opossit[0][a-'A']=b;
   opossit[1][a-'A']=0;
    opossit[0][b-'A']=a;
   opossit[1][b-'A']=0;
   fgetc(input_file);
   num_of_ops--;
}
/*for(int k=0;k<26;k++)
{
printf("cobined[%d][0]=%c opossit[0][%d]=%c ",k,cobined[k][0],k,opossit[0][k]);
printf("cobined[%d][1]=%c opossit[1][%d]=%c\n",k,cobined[k][1],k,opossit[1][k]);
}
printf("##################################################\n\n\n");*/
}
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
	//char line[1000];
	char *line_new;
	//char delimiter[501];
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
	update_data();
	printf("case=%d\n",n+1);
	fscanf(input_file,"%d",&i_in);
	
	line_new = (char*)malloc(i_in);
    fgetc(input_file);
	for(i=0;i<i_in;i++ )
	{
		input_char = fgetc(input_file);
		if((l>0)&&(cobined[line_new[l-1]-'A'][0]==input_char))
		{
			if(opossit[1][opossit[0][line_new[l-1]-'A']-'A']>0)
			 opossit[1][opossit[0][line_new[l-1]-'A']-'A']--;
			line_new[l-1]=cobined[line_new[l-1]-'A'][1];
			
		}
		else if(opossit[1][input_char-'A']>0)
		{
			l=0;
			memset(&opossit[1][0],0,26);
		}
		else
		{
			line_new[l] = input_char;
			//if(cobined[list_to[l]-'A'][0]!='\0')
			//  cobined[cobined[list_to[l]-'A'][0]-'A'][1]=1;
		   if(opossit[0][line_new[l]-'A']!='\0')
			 opossit[1][opossit[0][line_new[l]-'A']-'A']++;
		   l++;
		}
	/*	for(int k=0;k<26;k++)
{
printf("cobined[%d][0]=%c opossit[0][%d]=%c ",k,cobined[k][0],k,opossit[0][k]);
printf("cobined[%d][1]=%c opossit[1][%d]=%c\n",k,cobined[k][1],k,opossit[1][k]);
}*/
//printf("##################################################\n\n\n");

	}
	r=0;
fputc('[',output_file);

	while(l>r)
	{

		if(r!=0)fputc(' ',output_file);
		fputc(line_new[r],output_file);



	r++;
	if(r<l)fputc(',',output_file);
	}
	fputc(']',output_file);
	fprintf(output_file,"\n");
	free(line_new);
}

