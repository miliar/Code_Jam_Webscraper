// TaskB.cpp
// MS Visual Studio 2008 Express Edition
// Fair Warning



#include <iostream>
#include <vector>


typedef unsigned long long int big_int;

using namespace std;

void read_numbers(vector<big_int>& numbers)
{
	for (unsigned int i = 0; i < numbers.size(); ++i)
	{
		cin >> numbers[i];
		//cout << numbers[i] << ", ";
	}
	//if (numbers.size() < 3)
	//{
	//	cout << "0, ";
	//}
}

const big_int& vector_min(const vector<big_int>& numbers)
{
	int min_index = 0;
	for (int i = 1; i < numbers.size(); ++i)
	{
		if (numbers[i] < numbers[min_index])
		{
			min_index = i;
		}
	}
	return numbers[min_index];
}

big_int gcd(big_int a,big_int b)
{
    while(a!=0 && b!=0)
    {
       if(a>=b) a=a%b;
           else b=b%a;
    }
	return a+b;
}

big_int gcd(vector<big_int>& input)
{	
	if (input.size() == 1)
	{
		return input[0];
	}
	big_int cur_gcd = gcd(input[0], input[1]);

	for (unsigned int i = 2; i < input.size(); ++i)
	{
		if (cur_gcd == 0 || cur_gcd == 1)
		{
			break;
		}
		cur_gcd = gcd(cur_gcd, input[i]);		
	}
	return cur_gcd;
}

void check(const vector<big_int>& numbers, big_int T, big_int y)
{
	if (y >= T)
		cout << "not ok! " << "(y = " << y << "T = " << T << "; ";
	big_int v = numbers[0] % T;
	for (int i = 0; i < numbers.size(); ++i)
	{
		if (v != numbers[i] % T)
		{
			cout << "not ok! " << i << " ";
		}
	}
}

big_int calc_y(const vector<big_int>& numbers)
{
	int N = numbers.size();
	vector<big_int> diffs;
	diffs.reserve(N*(N-1) / 2);
	// find differences between all events
	for (int i = 1; i < N; ++i)
	{
		int j = i-1;
		for (int j = 0; j < i; ++j)
		{
			if (numbers[i] != numbers[j])
				diffs.push_back(_abs64(numbers[i] - numbers[j]));
		}
		
	}
	//calculate greatest mupltiple
	big_int T = gcd(diffs);
	if (T == 0 || T == 1)
	{
		return 0;
	}
	
	const big_int& last_event = vector_min(numbers);
	big_int y = (T - (last_event % T))%T;	
	
	check(numbers, T, y); 
	return y;
}


int main()
{
	int T = 0;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		int N = 0;
		cin >> N;
		vector<big_int> numbers;
		numbers.resize(N);
		read_numbers(numbers);

		std::cout << "Case #" << i << ": ";
		std::cout << calc_y(numbers) << "\n";
	}

	return 0;
}

