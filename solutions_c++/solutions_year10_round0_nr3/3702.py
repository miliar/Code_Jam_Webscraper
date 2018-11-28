#include <iostream>

using namespace std;

void change(int** str, int count, int n);
int main()
{
	int a=0;
	int r,k,n;
	int i, j;
	int temp_cost=0;
	int *cost;
	int count=0;
	int money_count=0;

	
	FILE* file, *file2;
	file = fopen("C:\\Users\\Äí¿ì\\Desktop\\input.txt", "r");
	if(file == NULL)
	{
		printf("File open error!\n");
		return 1;
	}

	fscanf(file, "%d\n", &a);
	cost = new int[a];
	for(i=0; i<a; i++)
	{
		fscanf(file, "%d %d %d\n", &r, &k, &n);
		int* temp = new int[n];
		for(j=0; j<n; j++)
			fscanf(file, "%d", &temp[j]);
		for(j=0; j<r; j++)
		{
			int sum=k;
			while(1){
				if(sum < temp[count])
					break;
				else
				{
					sum = sum - temp[count];
					if(count == n)
						break;
					else
						count++;
					money_count++;
				}	
			}
			for(int w=0,q=0; q<money_count; q++)
			{
				temp_cost = temp_cost + temp[w];
				if(n-1 == w)
					w = 0;
				else w++;
			}

			change(&temp, count, n);
			count=0;
			money_count=0;
			
		}
		cost[i] = temp_cost;
		temp_cost = 0;
		delete []temp;
	}


	file2 = fopen("C:\\Users\\Äí¿ì\\Desktop\\result.txt", "w");
	for(i=0;i<a;i++)
	{
		fprintf(file2, "Case #%d: %d\n",i+1, cost[i]);
	}
	delete [] cost;
	return 0;
}

void change(int** str, int count, int n)
{
	int i,j;
	int *temp = new int[n*sizeof(int)];
	j=count;
	for(i=0;i<n;i++)
		temp[i] = (*str)[i];

	for(i=0;i<n-count;i++)
	{
		(*str)[i] = temp[j];
		j++;
	}

	j=0;
	for(i=n-count;i<n;i++)
	{
		(*str)[i] = temp[j];
		j++;
	}
	delete [] temp;
}
