#include <fstream>
#include <iostream>

using namespace std;

#define max(x, y) x>y?x:y

int x[15];
bool flag[15];
int result;
int N;

void backTrack(int depth)
{
	if(depth >= N)
	{
		//bool allFalse = true;
		//bool allTrue = true;
		int tmp = 0;
		for(int i = 0; i < N; ++i)
		{
			tmp = tmp + (int)flag[i];
		}
		if(tmp == 0 || tmp == N)
			;
		else
		{
		
		int left = 0;
		int right = 0;
		int leftNormal = 0;
		int rightNormal = 0;
		for(int j = 0; j < N; ++j)
		{
			if(flag[j])
			{
				left = left ^ x[j];
				leftNormal = leftNormal + x[j];
			}
			else
			{
				right = right ^ x[j]; 
				rightNormal = rightNormal + x[j];
			}
		}

		if(left == right)
		{
			//if(abs(leftNormal - rightNormal) > result)
				//result = abs(leftNormal - rightNormal);
			int tmp = max(leftNormal, rightNormal);
			if (tmp > result)
				result = tmp;
		}
		}
	}
	else
	{
		for(int i = 0; i < 2; ++i)
		{
			flag[depth] = i;
			backTrack(depth+1);
		}
	}
	
}

int main()
{
	ifstream input ("C-small.in");
	if(!input.is_open())
	{	
		cout << "error to open input file" << endl;
		return -1;
	}

	ofstream output ("C-small.out");
	if(!output.is_open())
	{
		cout << "unable to create the output file" << endl;
		return -1;
	}

	int T;
	int t, i, j;

	input >> T;
	for(t = 1; t <= T; ++t)
	{
		result = -1;

		for(j = 0; j < 15; ++j)
			flag[j] = false;

		input >> N;
		
		for(i = 0; i < N; ++i)
			input >> x[i];

		backTrack(0);
		

		output << "Case #" << t << ": ";

		if(result == -1)
			output << "NO" << endl;
		else
			output << result << endl;
	}

	system("pause");
	return 0;

}