// Square Tiles --- Round 1C A.

#include "stdafx.h"
#include <algorithm>
#include <stdio.h>
#include <vector>
#include "assert.h"
#include <hash_map>

using namespace std;

namespace CodeJam
{

class InputReader
{
public:
	InputReader(const char* inputFile);
	~InputReader();

	// Reads a line that contains a single integer and return the value.
	int ReadIntLine();

	// Reads a new line from file into m_line.
	// Returns true for success and false if no more line.
	bool ReadLine();

	// Reads an integer from m_p.
	// Returns the value of the integer if exists or -1 if no more.
	int ReadInt();

	__int64 ReadInt64();

	// Read sequency of character into buf and make it 0-terminated
	// string length must less than len
	void ReadString(char* buf, int len);

private:
	void SkipSpace();
	FILE * m_fp;
	static const int c_maxLineLen = 100 * 1024;
	char m_line[c_maxLineLen];  // current line read.
	char* m_p;  // pointer to current character in the line.

	InputReader(const InputReader&);
	void operator=(const InputReader&);
};

InputReader::InputReader(const char* inputFile)
{
	m_fp = NULL;
	fopen_s(&m_fp, inputFile, "r");
	assert(m_fp != NULL);
}

InputReader::~InputReader()
{
	fclose(m_fp);
}

int InputReader::ReadIntLine()
{
	ReadLine();
	return ReadInt();
}

bool InputReader::ReadLine()
{
	memset(m_line, 0, c_maxLineLen);
	m_p = m_line;
	return fgets(m_line, c_maxLineLen, m_fp) != NULL;
}

int InputReader::ReadInt()
{
	SkipSpace();
	// Returns -1 to indicate no more data.
	if (*m_p == 0)
	{
		return -1;
	}
	int value = 0;
	while (*m_p >= '0' && *m_p <= '9')
	{
		value = value * 10 + (*m_p - '0');
		m_p++;
	}
	// printf("%d\n", value);
	return value;
}

__int64 InputReader::ReadInt64()
{
	SkipSpace();
	// Returns -1 to indicate no more data.
	if (*m_p == 0)
	{
		return -1;
	}
	__int64 value = 0;
	while (*m_p >= '0' && *m_p <= '9')
	{
		value = value * 10 + (*m_p - '0');
		m_p++;
	}
	return value;
}

void InputReader::ReadString(char* buf, int len)
{
	assert(len >= 1);
	*buf = 0;
	memset(buf, 0, len);
	SkipSpace();
	int offset = 0;
	while (*m_p != 0 && *m_p != '\n' && *m_p != '\r' && *m_p != ' ' && *m_p != '\t')
	{
		assert(offset < len - 1);
		buf[offset] = *m_p;
		m_p++;
		offset++;
	}
	buf[offset] = 0;
	assert(offset < len);
}

void InputReader::SkipSpace()
{
	while (*m_p == ' ' || *m_p == '\r' || *m_p == '\n' || *m_p == '\t') m_p++;
}

// A single TestCase
class TestCase
{
public:
    TestCase(InputReader& reader);
	~TestCase();
	void Solve();
	void ShowInput() const;
	void ShowOutput(int caseNum) const;
private:
	int m_R;  // rows
	int m_C;  // cols
	char m_tiles[50][50];
	bool m_possible;

	char m_numR[50];
	char m_numC[50];

	TestCase(const TestCase&);
	void operator=(const TestCase&);
};

// All test cases
class TestSet
{
public:
    TestSet(const char* inputFile);
	~TestSet();
	void SolveAll();
	void ShowInput() const;
	void ShowOutput() const;
private:
	
	// max possible number of test cases.
	static const int c_maxT = 100;
	int m_T;  // number of test cases
	TestCase* m_cases[c_maxT];

	InputReader* m_reader;

