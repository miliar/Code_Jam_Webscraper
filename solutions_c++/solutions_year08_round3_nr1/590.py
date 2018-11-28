#pragma warning (disable:4786)
#include <algorithm>
#include <functional>
#include <cstdlib>

#include <cstdio>
#include <vector>

using namespace std;

typedef vector<int> VI;
__int64 KeyBoard[1005][1005];

int main()
{
	FILE *fp, *fw;
	if ((fp = fopen("A-large.in.txt", "r")) == NULL) 
		return 1;
	if ((fw = fopen("A-large.out.txt", "w")) == NULL)
		return 1;
	
	int max_casenum = 0;
	fscanf(fp, "%d", &max_casenum);
	for (int casenum = 0; casenum < max_casenum; casenum++)
	{
		memset(KeyBoard, 0, sizeof(KeyBoard));
		int num_maxplace = 0, num_key_avaliable =0, num_alphablet = 0;
		fscanf(fp, "%d", &num_maxplace);
		fscanf(fp, "%d", &num_key_avaliable);
		fscanf(fp, "%d", &num_alphablet);
		VI alphet;
		for (int i=0; i < num_alphablet; i++)
		{
			int num_letter_frequency = 0;
			fscanf(fp, "%ld", &num_letter_frequency);
			alphet.push_back(num_letter_frequency);			
		}
		sort(alphet.begin(), alphet.end(), greater<int>());
		for (int m=0; m<num_alphablet; m++)
		{
			int row = (m+1) % num_key_avaliable;
			if (row == 0) row = num_key_avaliable;
			int column = (m+1 - row) / num_key_avaliable + 1;
			if (column < 0 ) column = 0;
			

			KeyBoard[row][column] = alphet[m];
			int tmp = alphet.size();
		}
		
		__int64 iResult = 0;
		for (int k=1; k<=num_key_avaliable; k++)
		{
			for (int j=1; j<=num_maxplace; j++)
			{
				iResult += KeyBoard[k][j] * j; 
			}
		}
		fprintf(fw, "Case #%d: %llld \n", casenum+1, iResult);
	}
	fclose(fp);
	fclose(fw);
	return 0;	
}