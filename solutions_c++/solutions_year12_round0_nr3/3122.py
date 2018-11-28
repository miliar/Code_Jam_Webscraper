#include <iostream>
#include <string>
#include <vector>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::vector;


struct tNumbers
{
	int A;
	int B;

	int result;
};

struct tPair
{
	int m,n;
};


int GetNumberOfDigits(int number)
{
	int res = 0;
	while(number > 0)
	{
		res++;
		number = number/10;
	}
	return res;
}

int RotateDigit(int number, int digits)
{
	int numberOfDigits = GetNumberOfDigits(number);

	int pivot = 1, iter = 0;
	int mod, div;

	for(;iter < (numberOfDigits -digits);iter++)
		pivot = pivot * 10;

	mod = number % pivot;
	div = number / pivot;

	for(iter = 0;iter < digits;iter++)
		mod = mod * 10;
	mod += div;

	return mod;

}

bool findFunction(vector<tPair> pairs, tPair temp)
{
	bool found = false;
	for(int iter = 0; (iter < pairs.size()) && (!found); iter++)
	{
		if(pairs[iter].m == temp.m && pairs[iter].n == temp.n)
			found = true;
	}
	return found;
}


void GetResult(tNumbers &input)
{
	int iter, iter2;
	int numberOfDigits = GetNumberOfDigits(input.A);
	int m,n;

	vector<tPair> pairs;
	tPair temp;

	if(input.A > input.B)
	{
		// Swap if A > B
		input.A = input.A + input.B;
		input.B = input.A - input.B;
		input.A = input.A - input.B;
	}

	for(iter = input.A; iter <= input.B; iter++)
	{
		for(iter2 = 1; iter2 < numberOfDigits; iter2++)
		{
			// rotate digit
			m = RotateDigit(iter, iter2);
			// check if inside limit
			if(m >= input.A && m <=input.B)
			{
				// check if NOT same
				if(m != iter)
				{
					if(m < iter)
					{
						temp.m = m;
						temp.n = iter;
					}
					else
					{
						temp.m = iter;
						temp.n = m;
					}

					// check if not already present
					bool present = findFunction(pairs, temp );

					if(!present)
					{
						// Add
						pairs.push_back(temp);
					}
					
				}
			}
		}
	}

	input.result = pairs.size();
}


int main()
{
	int T; // Total number of inputs
	vector<tNumbers> inputList;
	tNumbers current;

	int iter;

	cin>>T;

	for(iter=0;iter<T;iter++)
	{
		cin.ignore();
		cin>>current.A;
		cin>>current.B;

		current.result = 0;
		inputList.push_back(current);
	}

/*
	for(iter=0;iter<inputList.size();iter++)
	{
		cout<<inputList[iter].A<<endl;
		cout<<inputList[iter].B<<endl;

		cout<<endl<<inputList[iter].result<<endl<<endl;
	}
*/

	for(iter=0;iter<inputList.size();iter++)
	{
		GetResult(inputList[iter]);
		cout<<"Case #"<<(iter+1)<<": "<<inputList[iter].result<<endl;
	}

	return 0;
}

