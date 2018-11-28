#include <cstdio>
#include <iostream>
using namespace std;

#define MAX 1000000

FILE* fin;
FILE* fout;

int P,Q,p[100];
bool used[100];

int getResult(int n)
{
	int result = MAX;
	if(n == 0)
		return 0;
	for(int i = 0; i < Q; i++)
	{
		if(used[i])
			continue;
		int check = 0;
		bool found = false;
		for(int j = i-1; j >= 0; j--)
			if(used[j])
			{
				check += p[i] - p[j] - 1;
				found = true;
				break;
			}
		if(!found)
			check += p[i] - 1;
		
		found = false;
		for(int j = i+1; j < Q; j++)
			if(used[j])
			{
				check += p[j]-p[i]-1;
				found = true;
				break;
			}
		if(!found)
			check += P - p[i];
		
		used[i] = true;
		check += getResult(n-1);
		used[i] = false;
		if(check < result)
			result = check;
	}
	return result;
}

int main()
{
	fin = fopen ("c_small.in","r");
	fout = fopen ("c_small.out","w");
	
	int T;
	fscanf(fin, "%d", &T);
	for(int t = 1; t <= T; t++)
	{
		fscanf(fin, "%d %d", &P, &Q);
		for(int i = 0; i < Q; i++)
			fscanf(fin, "%d", &p[i]);
		sort(p, p+Q);
		fprintf(fout, "Case #%d: %d\n", t,getResult(Q));
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
