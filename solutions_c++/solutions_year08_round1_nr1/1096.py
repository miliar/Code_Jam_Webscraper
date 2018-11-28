#include<iostream>
#include<string>
#include<fstream>
using namespace std;

void sort1(int array[] , int n)
{

	for(int x=0; x<n; x++)

	{

		int index_of_min = x;

		for(int y=x; y<n; y++)

		{

			if(array[index_of_min]<array[y])

			{

				index_of_min = y;

			}

		}

		int temp = array[x];

		array[x] = array[index_of_min];

		array[index_of_min] = temp;

	}
/*



	int min;
	for (int i=0 ; i < n ;i++)
	{
		min = i;
		for (int j=i ; j < n ; j++)
		{
			if (A[min] > A[j] )
			{
				min=j;
			}
		}
	}
	int temp = A[i];
	A[i] = A[min];
	A[min] = temp;*/
}


void sort2(int array[] , int n)
{

for(int x=0; x<n; x++)

	{

		int index_of_min = x;

		for(int y=x; y<n; y++)

		{

			if(array[index_of_min]>array[y])

			{

				index_of_min = y;

			}

		}

		int temp = array[x];

		array[x] = array[index_of_min];

		array[index_of_min] = temp;

	}
/*









	int max;
	for (int i=0 ; i < n ;i++)
	{
		max = i;
		for (int j=i ; j < n ; j++)
		{
			if (A[max] < A[j] )
			{
				max=j;
			}
		}
	}
	int temp = A[i];
	A[i] = A[max];
	A[max] = temp;*/
}



int main()
{
	int n;
	int size;
	ifstream file;
	file.open("ali.in");
	ofstream out;
	out.open("output.txt");
	file >> n;
	int first[800];
	int second[800];
	int count = 1;
	for  (count = 1 ; count <= n ; count++)
	{
		file >> size;
		for (int k = 0 ; k < size ; k++)
		{
			file >> first[k];
		}
		for (k = 0 ; k < size ; k++)
		{
			file >> second[k];
		}
		sort1(first , size);
		sort2(second , size);
		for (int l= 0 ; l < size ;l++ )
			cout << first[l] << "\n";
		cout << "****";
		for (int h=0 ; h < size ; h++)
			cout << second[h] << "\n";
		int sum = 0;
		for (k=0 ; k < size ; k++)
		{
			sum += first[k]*second[k];
		}
		out << "Case #"<<count<<": "<<sum<<"\n";
	}
	


	return 0;
}

