/*
 * FairWarning.cpp
 *
 *  Created on: May 8, 2010
 *      Author: wen
 */
#include <iostream>
#include <fstream>

using namespace std;

long long int gcd(long long int x, long long int y) //greatest common divisor
{
    while(x>y?(x%=y):(y%=x));
    return x+y;
}

void quicksort(long long int a[], int front, int end)
{
	if (front >= end)return;
	long long int pivot=a[front];
	int i=front;
	int j=end;
	while (i<j)
	{
		while (i<j&&a[j]>pivot) j--;
		a[i]=a[j];
		while (i<j&&a[i]<=pivot) i++;
		a[j]=a[i];
	}
	a[i]=pivot;
	quicksort(a,front,i-1);
	quicksort(a,i+1,end);
	return;
}

int main()
{
	ifstream input("D:\\eclipseWorkspace\\FairWarning\\B-small-attempt3.in");
	ofstream output("D:\\eclipseWorkspace\\FairWarning\\B-small-attempt3.out");

	int C;//No. of test cases
	input>>C;
	for (int i=1;i<=C;i++)
	{
		int N;
		input>>N;
		long long int t[N];
		for(int j=0;j<N;j++)
		{
			long long int  temp;
			input>>temp;
			t[j]=temp;
		}
		quicksort(t,0,N-1);
		long long int result;
		if (t[0]==t[N-1])
			result=0;
		else
		{
			long long int minDiff=LLONG_MAX;
			long long int diff[N-1];
			for(int j=0;j<N-1;j++)
			{
				diff[j]=t[j+1]-t[j];
			}
			if (N==3)
			{
				if (diff[0]==0)
					minDiff=diff[1];
				else if (diff[1]==0)
					minDiff=diff[0];
				else
					minDiff=gcd(diff[0],diff[1]);
			}
			else
			{
				minDiff=diff[0];
			}
			if(t[0]%minDiff)
				result=((t[0]/minDiff)+1)*minDiff-t[0];
			else
				result=0;
			/*for(int j=0;j<N;j++)
			{
				cout<<(result+t[j])/(float)minDiff<<" ";
			}
			cout<<endl;*/

		}
		output<<"Case #"<<i<<": "<<result<<endl;
	}

	input.close();
	output.close();
}
