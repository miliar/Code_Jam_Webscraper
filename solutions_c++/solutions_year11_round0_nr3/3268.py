#include <iostream>
#include <queue>
using namespace std;

int PatSum(int num1, int num2);
int MaxValue(int num1, int num2);
void main ()
{
	int testCases=0;
	int candy;
	int i = 1;
	freopen("C-large.in","r",stdin);
	freopen("out3_large.txt","w",stdout);

	for (cin >> testCases; i <= testCases; i++)
    {
		cin >> candy;
		int value;
		int patSum = 0;
		int sum=0;
		int min=0;

		for (int c=1; c<=candy; c++)
		{
			cin >> value;
			patSum = PatSum(patSum,value);
			sum = sum+value;

			if (c==1)
				min=value;
			else if (value<min)
				min=value;
		}

		if(patSum!=0)
			cout<< "Case #" << i << ": " << "NO" << endl;
		else
			cout<< "Case #" << i << ": " << sum-min << endl;
	}
	//cout << "ans" << PatSum(a,b) <<", " << MaxValue(a,b)<<endl;
	//cout << "ans" << PatSum(PatSum(3,5),6);
}

int PatSum(int num1, int num2)
{
	int sum=0;
	for (int i = 0 ;i<32;i++)
		sum |= (((num1>>i)+(num2>>i))&1)<<i;
	return sum;
}

int MaxValue(int num1, int num2)
{
	int sum=0;
	for (int i = 0 ;i<32;i++)
		sum = num1|num2;
	return sum;
}