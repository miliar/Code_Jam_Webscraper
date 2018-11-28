// BotTrust.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "assert.h"

struct Step
{
	char m_robot;
	int m_button;
};

struct TestCase
{
	int m_N;
	Step m_steps[100];
	int m_solution;
};


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

char ReadChar()
{
	while (*p == ' ') p++;
	assert(*p == 'B' || *p == 'O');
	char ch = *(p++);
	return ch;
}

void ReadTestCase(TestCase& t)
{
	ReadLine();
	t.m_N = ReadInt();
	for (int i = 0; i < t.m_N; i++)
	{
		t.m_steps[i].m_robot = ReadChar();
		t.m_steps[i].m_button = ReadInt();
	}
}

void ShowTestCase(TestCase& t)
{
	printf("%d ", t.m_N);
	for (int i = 0; i < t.m_N; i++)
	{
		printf("%c %d ", t.m_steps[i].m_robot, t.m_steps[i].m_button);
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
	printf("%d\n", numCases);
	for (int i = 0; i < numCases; i++)
	{
		ShowTestCase(cases[i]);
	}
}

class SolveTestCase
{
public:
	SolveTestCase(TestCase& t)
		: m_t(t),
		  m_solutions(0),
		  m_loc_o(1),
		  m_loc_b(1),
	      m_curr(0)
	{
		t.m_solution = 0;
		while (m_curr < t.m_N)
		{
			m_solutions++;
			bool buttonPressed = false;
			DoRoundAction('B', &buttonPressed);
			DoRoundAction('O', &buttonPressed);
			if (buttonPressed) m_curr++;
		}
		t.m_solution = m_solutions;
	}

	int GetMyNextStepIndex(char me)
	{
		for (int i = m_curr; i < m_t.m_N; i++)
		{
			if (m_t.m_steps[i].m_robot == me) return i;
		}
		return -1;
	}

	void DoRoundAction(char me, bool* buttonPressed)
	{
		int i = GetMyNextStepIndex(me);
		if ( i < 0) return;
		Step& step = m_t.m_steps[i];

		int loc = (me == 'B') ? m_loc_b : m_loc_o;
		if (loc < step.m_button)
		{
			// move forward toward the button
			loc++;
		}
		else if (loc == step.m_button)
		{
			if (i == m_curr)
			{
				// press the button
				*buttonPressed = true;
			}
			// otherwise wait right here
		}
		else
		{
			// move backward toward the button
			loc--;
		}
		if (me == 'B') m_loc_b = loc;
		else m_loc_o = loc;
	}

	TestCase& m_t;
	int m_solutions;
	int m_loc_o;
	int m_loc_b;
	int m_curr;
};

int main(int argc, char* argv[])
{
	ReadInput("A-large.in");
	FILE* fpout = fopen("C:\\CodeJam\\BotTrust\\BotTrust\\output.txt", "w");
	char line[1024];
	for (int i = 0; i < numCases; i++)
	{
		SolveTestCase solve(cases[i]);
		printf("Case #%d: %d\n", i + 1, cases[i].m_solution);
		sprintf_s(line, 1024, "Case #%d: %d\n", i + 1, cases[i].m_solution);
		fputs(line, fpout);
	}
	fclose(fpout);
	return 0;
}

