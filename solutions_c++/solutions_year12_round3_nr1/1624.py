//============================================================================
// Name        : RoundB-A.cpp
// Author      : Sina.1368
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

void multiple(int matrix1[100][100], int matrix2[100][100],int n);
void check_path(int matrix[100][100], int start, int end, int n);

int count;

int main() {
	int test;
	int n, m, num;
	int matrix[100][100];
	int mask[100][100];
	int matrix_count[100][100];

	cin >> test;

	for(int i = 0; i < test; i++)
	{
		cin >> n;
		for(int j = 0; j < n; j++)
			for(int k = 0; k < n; k++)
				matrix_count[j][k] = mask[j][k] = matrix[j][k] = 0;
		for(int j = 0; j < n; j++)
		{
			cin >> m;
			for(int k = 0; k < m; k++)
			{
				cin >> num;
				mask[j][num - 1] = matrix[j][num - 1] = 1;
			}
		}
		bool check = false;
		bool found = false;
		num = 1;
		while((!check) && (num < n))
		{
			multiple(matrix,mask, n);
			for(int m = 0; m < n; m++)
				for(int z = 0; z < n; z++)
					if(matrix[m][z])
					{
						count = 0;
						check_path(mask, m, z, n);
						if((matrix_count[m][z] + count) >= 2)
						{
							found = true;
							goto lable;
						}
						else
							matrix_count[m][z] += count;
					}
			lable:
			if(found)
				check = true;
			num++;
		}

		if(found)
			cout << "Case #" << i + 1 << ": Yes\n";
		else
			cout << "Case #" << i + 1 << ": No\n";
	}

	return 0;
}

void multiple(int matrix1[100][100], int matrix2[100][100],int n)
{
	int i, j, k;
	int mask[100][100];

	for(i = 0; i < n; i++)
		for(j = 0; j < n; j++)
		{
			int sum = 0;
			for(k = 0; k < n; k++)
			{
				sum += matrix1[i][k] * matrix2[k][j];
				if(sum >= 1)
					break;
			}
			if(sum > 0)
				mask[i][j] = 1;
			else
				mask[i][j] = 0;
		}

	for(i = 0; i < n; i++)
		for(j = 0; j < n; j++)
			matrix1[i][j] = mask[i][j];

}

void check_path(int matrix[100][100], int start, int end, int n)
{
	if(start == end)
		count++;
	else {
		for(int j = 0; j < n; j++)
			if(matrix[start][j])
				check_path(matrix, j, end, n);
	}
}
