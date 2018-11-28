// Magicka.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "assert.h"

struct Combine
{
	char m_elem_1;
	char m_elem_2;
	char m_elem_3;
};

struct Oppose
{
	char m_elem_1;
	char m_elem_2;
};

struct TestCase
{
	int m_numC;
	int m_numD;
	int m_numN;
	Combine m_C[36];
	Oppose m_D[28];
	char m_N[100];

	int m_numOutput;
	char m_output[100];
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

bool IsBaseElement(char c)
{
	return (c == 'Q' || c == 'W' || c == 'E' || c == 'R' ||
		    c == 'A' || c == 'S' || c == 'D' || c == 'F');
}

void ReadCombine(Combine& c)
{
	c.m_elem_1 = ReadChar();
	c.m_elem_2 = ReadChar();
	c.m_elem_3 = ReadChar();
	assert(IsBaseElement(c.m_elem_1));
	assert(IsBaseElement(c.m_elem_2));
	assert(!IsBaseElement(c.m_elem_3));
}

void ReadOppose(Oppose& d)
{
	d.m_elem_1 = ReadChar();
	d.m_elem_2 = ReadChar();
	assert(IsBaseElement(d.m_elem_1));
	assert(IsBaseElement(d.m_elem_2));
}

void ReadTestCase(TestCase& t)
{
	ReadLine();
	t.m_numC = ReadInt();
	for (int i = 0; i < t.m_numC; i++)
	{
		ReadCombine(t.m_C[i]);
	}
	t.m_numD = ReadInt();
	for (int i = 0; i < t.m_numD; i++)
	{
		ReadOppose(t.m_D[i]);
	}
	t.m_numN = ReadInt();
	for (int i = 0; i < t.m_numN; i++)
	{
		t.m_N[i] = ReadChar();
		assert(IsBaseElement(t.m_N[i]));
	}
}

void ShowTestCase(TestCase& t)
{
	printf("%d ", t.m_numC);
	for (int i = 0; i < t.m_numC; i++)
	{
		printf("%c%c%c ", t.m_C[i].m_elem_1, t.m_C[i].m_elem_2, t.m_C[i].m_elem_3);
	}

	printf("%d ", t.m_numD);
	for (int i = 0; i < t.m_numD; i++)
	{
		printf("%c%c ", t.m_D[i].m_elem_1, t.m_D[i].m_elem_2);
	}

	printf("%d ", t.m_numN);
	for (int i = 0; i < t.m_numN; i++)
	{
		printf("%c", t.m_N[i]);
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

void ShowInput(const char* name)
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
		t.m_numOutput = 0;
		for (int i = 0; i < t.m_numN; i++)
		{
			// append the element to the end of element list.
			t.m_output[t.m_numOutput++] = t.m_N[i];

			ApplyCombineOrOppose();
		}
	}

private:
	void ApplyCombineOrOppose()
	{
		// combine last two elements if necessary
		if (m_t.m_numOutput >= 2)
		{
			char c = GetCombineChar(m_t.m_output[m_t.m_numOutput - 2], m_t.m_output[m_t.m_numOutput - 1]);
			if (c != 0)
			{
				m_t.m_numOutput -= 2;
				m_t.m_output[m_t.m_numOutput++] = c;
				return;
			}
		}

		// check any oppose
		for (int i = 0; i < m_t.m_numOutput - 1; i++)
		{
			if (CheckOppose(m_t.m_output[i], m_t.m_output[m_t.m_numOutput - 1]))
			{
				// clear the list
				m_t.m_numOutput = 0;
			}
		}
	}

	char GetCombineChar(char elem1, char elem2)
	{
		for (int i = 0; i < m_t.m_numC; i++)
		{
			if (m_t.m_C[i].m_elem_1 == elem1 && m_t.m_C[i].m_elem_2 == elem2) return m_t.m_C[i].m_elem_3;
			if (m_t.m_C[i].m_elem_1 == elem2 && m_t.m_C[i].m_elem_2 == elem1) return m_t.m_C[i].m_elem_3;
		}
		return 0;
	}

	bool CheckOppose(char elem1, char elem2)
	{
		for (int i = 0; i < m_t.m_numD; i++)
		{
			if (m_t.m_D[i].m_elem_1 == elem1 && m_t.m_D[i].m_elem_2 == elem2) return true;
			if (m_t.m_D[i].m_elem_1 == elem2 && m_t.m_D[i].m_elem_2 == elem1) return true;
		}
		return false;
	}

	TestCase& m_t;
};

int main(int argc, char* argv[])
{
	ReadInput(argv[1]);
	
	for (int i = 0; i < numCases; i++)
	{
		TestCase& t = cases[i];
		SolveTestCase solve(t);
		printf("Case #%d: [", i + 1);
		for (int i = 0; i < t.m_numOutput; i++)
		{
			printf("%c", t.m_output[i]);
			if (i < t.m_numOutput - 1) printf(", ");
		}
		printf("]\n");
	}
	// OutputToFile("C:\\CodeJam\\Magicka\\test_output.txt");
	
	return 0;
}