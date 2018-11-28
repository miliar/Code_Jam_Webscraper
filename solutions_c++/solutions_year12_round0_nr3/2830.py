#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int getDigitNum(int number)
{
    if (number < 10)
	return 1;
    
    int num = 0;
    while (number > 0)
    {
	number /= 10;
	num++;
    }

    return num;
}

int getRotated(int number, int digits, int transform)
{
    int out = 0;
    int base = 1;

    int lastnum;
    for (int i = 0 ; i < transform ; ++i)
    {
	lastnum = number % 10;
	if (i == transform -1)
	    if (lastnum == 0)
		return -1;
	out += lastnum * base;
	base *= 10;

	number /= 10;
    }

    for (int i = 0 ; i < digits - transform ; ++i)
    {
	out *= 10;
    }

    out += number;
    
    return out;
}

bool has(const vector<int> &map, int value)
{
    for (int i = 0 ; i < map.size() ; ++i)
	if (map[i] == value)
	    return true;

    return false;
}

int main()
{
    int T;
    cin >> T;

    // run all test cases
    for (int t = 0 ; t < T ; ++t)
    {
	int A;
	int B;

	cin >> A;
	cin >> B;

	int solution = 0;
	int digits = getDigitNum(A);
	vector<int> used;

	// bruteforce main cycle
	for (int a = A ; a < B ; ++a)
	{
	    used.clear();
	    // bruteforce minority cycle
	    for (int d = 1 ; d <= digits ; ++d)
	    {
		int b = getRotated(a,digits, d);
		if (b < 0) // null at front
		    continue;
		
		if (a < b )
		    if (b <= B)
		    {
			if (has(used, b) == false)
			{
			    solution++;
			    used.push_back(b);
			}
		    }
	    }
	    
	}

	printf("Case #%d: %d\n",t+1,solution);

    }

    return 0;
}