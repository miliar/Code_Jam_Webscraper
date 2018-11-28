#include<iostream>
#include<stdlib.h>
using namespace std;

void display(int **matrix, int row, int col)
{
	for(int i = 0; i < row; i++)
	{
		for(int j = 0; j < col; j++)
			cout << matrix[i][j] << " ";
		cout << endl;
	}
	cout << endl;
	
	return;
}

int sinkCount = 1;

int trackSink(int **matrix, int **ans, int i, int j)
{
	//cout << endl << "Tracking Sink for " << i << " " << j << endl;
	if(ans[i][j] != 0)
	{
		return ans[i][j];
	}
		
	int nextX = i - 1;
	int nextY = j;
	int min = matrix[nextX][nextY];
	if(matrix[i][j - 1] < min)
	{
		nextX = i;
		nextY = j - 1;
		min = matrix[i][j - 1];
	}
	if(matrix[i][j + 1] < min)
	{
		nextX = i;
		nextY = j + 1;
		min = matrix[i][j + 1];
	}
	if(matrix[i + 1][j] < min)
	{
		nextX = i + 1;
		nextY = j;
		min = matrix[i + 1][j];
	}
	
	if(min >= matrix[i][j])
	{
		//cout << min << " " << matrix[i][j] << " " << i << " " << j << endl;
		sinkCount++;
		ans[i][j] = sinkCount;
		return sinkCount;
	}
	
	return trackSink(matrix, ans, nextX, nextY);
}

int main()
{
	int cases;
	cin >> cases;
	
	int **matrix = (int **)malloc(110 * sizeof(int *));
	for(int i = 0; i < 110; i++)
		matrix[i] = (int *)malloc(110 * sizeof(int));
	
	int **ans = (int **)malloc(110 * sizeof(int *));
	for(int i = 0; i < 110; i++)
		ans[i] = (int *)malloc(110 * sizeof(int));
			
		
	
	for(int t = 0; t < cases; t++)
	{
		sinkCount = 0;
		int row, col;
		cin >> row >> col;
		row += 2;
		col += 2;
		
		for(int i = 1; i < row - 1; i++)
		{
			for(int j = 1; j < col - 1; j++)
			{
				cin >> matrix[i][j];
				//ans[i][j] = 0;
			}
		}
		
		for(int i = 0; i < row; i++)
			for(int j = 0; j < col; j++)
				ans[i][j] = 0;
			
		
		for(int i = 0; i < row; i++)
		{
			matrix[i][0] = INT_MAX;
			matrix[i][col - 1] = INT_MAX;
		}
		
		for(int j = 0; j < col; j++)
		{
			matrix[0][j] = INT_MAX;
			matrix[row - 1][j] = INT_MAX;
		}
		
		int sinkCount = 1;
		/*
		for(int i = 1; i < row - 1; i++)
		{
			for(int j = 1; j < col - 1; j++)
			{
				if((matrix[i][j] <= matrix[i + 1][j]) && (matrix[i][j] <= matrix[i - 1][j]) && (matrix[i][j] <= matrix[i][j + 1]) && (matrix[i][j] <= matrix[i][j - 1]))
					ans[i][j] = sinkCount++;
			}
		}
		*/
		
		cout << "Case #" << t + 1 << ":" << endl;
		
		for(int i = 1; i < row - 1; i++)
		{
			for(int j = 1; j < col - 1; j++)
			{
				ans[i][j] = trackSink(matrix, ans, i, j);
				cout << (char)(ans[i][j] + 'a' - 1);
				if(j != col - 2)
					cout << " ";
			}
			cout << endl;
		}
		//cout << "End of Case." << endl;
		/*
		for(int i = 0; i < col; i++)
			free(matrix[i]);
		free(matrix);
		
		for(int i = 0; i < col; i++)
			free(ans[i]);
		free(ans);
		*/
		//display(matrix, row, col);
		//display(ans, row, col);
	}
	
	
	return 0;
}