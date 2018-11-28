/*
GCJ 2008
Problem: Save the universe!!!
Author: Reginaldo José da Silva Filho
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define TRUE 1
#define FALSE 0

typedef char string_type[120];

int get_engine_number(string_type query_name, string_type engines[], int n_engines);
void initialize_set(int set[], int size); //vector from 0 to size-1
int is_in_set(int element, int set[], int size);
int remove_from_set(int element, int set[], int size);
void print_set(int set[], int size);
int main(void)
{
	int n_cases, caseCounter;
	int n_engines, engineCounter, n_queries, queryCounter;
	int n_switches;
	int set_size;
	int possible[120];
	string_type engines[120];
	string_type query_name;
	int queries[1200]; //contains the search engine numbers
	scanf("%d", &n_cases);
	//printf("Casos: %d\n", n_cases);
	for(caseCounter = 0; caseCounter < n_cases && !feof(stdin); caseCounter++)
	{
		n_engines = n_queries = 0;
		n_switches = 0;
		set_size = 0;
		
		//monta vetor de engines
		scanf("%d", &n_engines);
		gets(query_name);
		//printf("Engines: %d\n", n_engines);
		for(engineCounter = 0; engineCounter < n_engines && !feof(stdin); engineCounter++)
		{
			gets(engines[engineCounter]);
			//printf("Leu: %s %d\n", engines[engineCounter], engineCounter);
		}
		//monta vetor de queries e o processa
		initialize_set(possible, n_engines);
		set_size = n_engines;
		//print_set(possible, set_size);

		scanf("%d", &n_queries);
		//printf("Queries: %d\n", n_queries);
		gets(query_name);
		for(queryCounter = 0; queryCounter < n_queries && !feof(stdin); queryCounter++)
		{
			gets(query_name);
			queries[queryCounter] = get_engine_number(query_name, engines, n_engines);
			//printf("Leu: %s %d\n", query_name, queries[queryCounter]);
			if (is_in_set(queries[queryCounter], possible, set_size) == TRUE)
			{
					remove_from_set(queries[queryCounter], possible, set_size);
					set_size--;
			}
			//print_set(possible, set_size);
			if(set_size == 0)
			{
				n_switches++;
				initialize_set(possible, n_engines);
				set_size = n_engines;
				
				//printf("Calling is_int_set(%d, %d)\n", queries[queryCounter],  set_size);
				if (is_in_set(queries[queryCounter], possible, set_size) == TRUE)
				{
					remove_from_set(queries[queryCounter], possible, set_size);
					set_size--;
				}
				//printf("%d switches: ", n_switches);
				//print_set(possible, set_size);
			}
		}
		printf("Case #%d: %d\n", caseCounter + 1, n_switches);
	}
	//system("pause");
	return 0;
}

int get_engine_number(string_type query_name, string_type engines[], int n_engines)
{
	int i;
	for(i = 0; i < n_engines; i++)
	{
		if(!strcmp(query_name, engines[i]))
		{
			return i;
		}
	}
	return -1;
}

void initialize_set(int set[], int size)
{
	int i;
	for(i = 0; i < size; i++)
	{
		set[i] = i;
	}
}

int is_in_set(int element, int set[], int size)
{
	int i;
	for(i = 0; i<size; i++)
	{
		if(set[i] == element)
		{
			return TRUE;
		}

	}
	return FALSE;
}
int remove_from_set(int element, int set[], int size) //does nothing if 
{
	int i;
	int j;
	int ans = 0;
	for(i = 0; i < size; i++)
	{
		if(element == set[i])
		{
			ans = 1;
			break;
		}
	}
	if(i != size-1) //then i will be the index of the element to remove
	{
		for(j = i; j < size - 1; j++)
		{
			set[j] = set[j+1];
		}
	}
	return ans;
}

void print_set(int set[], int size)
{
	int i;
	printf("%d Possible engines: ", size);
	for(i = 0; i < size; i++)
	{
		printf("%d ", set[i]);
	}
	printf("\n");
}