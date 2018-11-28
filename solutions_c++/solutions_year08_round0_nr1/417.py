#include <stdio.h>
#include <string>

const int MAX_S = 100;
const int MAX_Q = 1000;
const int NUM_FACTORS = 14;
const int INF = 1000000;

//-----------------------------------------

int _Factors[] = 
{
	3,
	5,
	7,
	11,
	13,
	17,
	19,
	23,
	29,
	31,
	37,
	41,
	43,
	47,
};

int CalcHash(const char* str)
{
	int code = 0;

	for (int i = 0; str[i] != 0; i++)
		code += str[i] * _Factors[i % NUM_FACTORS];

	if (code < 0)
		return -code;
	return code;
}

//-----------------------------------------

struct Node
{
	std::string Str;
	int Code;
	int Value;
};

Node _Nodes[MAX_S * 2];
int _Count;

void ClearTable()
{
	_Count = 0;
	for (int i = 0; i < MAX_S * 2; i++)
	{
		_Nodes[i].Code = -1;
		_Nodes[i].Str = "";
		_Nodes[i].Value = -1;
	}
}

int KeyToValue(const char* str)
{
	int code = CalcHash(str);

	int i = code % (MAX_S * 2);
	while (true)
	{
		if (_Nodes[i].Code == -1)
		{
			_Nodes[i].Code = code;
			_Nodes[i].Str = str;
			_Nodes[i].Value = _Count;
			_Count++;

			return _Nodes[i].Value;
		}
		else if (_Nodes[i].Code == code)
		{
			return _Nodes[i].Value;
		}
		i++;
		if (i >= MAX_S * 2)
			i = 0;
	}
}

//-----------------------------------------

char _Buf[1024];
int S;
int Q;
int NumSwithces;

int A[MAX_Q];
int B[MAX_S];

void ReadData()
{	
	ClearTable();
	
	scanf("%i\n", &S);
	for (int i = 0; i < S; i++)
	{
		gets(_Buf);
		KeyToValue(_Buf);
	}
	
	scanf("%i\n", &Q);
	for (int i = 0; i < Q; i++)
	{
		gets(_Buf);
		A[i] = KeyToValue(_Buf);
	}
}

void Work()
{
	for (int i = 0; i < S; i++)
		B[i] = 0;

	for (int i = 0; i < Q; i++)
	{
		int k = A[i];

		int minB = INF;
		for (int j = 0; j < S; j++)
		{			
			if (B[j] != -1 && B[j] < minB)
				minB = B[j];
		}

		for (int j = 0; j < S; j++)
		{
			if (j == k)
				continue;
			if (B[j] == -1)
				B[j] = minB + 1;
		}

		B[k] = -1;
	}


	if (S == 0)
		NumSwithces = 0;
	else
	{
		int minB = INF;
		for (int j = 0; j < S; j++)
		{		
			if (B[j] != -1 && B[j] < minB)
				minB = B[j];
		}
		NumSwithces = minB;
	}
}

void WriteResult(int test)
{
	printf(
		"Case #%i: %i\n",
		test,
		NumSwithces);
}

//-----------------------------------------

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int n;
	scanf("%i\n", &n);

	for (int i = 0; i < n; i++)
	{
		ReadData();
		Work();
		WriteResult(i + 1);
	}

	return 0;
}
