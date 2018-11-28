#include <stdio.h>
#include <memory.h>
#include <map>


// #define SMALL

using namespace std;


#define MAX_SIZE 100
#ifdef SMALL
	#define MAX_NA	  21
	#define MAX_NB	  21
	#define MAX_T 6
#else
	#define MAX_NA	  101
	#define MAX_NB	  101
	#define MAX_T 61
#endif

int NA, NB, T;
FILE *out;
int N;
int iCase = 1;

void ReadFile(FILE *file, multimap<int, int> &A2B, multimap<int, int> &B2A)
{
	A2B.clear();
	B2A.clear();

	int i;
	char buf[MAX_SIZE];
	int hour, minit;	
	int src, des;

	fscanf(file, "%d", &T);	
	fscanf(file, "%d", &NA);	
	fscanf(file, "%d", &NB);	
	
	for(i = 1; i <= NA + NB; ++i)
	{
		fscanf(file, "%s", buf);
		//printf("%s_%d\n", buf, strlen(buf));
		hour = (buf[0] - '0') * 10 + (buf[1] - '0');
		minit = (buf[3] - '0') * 10 + (buf[4] - '0');
		src = hour * 60 + minit;

		fscanf(file, "%s", buf);
		//printf("%s_%d\n", buf, strlen(buf));
		hour = (buf[0] - '0') * 10 + (buf[1] - '0');
		minit = (buf[3] - '0') * 10 + (buf[4] - '0');
		des = hour * 60 + minit;

		if (i <= NA)
		{
			A2B.insert(pair<int, int>(src, des + T)); 
		}
		else
		{
			B2A.insert(pair<int, int>(src, des + T));
		}
	}
	// printf("%d, %d\n", A2B.size(), B2A.size());
}


struct Map
{
	multimap<int, int> *pMap;
	Map *next;
};


void GetStarts(multimap<int, int> &A2B, multimap<int, int> &B2A, int &resultA, int &resultB)
{
	multimap<int, int>::iterator iter1, iter2;

	resultA = resultB = 0;
	int total = NA + NB;

	Map aMap, bMap;
	aMap.pMap = &A2B; aMap.next = &bMap;
	bMap.pMap = &B2A; bMap.next = &aMap;
	Map *cur;
	int des;

	while(total > 0)
	{
		if (A2B.size() == 0)
		{
			resultB += B2A.size();
			break;
		}
		if (B2A.size() == 0)
		{
			resultA += A2B.size();
			break;
		}

		if (A2B.begin()->first < B2A.begin()->first)
		{
			++ resultA;
			cur = &aMap;
		}
		else
		{
			++ resultB;
			cur = &bMap;
		}	
		des = 0;
		while(true)
		{
			iter1 = cur->pMap->lower_bound(des);
			if (iter1 == cur->pMap->end())
			{
				break;
			}
			des = iter1->second;
			
			cur->pMap->erase(iter1);
			-- total;

			cur = cur->next;
		}
	}
}


int main()
{
	char *InName = "B-large.in";
	char *OutName = "B-large.out";

	FILE *file = fopen(InName, "r");
	if (0 == file)
	{
		printf("File can't be opened!\n");
		exit(-1);
	}
	out = fopen(OutName, "w");

	
	fscanf(file, "%d", &N);

	multimap<int, int> A2B, B2A;


	for(iCase = 1; iCase <= N; ++ iCase)
	{
		ReadFile(file, A2B, B2A);

		int resultA = 0, resultB = 0;

		GetStarts(A2B, B2A, resultA, resultB);

		fprintf(out, "Case #%d: %d %d\n", iCase, resultA, resultB);
	}

	fclose(out);
	fclose(file);
	
	return 0;
}