#include <iostream>
#include <stdio.h>
#include <vector>

#define SIZE 20

using namespace std;

int counter = 0, cflag = 0;
long long sum_list[100000];

void rec_subset(long long A[SIZE], int list_size, bool check_list[SIZE], int level, int flag)
{
	if(level < 0)
	{
		long long sum = 0;
		if(counter < 100000)
		{
		for(int i = 0; i < list_size; i++)
		    if(check_list[i])
				sum += A[i];
		sum_list[counter] = sum;
		counter++;
		}
	}
	else
	{
		for(int i = flag; i < list_size - level; i++)
		{	
			check_list[i] = true;
			rec_subset(A, list_size, check_list, level - 1, i + 1);
			check_list[i] = false;
		}
	}
}

void subset(long long A[SIZE], int n, int k)
{
	bool check_list[SIZE] = {false};
	rec_subset(A, n, check_list, k - 1, 0);
}

void alt_rec_subset(long long A[SIZE], int list_size, bool check_list[SIZE], int level, int flag, int x)
{
	if(level < 0)
	{
		long long sum = 0;
		for(int i = 0; i < list_size; i++)
		    if(check_list[i])
				sum += A[i];
		if(sum == sum_list[x] && cflag < 3)
		{
			for(int i = 0; i < list_size; i++)
				if(check_list[i])
				{
					cout <<A[i];
					printf(" ");
				}
			printf("\n");
			cflag++;
		}	
	}
	else
	{
		for(int i = flag; i < list_size - level; i++)
		{	
			check_list[i] = true;
			alt_rec_subset(A, list_size, check_list, level - 1, i + 1, x);
			check_list[i] = false;
		}
	}
}

void alt_subset(long long A[SIZE], int n, int k, int x)
{
	bool check_list[SIZE] = {false};
	alt_rec_subset(A, n, check_list, k - 1, 0, x);
}

int main()
{
    freopen("input.txt", "rb", stdin);
    freopen("output.txt", "w", stdout);

	int T, N;
	long long A[SIZE];
	long long sum, temp;
	
	//input
	scanf("%d", &T);
	for(int i = 1; i <= T; i++) {
	cin>>temp;
	for(int j = 0; j < temp; j++)
		cin>>A[j];

	printf("Case #%d:\n", i);
	cflag = 0; counter = 0;
	for(int k = 1; k < SIZE; k++) 
		subset(A, SIZE, k);
	bool flag = true; int x = -1;
	for(int k = 0; k < 100000 && flag; k++)
		for(int l = k + 1; l < 100000 && flag; l++)
			if(sum_list[k] == sum_list[l])
			{
				x = k;
				flag = false;
			}
	if(x == -1)
	{
		printf("Impossible");	
	}
	else
	{
		for(int j = 1; j < SIZE; j++) 
			alt_subset(A, SIZE, j, x);
		
	}
	}
	 
    return 0;
}
