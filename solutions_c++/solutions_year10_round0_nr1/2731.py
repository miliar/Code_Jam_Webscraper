#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;




int solve(int N, int k)
{
	
	_int64 pows = pow(2,N);
	
	int nRes = k % pows;

	if (nRes==pows-1)
	{
		return 1;
	}

	return -1;
}

int main(int argc, char * argv)
{
	FILE * fp = fopen("test.txt","rt");
	FILE * fout = fopen("out.txt","wt");
	long testcase;
	fscanf(fp,"%d\n",&testcase);
	
	vector <int> result;
	
	for (int i=0; i<testcase; i++)
	{
		int n,k;
		fscanf(fp,"%d %d \n",&n,&k);
		int sov = solve(n,k);
		result.push_back(sov);
	}
	

	
	for (i=0; i<result.size(); i++)
	{
		if (result[i]<0)
		{
			fprintf(fout,"Case #%d: OFF\n",i+1);
		}
		else
		{
			fprintf(fout,"Case #%d: ON\n",i+1);
		}
		
	}
	
	fclose(fout);
}