	TestSet(const TestSet&);
	void operator=(const TestSet&);
};

TestCase::TestCase(InputReader& reader)
{
	m_possible = true;
	reader.ReadLine();
	m_R = reader.ReadInt();
	m_C = reader.ReadInt();
	assert(m_R >= 1 && m_R <= 50);
	assert(m_C >= 1 && m_C <= 50);

	for (int i = 0; i < 50; i++)
	{
		m_numR[i] = 0;
		m_numC[i] = 0;
	}
	for (int i = 0; i < m_R; i++)
	{
		reader.ReadLine();
		reader.ReadString(m_tiles[i], m_C + 1);
		for (int k = 0; k < m_C; k++)
		{
			assert(m_tiles[i][k] == '.' || m_tiles[i][k] == '#');
			if (m_tiles[i][k] == '#') m_numR[i]++;
			if (m_tiles[i][k] == '#') m_numC[k]++;
		}
	}
}

TestCase::~TestCase()
{
}

void TestCase::ShowInput() const
{
	printf("%d %d\n", m_R, m_C);
	for (int i = 0; i < m_R; i++)
	{	
		for (int k = 0; k < m_C; k++)
		{
			printf("%c", m_tiles[i][k]);
		}
		printf("\n");
	}
}

void TestCase::ShowOutput(int caseNum) const
{
	printf("Case #%d:\n", caseNum);
	if (!m_possible)
	{
		printf("Impossible\n", caseNum);
	}
	else
	{
		for (int i = 0; i < m_R; i++)
		{	
			for (int k = 0; k < m_C; k++)
			{
				printf("%c", m_tiles[i][k]);
			}
			printf("\n");
		}
	}
}

void TestCase::Solve()
{
	// start from top left #
	// if any row burst of old number of #, impossible.
	for (int i = 0; i < m_R; i++)
	{	
		for (int k = 0; k < m_C; k++)
		{
			if (m_tiles[i][k] != '#') continue;
			// find one #
			if (k >= m_C - 1 || i >= m_R - 1)
			{
				m_possible = false;
				return;
			}
			if (m_tiles[i][k+1] != '#' ||
				m_tiles[i+1][k] != '#' ||
				m_tiles[i+1][k+1] != '#')
			{
				m_possible = false;
				return;
			}
			m_tiles[i][k] = '/';
			m_tiles[i][k+1] = '\\';
			m_tiles[i+1][k] = '\\';
			m_tiles[i+1][k+1] = '/';
		}
	}
	return;
}

TestSet::TestSet(const char* inputFile)
{
	for (int i = 0; i < c_maxT; i++) m_cases[i] = NULL;
	m_reader = new InputReader(inputFile);
	m_T = m_reader->ReadIntLine();
	assert(m_T >= 1 && m_T <= c_maxT);
	for (int i = 0; i < m_T; i++)
	{
		m_cases[i] = new TestCase(*m_reader);
	}
	ShowInput();
}

TestSet::~TestSet()
{
	delete m_reader;
	for (int i = 0; i < m_T; i++)
	{
		delete m_cases[i];
	}
}

void TestSet::SolveAll()
{
	for (int i = 0; i < m_T; i++)
	{
		printf("Case %d\n", i + 1);
		m_cases[i]->ShowInput();
		m_cases[i]->Solve();
		m_cases[i]->ShowOutput(i + 1);
	}
	printf("Final output:\n");
	ShowOutput();
}

void TestSet::ShowInput() const
{
	printf("%d\n", m_T);
	for (int i = 0; i < m_T; i++)
	{
		m_cases[i]->ShowInput();
	}
}

void TestSet::ShowOutput() const
{
	for (int i = 0; i < m_T; i++)
	{
		m_cases[i]->ShowOutput(i + 1);
	}
}
}  // end namespace

using namespace CodeJam;
int main(int argc, char* argv[])
{
	const char c_sampleInput[] = "C:\\CodeJam\\SquareTiles\\A-small-attempt0.in";
		// "C:\\CodeJam\\SquareTiles\\B-small-practice.in";
	TestSet cases(c_sampleInput);
	cases.SolveAll();
	
	return 0;
}