// Scholar_Product.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

//----------------------------------------------------------------------------
#if 1

#if 0
#define		INPUT_FILENAME	"test.in"
#define		OUTPUT_FILENAME	"test.out"
#else
#define		INPUT_FILENAME	"A-small-attempt0.in"
#define		OUTPUT_FILENAME	"A-small-attempt0.out"
#endif

#else
#define		INPUT_FILENAME	"C_large.in"
#define		OUTPUT_FILENAME	"C_large.out"
#endif

#define		MAX_BUFLEN		1024

#define		MAX_ENTRY		800


//#define		NO_TRACE

//----------------------------------------------------------------------------
FILE	*fp_in;
FILE	*fp_out;

char	buffer[MAX_BUFLEN];

long long	entries[2][MAX_ENTRY];
long long	sum_table[MAX_ENTRY];
long long	sum;
int			nEntries;

//----------------------------------------------------------------------------
void	initialize_state(void);
void	read_input(void);
void	process(void);
void	print_output(int num);

void	removeCR(char* str);

void	sort_entries(void);
//----------------------------------------------------------------------------

int _tmain(int argc, _TCHAR* argv[])
{
	int		num_input;
	int		i;

	fp_in= fopen(INPUT_FILENAME, "r");
	if( fp_in==NULL )
	{
		printf("파일 %s를 열수 없습니다\n", INPUT_FILENAME);
		return 0;
	}

	fp_out= fopen(OUTPUT_FILENAME, "w");
	if( fp_out==NULL )
	{
		printf("파일 %s를 열수 없습니다\n", OUTPUT_FILENAME);
		return 0;
	}

	fgets( buffer, MAX_BUFLEN, fp_in );
	num_input= atoi(buffer);
#ifndef NO_TRACE
	printf("num_input=%d\n", num_input);
#endif

	for(i=0; i<num_input; ++i)
	{
		initialize_state();

		read_input();

		process();

		print_output(i+1);
	}

	fclose(fp_in);
	fclose(fp_out);

	getchar();
	return 0;
}

//----------------------------------------------------------------------------
void	removeCR(char* str)
{
	int len= strlen(str);

	if(str[len-1]=='\n') str[len-1]='\0';
}

//----------------------------------------------------------------------------
void	initialize_state(void)
{
	int i;

	for(i= 0; i<MAX_ENTRY; ++i)
	{
		entries[0][i]= 0;
		entries[1][i]= 0;

		sum_table[i]= 0;
	}

	sum=0;
	nEntries= 0;
}

//----------------------------------------------------------------------------
void	read_input(void)
{
	char*	ptr;
	int		i, j;

	fgets( buffer, MAX_BUFLEN, fp_in );
	nEntries= atoi(buffer);

	for(j=0; j<2; ++j)
	{
		fgets( buffer, MAX_BUFLEN, fp_in );
		removeCR(buffer);

#ifndef NO_TRACE
		printf("vector %d=(", j+1);
#endif
		ptr= strtok( buffer, " " );
		entries[j][0]= atol(ptr);
		
#ifndef NO_TRACE
			printf("%ld,",entries[j][0]);
#endif

		for(i= 1; i<nEntries; ++i)
		{
			ptr= strtok( NULL, " " );
			entries[j][i]= atol(ptr);

#ifndef NO_TRACE
			printf("%ld,",entries[j][i]);
#endif
		}
#ifndef NO_TRACE
		printf(")\n", j+1);
#endif
	}

}

//----------------------------------------------------------------------------
void	process(void)
{
	int i;
	int nEntryId;

	// sort
	sort_entries();

	// calc sum
#ifndef NO_TRACE
	printf("sum_table=(,");
#endif
	for(i=0; i<nEntries; ++i)
	{
		sum_table[i]= entries[0][i]*entries[1][nEntries-1-i];

#ifndef NO_TRACE
		printf("%ld,",sum_table[i]);
#endif
	}
#ifndef NO_TRACE
	printf("\n");
#endif

	for(i=0; i<nEntries/2; ++i)
	{
		sum+= sum_table[i]+sum_table[nEntries-1-i];
	}

	if( nEntries%2==1 )
	{
		sum+= sum_table[nEntries/2];
	}
}

//----------------------------------------------------------------------------
void	sort_entries()
{
	int i;
	int j;

	for(i=0; i<nEntries; ++i)
		for(j=i+1; j<nEntries; ++j)
		{
			if(entries[0][j]<entries[0][i])
			{
				long long temp= entries[0][j];

				entries[0][j]=entries[0][i];
				entries[0][i]=temp;
			}

			if(entries[1][j]<entries[1][i])
			{
				long long temp= entries[1][j];

				entries[1][j]=entries[1][i];
				entries[1][i]=temp;
			}
		}
}

//----------------------------------------------------------------------------
void	print_output(int num)
{
	printf("Case #%d: %ld\n", num, sum);
	fprintf(fp_out, "Case #%d: %ld\n", num, sum);
}


