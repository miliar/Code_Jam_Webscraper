#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;




int solve(int R, int k, vector <int> man)
{
	int i,j;
	int ret = 0;
	int manSize = man.size();
	int manTurn = 0;

//	for (j=0; j<manSize; j++)
//	{
//		printf("Man : %d\n",man[j]);	
//	}


	for(i=0; i<R; i++)  /*****R round*****/
	{
		int sum = 0;
		
		int step = 0;
		for (j=0; j<manSize; j++)
		{	
			int id = (j+manTurn)%manSize;	
			if (sum + man[id] <= k)
			{
				sum += man[id];
				step++;
			}
			else
			{
				break;
			}
		}
		
		manTurn += step;
		ret += sum;
	}

	return ret;
}

int main(int argc, char * argv)
{
	FILE * fp = fopen("test.txt","rt");
	FILE * fout = fopen("out.txt","wt");
	int testcase;
	fscanf(fp,"%d\n",&testcase);

	vector <int> result;

	for (int i=0; i<testcase; i++)
	{
		int R,k,size;
		fscanf(fp,"%d %d %d\n",&R,&k,&size);
		vector <int> man;
		int num;
		for (int j=0; j<size-1; j++)
		{
			fscanf(fp,"%d ",&num);
			man.push_back(num);
		}
		fscanf(fp,"%d\n",&num);

		man.push_back(num);
		
		int sov = solve(R,k,man);
		result.push_back(sov);
	}


	for (i=0; i<result.size(); i++)
	{
		printf("Case #x: %d\n",result[i]);
	}

	for (i=0; i<result.size(); i++)
	{
		fprintf(fout,"Case #%d: %d\n",i+1,result[i]);
	}

	fclose(fout);
}