#include "iostream"
#include "fstream"
#include <vector>
#include <string>
using namespace std;

void round(unsigned long *&arr, int count);
unsigned long process(unsigned long *arr, unsigned long R, unsigned long k, int N);

void main()
{
	ifstream fin;
	ofstream fout;
	int T;	//number of testcases

	fin.open("C-small-attempt1.in", ios_base::in);
	fout.open("C-small-attempt1.out", ios_base::out);

	fin>>T;

	for(int i=1; i<=T; i++)
	{
		unsigned long R;
		unsigned long k;
		int N;
		unsigned long *queue;
		unsigned long money = 0;

		fout<<"Case #"<<i<<": ";		
		fin>>R;
		fin>>k;
		fin>>N;
		
		queue = new unsigned long[N];

		for(int j=0; j<N; j++)
		{
			fin>>queue[j];
		}

		money = process(queue,R,k,N);
		fout<<money;

		if(i<T)
			fout<<endl;
	}

	fin.close();
	fout.close();
}

int find(unsigned long *arr, unsigned long k ,int N, unsigned long &numPeo)
{	

	unsigned long sum = 0;

	if(N==1)
		numPeo = arr[0];
	for(int i=0; i<N; i++)
	{				
		sum += arr[i];
		if(sum > k)
		{
			numPeo = sum - arr[i];
			return i-1;
		}
		
	}
	numPeo = sum;
	return -1;
}

void round(unsigned long *&arr, int num, int index)
{
	int count = index;
	unsigned long *tmp;
	int k=0;
	tmp = new unsigned long[num];

	for(int i=count; i<num; i++)
	{
		tmp[k++] = arr[i];
	}
	for(int i=0; i<count; i++)
	{
		tmp[k++] = arr[i];
	}
	arr = tmp;
}
unsigned long process(unsigned long *arr, unsigned long R, unsigned long k, int N)
{
	unsigned long money=0;
	for(int i=0; i<R; i++)
	{
		unsigned long sum=0;
		int index=0;

		index = find(arr, k, N, sum);
		money += sum;
		round(arr, N, index+1);
	}
	return money;
	
}
