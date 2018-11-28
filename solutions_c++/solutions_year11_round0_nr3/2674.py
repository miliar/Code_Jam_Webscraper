// CandySplitting.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include "assert.h"

struct TestCase
{
	int m_N;
	int m_C[1000];
	int m_maxValue;  // -1 indicates NO
};

// ugly global variables.
FILE * fp = NULL;
char line[1024];
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
	return value;
}

void ReadLine()
{
	fgets(line, 1024, fp);
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

char ReadChar()
{
	SkipSpace();
	assert(*p >= 'A' && *p <= 'Z');
	char ch = *(p++);
	return ch;
}

void ReadTestCase(TestCase& t)
{
	t.m_N = ReadIntLine();
	ReadLine();
	for (int i = 0; i < t.m_N; i++)
	{
		t.m_C[i] = ReadInt();
		assert(t.m_C[i] > 0);
	}
}

void ShowTestCase(TestCase& t)
{
	printf("%d\n", t.m_N);
	for (int i = 0; i < t.m_N; i++)
	{
		printf("%d ", t.m_C[i]);
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
class SolveTestCase
{
public:
	SolveTestCase(TestCase& t)
		: m_t(t)
	{
		BuildBitsMatrix();
		if (!IsPossible())
		{
			m_t.m_maxValue = -1;
		}
		else
		{
			m_t.m_maxValue = GetMaxValue();
		}
	}

private:
	void BuildBitsMatrix()
	{
		for (int i = 0; i < m_t.m_N; i++)
		{
			int k = m_t.m_C[i];
			for (int j = 0; j < 32; j++)
			{
				m_bits[i][j] = (k & 1);
				k >>= 1;
			}
		}
	}

	bool IsPossible()
	{
		// It will be possible IFF count of bit 1 is even number in every bit position (32 of them).
		for (int j = 0; j < 32; j++)
		{
			int count = 0;
			for (int i = 0; i < m_t.m_N; i++)
			{
				if (m_bits[i][j] == 1) count++;
			}
			if ((count & 1) != 0) return false;
		}
		return true;
	}

	int GetMaxValue()
	{
		// Only the smallest candy will be given to Sean
		int sum = 0;  // assume sum is less than 2B.
		int min = m_t.m_C[0];
		for (int i = 0; i < m_t.m_N; i++)
		{
			sum += m_t.m_C[i];
			if (min > m_t.m_C[i]) min = m_t.m_C[i];
		}
		return sum - min;
	}

	TestCase& m_t;
    // the bits matrix, memory better be dynamically allocated.
	// here we lazily use 32k on the stack.
	char m_bits[1000][32];
};

int main(int argc, char* argv[])
{
	ReadInput(argv[1]);
	// ReadInput("test_input.txt");
	// ShowInput();
	
	for (int i = 0; i < numCases; i++)
	{
		TestCase& t = cases[i];
		SolveTestCase solve(t);
		if (t.m_maxValue < 0) printf("Case #%d: NO\n", i + 1);
		else printf("Case #%d: %d\n", i + 1, t.m_maxValue);
	}
	
	return 0;
}