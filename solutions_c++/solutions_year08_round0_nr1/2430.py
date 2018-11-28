#define MAX_WORD_LENGTH 105

#include "stdio.h"
#include "string.h"
#include "stdlib.h"

//GLOBALS
char *sorted_search_engines[100];
char queries[1000][MAX_WORD_LENGTH];
char *current_query;
bool flags_search_engine[100];

void unset_all_flags(int s)
{
	for(int i=0;i<s;i++)
		flags_search_engine[i] = false;
}
int bin(int l,int u)
{
	int m;
	m=(l+u)/2;
	//printf("value of m is %d\n",m);
	if(strcmp(current_query,sorted_search_engines[m])<0)
	{
		if(u>=l)
		{
			u=m-1;
			bin(l,u);
		}
		else	
		{	
			return -1;
		}
	}
	else if(strcmp(current_query,sorted_search_engines[m])>0)
	{
		if(l<=u)
		{
			l=m+1;
			bin(l,u);
		}
		else
		{
			return -1;
		}
	}
	else if(strcmp(current_query,sorted_search_engines[m])==0)
	{
		return m;
	}
}

int main(int argc, char* argv[])
{
	char word_buffer[MAX_WORD_LENGTH];
	int n;
	int s;
	int q;
	char search_engines[100][MAX_WORD_LENGTH];

	
	int no_of_switches=0;

	char output_string[50];

	FILE *in = NULL;
	FILE *out = NULL;

	in = fopen("c:\\input","r");
	out = fopen("c:\\output","w");

	if(in==NULL)
	{
		printf("File read error\n");
		exit(1);
	}


	fgets(word_buffer,MAX_WORD_LENGTH,in);
	printf("N read as      : %s",word_buffer);
	n = atoi(word_buffer);
	printf("N converted as : %d\n",n);

	char *temp_ptr;
	int /*outer*/engine_no;
	int no_of_striked_out_engines;

	for(int input_case=0;input_case<n;input_case++)
	{
		//read S
		fgets(word_buffer,MAX_WORD_LENGTH,in);
		printf("S read as      : %s", word_buffer);
		s = atoi(word_buffer);
		printf("S converted as : %d\n",s);
		//read search engines
		for(/*inner*/engine_no = 0; engine_no < s; engine_no++)
		{
			fgets(word_buffer,MAX_WORD_LENGTH,in);
			strcpy(search_engines[engine_no],word_buffer);
			printf("Search Engine read as   : %s", word_buffer);
			printf("Search Engine copied as : %s", search_engines[engine_no]);
		}
				
		//read Q
		fgets(word_buffer,MAX_WORD_LENGTH,in);
		printf("Q read as      : %s", word_buffer);
		q = atoi(word_buffer);
		printf("Q converted as : %d\n",q);
		//read queries
		for(int query_no=0; query_no < q; query_no++)
		{
			fgets(word_buffer,MAX_WORD_LENGTH,in);
			strcpy(queries[query_no],word_buffer);
			printf("Query read as   : %s", word_buffer);
			printf("Query copied as : %s", queries[query_no]);
		}

		if(q>1)
		{
			//sort search_engines and store
			for(engine_no = 0; engine_no < s; engine_no++)
			{
				sorted_search_engines[engine_no] = search_engines[engine_no];
			}
			for(int index_i=0;index_i<engine_no;index_i++)
			{
				for(int index_j=0;index_j<engine_no;index_j++)
				{
					if(strcmp(sorted_search_engines[index_i],sorted_search_engines[index_j])<0)
					{
						temp_ptr = sorted_search_engines[index_i];
						sorted_search_engines[index_i] = sorted_search_engines[index_j];
						sorted_search_engines[index_j] = temp_ptr;
					}
				}
			}
			printf("Sorted Search Engines are : \n");
			for(engine_no = 0; engine_no < s; engine_no++)
			{
				printf("%s",sorted_search_engines[engine_no]);
			}

			no_of_switches = 0;
			no_of_striked_out_engines=0;
			unset_all_flags(s);
			for(int query_no=0; query_no < q; query_no++)
			{
				
				
				//if striked out search engines == total no of search engines
				
				//binary search the matching search engine
				current_query = queries[query_no];
				printf("Current query is %s",current_query);
				engine_no = bin(0,s-1);
				printf("Search Engine found at %d\n",engine_no);

				//strike out the search engine as not usable
				if(flags_search_engine[engine_no]==false)
				{
					flags_search_engine[engine_no] = true;
					no_of_striked_out_engines++;
			
					//check if the count of striked out search engines equals total number of search engines
					if(no_of_striked_out_engines==s)
					{
						//if((query_no+1)!=q) //should not be the last query
							no_of_switches++;
						unset_all_flags(s);
						flags_search_engine[engine_no] = true;
						no_of_striked_out_engines = 1;
					}					
				}
			}

			sprintf(output_string,"Case #%d: %d\n",input_case+1,no_of_switches);
			printf("**********************Case #%d: %d\n",input_case+1,no_of_switches);
			fputs(output_string,out);
		}
		else
		{
			sprintf(output_string,"Case #%d: %d\n",input_case+1,0);
			printf("**********************Case #%d: %d\n",input_case+1,no_of_switches);
			fputs(output_string,out);
		}
	}

	fclose(out);
	fclose(in);
	return 0;
}