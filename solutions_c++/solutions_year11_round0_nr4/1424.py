// GoroSort.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <algorithm>
#include <stdio.h>
#include <vector>
#include "assert.h"

struct TestCase
{
	int m_N;
	int m_V[1000];
};

// ugly global variables.
FILE * fp = NULL;
const int c_LineLen = 100 * 1024;
char line[c_LineLen];
char* p;
int numCases = 0;
TestCase cases[100];

int ReadInt()
{
	while (*p == ' ') p++;
	int value = 0;
	while (*p >= '0' && *p <= '9')
	{
		value = value * 10 + (*p - '0');
		p++;
	}
	// printf("%d\n", value);
	return value;
}

void ReadLine()
{
	fgets(line, c_LineLen, fp);
	p = line;
}

int ReadIntLine()
{
	line[0] = 0;
	ReadLine();
	return ReadInt();
}

void SkipSpace()
{
	while (*p == ' ') p++;
}

void ReadTestCase(TestCase& t)
{
	t.m_N = ReadIntLine();
	ReadLine();
	for (int i = 0; i < t.m_N; i++)
	{
		t.m_V[i] = ReadInt();
		assert(t.m_V[i] > 0);  // Helps to detect parsing error.
	}
}

void ShowTestCase(TestCase& t)
{
	printf("%d\n", t.m_N);
	for (int i = 0; i < t.m_N; i++)
	{
		printf("%d ", t.m_V[i]);
	}
	printf("\n");
}

void ReadInput(const char* name)
{
	fopen_s(&fp, name, "r");
	numCases = ReadIntLine();
	for (int i = 0; i < numCases; i++)
	{
		ReadTestCase(cases[i]);
	}
}

void ShowInput()
{
	printf("%d\n", numCases);
	for (int i = 0; i < numCases; i++)
	{
		ShowTestCase(cases[i]);
	}
}

// This class takes a TestCase and solve it
class Solver
{
public:
	Solver()
	{
		ComputeExpectedValueArray();
	}
	double SolveTestCase(TestCase& t)
	{
		int s[1000];  // sorted values
		
		// detect all subsets of balls where within each subset, balls are shuffled.
		// exclude balls already in their expected final position
		for (int i = 0; i < t.m_N; i++)
		{
			s[i] = t.m_V[i];
		}
		std::sort(&s[0], &s[t.m_N]);
		
	    // position of the numbers in m_V if all numbers are sorted.
		int sorted_positions[1000];
		for (int i = 0; i < t.m_N; i++)
		{
			sorted_positions[i] = -1;
			// binary search would be better!
			for (int j = 0; j < t.m_N; j++)
			{
				if (s[j] == t.m_V[i])
				{
					sorted_positions[i] = j;
					break;
				}
			}
			assert(sorted_positions[i] >= 0);
		}

		// detect circular subsets
		std::vector<int> sizes;

		// position_processed[k] tells whether the number at t.m_V[k] has been evaluated 
		bool position_processed[1000];
        for (int i = 0; i < t.m_N; i++)
		{
			position_processed[i] = false;
		}
		for (int i = 0; i < t.m_N; i++)
		{
			if (position_processed[i]) continue;
			if (sorted_positions[i] == i)
			{
				position_processed[i] = true;
				continue;
			}
			
			// keep chasing the chain until we see a loop
			int k = i;
			int size = 0;
			while(true)
			{
                position_processed[k] = true;
				size++;
				k = sorted_positions[k];
				if (position_processed[k] == true)
				{
					// a loop detected.
					break;
				}
			}
			assert(size >= 2 && size <= t.m_N);
			sizes.push_back(size);
		}

		double evalue = 0.0;
		for (int i = 0; i < sizes.size(); i++)
		{
			evalue += m_v[sizes[i]];
		}
		return evalue;
	}

private:
	void ComputeExpectedValueArray()
	{	
		double s[1000];  // sum of first N cost
		m_v[0] = 0;
		m_v[1] = 1;
		m_v[2] = 2;
		s[0] = 0;
		s[1] = m_v[1];
		s[2] = s[1] + m_v[2];
		// Recursion walk through:
		// 1) a gang of three balls X Y Z
		//  1. chance X->X is 1/3, problem reduce to f(2)
		//  2. chance X->Y->X is 2/3*1/2=1/3, problem reduce to f(2) + 1
		//  3. chance X->Y->Z->X is 1/3, problem is f(3) + 1
		// So f(3) = 1/3(f(2)+f(2)+1+1+f(3)) => f(3) = 2/2(f(2)+1) = 3
		// 2) a gand of four bals X Y Z W
		//  1. chance X->X is 1/4, f(3) = 3
		//  2. chance X->Y->X is 1/4, f(2) + f(2) = 4
		//  3. chance X->Y->Z->X is 1/4, f(3) + 1 = 4
		//  4. chance X->Y->Z->W->X is 1/4, f(4) + 1
		// f(4) = 1/4(f(3)+f(2)+f(2)+f(3)+1+1+f(4)) ==> f(4) = 2/3(f(2)+f(3)+1) = 
		// recursively compute higher order value.
		// For example, a gang of 6 (A B C D E F) balls, after a random shuffle:
		//  1. The chance A->A is 1/6, problem reduce to f(5)
		//  2. The chance A->X->A (X!=A) is 5/6 * 1/5 = 1/6, problem reduce to f(2)+f(4)
		//  3. The chance A->X->Y->A is 5/6*4/5*1/4 = 1/6, problem reduce to f(3)+f(3)
		//  4. The chance A->X->Y->Z->A is 1/6, problem reduce to f(4)+f(2)
		//  5. The chance A->X->Y->Z->W->A is 1/6, problem reduce to f(5)+f(1)
		//  6. The chance A->X->Y->Z->W->T->A is 1/6, problem is not reduced, f(6)+f(1) 
		// Consluton: f(6) = 1/5(f(5)+f(2)+f(4)+f(3)+f(3)+f(4)+f(2)+f(5)+f(1)+f(1))
		//                 = 2/5(f(1)+f(2)+f(3)+f(4)+f(5))
		//                 = 2/5*S(5)
		// Similarily, f(7) = 2/6*S(6)
		for (int i = 3; i < 100; i++)
		{
			m_v[i] = 2.0 / (i - 1) * s[i-1];
			s[i] = s[i-1] + m_v[i];
			// printf("i:%d v:%8.6f s:%8.6f\n", i, m_v[i], s[i]);
		}
	}

	// expected value to sort N balls.
    double m_v[1000];
};


int main(int argc, char* argv[])
{
	ReadInput("C:\\CodeJam\\GoroSort\\D-small-attempt0.in");
	// ShowInput();
	Solver solver;
	for (int i = 0; i < numCases; i++)
	{
		double value = solver.SolveTestCase(cases[i]);
		printf("Case #%d: %8.6f\n", i + 1, value);
	}
	
	return 0;
}