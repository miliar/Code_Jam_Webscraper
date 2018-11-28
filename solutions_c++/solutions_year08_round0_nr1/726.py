#include <stdio.h>
#include <memory.h>
#include <map>
#include <string>

// #define SMALL

using namespace std;
typedef unsigned char SINT;
#define MAX_SIZE  101

#ifdef SMALL
	#define MAX_S	  11
	#define MAX_Q	  101
#else
	#define MAX_S	  101
	#define MAX_Q	  1001
#endif

int N, S, Q;
FILE *out;

void ReadFile(FILE *file, map<string, SINT> &name2id, SINT querys[])
{
	int i;
	char line[MAX_SIZE];
	SINT id = 0;

	name2id.clear();

	fscanf(file, "%d", &S);	
	fgets(line, MAX_SIZE - 1, file); // The first 10.
	for(i = 0; i < S; ++i)
	{
		fgets(line, MAX_SIZE - 1, file);

		line[strlen(line) - 1] = 0;
		name2id.insert(pair<string, SINT>(string(line), ++id));		

		// printf("%s_%d\n", line, strlen(line));
	}
	
	fscanf(file, "%d", &Q);
	fgets(line, MAX_SIZE - 1, file); // The first 10.
	for(i = 1; i <= Q; ++i)
	{
		fgets(line, MAX_SIZE - 1, file);

		line[strlen(line) - 1] = 0;
		id = name2id.find(string(line))->second;
		querys[i] = id;
		
		// printf("%d\n", querys[i]);
	}
}


int GetSwitches(SINT querys[], bool isUsed[])
{
	int holes = S;
	memset(isUsed, 0, sizeof(bool) * MAX_S);

	int switches = 0;

	int i = 0;
	for(i = 1; i <= Q; ++i)
	{
		SINT id = querys[i];
		if (!isUsed[id])
		{
			isUsed[id] = true;
			-- holes;
			if (0 == holes)
			{
				// fprintf(out, "%d, ", i);
				++ switches;				
				memset(isUsed, 0, sizeof(bool) * MAX_S);
				holes = S - 1;
				isUsed[id] = true;
			}
		}
	}

	return switches;
}


int main()
{
	char *InName = "A-large.in";
	char *OutName = "A-large.out";

	FILE *file = fopen(InName, "r");
	if (0 == file)
	{
		printf("File can't be opened!\n");
		exit(-1);
	}
	out = fopen(OutName, "w");

	fscanf(file, "%d", &N);

	map<string, SINT> name2id;
	SINT querys[MAX_Q];
	bool isUsed[MAX_Q];	
	int iCase = 1;
	for(iCase = 1; iCase <= N; ++ iCase)
	{
		ReadFile(file, name2id, querys);

		int result = GetSwitches(querys, isUsed);

		fprintf(out, "Case #%d: %d\n", iCase, result);
	}

	fclose(out);
	fclose(file);

	return 0;
}