#include "stdlib.h"
#include <list>
#include <string>
#include <vector>
#include <algorithm>

//#define INPUT "A-test.in"
//#define OUTPUT "A-test.out"

#define INPUT "A-large.in"
#define OUTPUT "A-large.out"



struct KEY
{
	unsigned int code;
	unsigned int freq;
};


void parseLine(char* line, unsigned int L, std::vector<unsigned int> &freq)
{
int ptr = 0;
unsigned int n;
//KEY k;

	freq.clear();
	for(unsigned int i=0; i < L; i++)
	{
		//k.code = i;
		n = 0;
		while((line[ptr] >= '0') && (line[ptr] <= '9'))
		{
			n = 10*n + (line[ptr] - '0');
			ptr++;
		}
		ptr++;
		//k.freq = n;
		freq.push_back(n);
		//printf("%d ", k.freq);
	}
	//printf("\n");
}

unsigned __int64 calc(unsigned int P, unsigned int K, unsigned int L, std::vector<unsigned int> freq)
{
int i;
	std::sort(freq.begin(), freq.end());

	/*
	for(i = 0; i < L; i++)
		printf("%d ", freq[i]);
	printf("\n");
	*/


	unsigned __int64 total = 0;

	unsigned __int64 round = 1;
	unsigned __int64 letter = 1;
	unsigned int f;
	for(i = L-1; i >= 0; i--)
	{
		f = freq[i];
		total += f*round;
		letter++;
		if(letter > K)
		{
			letter = 1;
			round++;

			if((round > P) && (i == L-1))
			{
				return -1;
			}
		}
	}	

	return total;
}



void main(void)
{
FILE* fpIn;
FILE* fpOut;
char line[1000000];
unsigned int N;
unsigned __int64 P, K, L;
std::vector<unsigned int> freq;
unsigned int i;
unsigned __int64 answer;

	// Abre arquivos
	fpIn = fopen(INPUT, "rb");
	fpOut = fopen(OUTPUT, "wb");

	// Lê numero de casos
	N = atoi(fgets(line, 1024, fpIn));

	// Loop nos casos
	for(i=0; i < N; i++)
	{
		// Lê parametros para cada caso
		fgets(line, 1000000, fpIn);
		sscanf(line, "%I64d %I64d %I65d", &P, &K, &L);

		fgets(line, 1000000, fpIn);
		parseLine(line, L, freq);

		// Processa parametros
		answer = calc(P, K, L, freq);

		// Imprime saída no arquivo e no prompt
		if(answer != -1)
		{
			printf("Case #%d: %I64d\r\n", i+1, answer);
			fprintf(fpOut, "Case #%d: %I64d\n", i+1, answer);
		}
		else
		{
			printf("Case #%d: Impossible\r\n", i+1);
			fprintf(fpOut, "Case #%d: Impossible\n", i+1);
		}
	}

	// Fecha arquivos
	fcloseall();
}

