#pragma warning (disable:4786)
#include <algorithm>
#include <functional>
#include <cstdlib>

#include <cstdio>
#include <vector>

using namespace std;

typedef vector<int> VI;
int main()
{
	FILE *fp, *fw;
	if ((fp = fopen("A-small-attempt0.in", "r")) == NULL) 
		return 1;
	if ((fw = fopen("A-small.out.txt", "w")) == NULL)
		return 1;
	int max_casenum = 0;
	fscanf(fp, "%d", &max_casenum);
	for (int casenum = 0; casenum < max_casenum; casenum++)
	{
		VI v1, v2;
		int num_integer = 0;
		fscanf(fp, "%d", &num_integer);
		int vec_element =0;
		for (int i=0; i<num_integer; i++)
		{
			fscanf(fp, "%d", &vec_element);
			v1.push_back(vec_element);
		}
		int num_v1 = v1.size();
		for (int j=0; j<num_integer; j++)
		{
			fscanf(fp, "%d", &vec_element);
			v2.push_back(vec_element);
		}
		sort(v1.begin(), v1.end(), less_equal<int>());
		sort(v2.begin(), v2.end(), greater_equal<int>());
		int iResult = 0;
		for (int k=0; k<num_integer; k++)
		{
			iResult += v1[k] * v2[k];
		}
		fprintf(fw, "Case #%d: %d \n", casenum+1, iResult);
	}
	fclose(fp);
	fclose(fw);
	return 0;	
}