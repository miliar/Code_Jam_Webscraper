#include <fstream>
#include <iostream>

using namespace std;

#define max(x, y) x>y?x:y

int x[15];
bool mark[15];
int benifit;
int N;

void brouteForceSearch(int layer)
{
	if(layer >= N)
	{
		int tmp = 0;
		for(int i = 0; i < N; ++i)
		{
			tmp = tmp + (int)mark[i];
		}
		if(tmp == 0 || tmp == N)
			;
		else
		{
		
		int leftPrice = 0;
		int rightPrice = 0;
		int leftNormal = 0;
		int rightNormal = 0;
		for(int j = 0; j < N; ++j)
		{
			if(mark[j])
			{
				leftPrice = leftPrice ^ x[j];
				leftNormal = leftNormal + x[j];
			}
			else
			{
				rightPrice = rightPrice ^ x[j]; 
				rightNormal = rightNormal + x[j];
			}
		}

		if(leftPrice == rightPrice)
		{
			int tmp = max(leftNormal, rightNormal);
			if (tmp > benifit)
				benifit = tmp;
		}
		}
	}
	else
	{
		for(int i = 0; i < 2; ++i)
		{
			mark[layer] = i;
			brouteForceSearch(layer+1);
		}
	}
	
}

int main()
{
	ifstream input ("C-small.in");
	ofstream output ("C-small.out");


	int T;
	int t, i, j;

	input >> T;
	for(t = 1; t <= T; ++t)
	{
		benifit = -1;

		for(j = 0; j < 15; ++j)
			mark[j] = false;

		input >> N;
		
		for(i = 0; i < N; ++i)
			input >> x[i];

		brouteForceSearch(0);
		

		output << "Case #" << t << ": ";

		if(benifit == -1)
			output << "NO" << endl;
		else
			output << benifit << endl;
	}

	return 0;

}