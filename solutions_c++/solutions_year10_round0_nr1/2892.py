#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;

#ifndef EXIT_SUCCESS
#define EXIT_SUCCESS 0
#endif
#ifndef EXIT_FAILURE
#define EXIT_FAILURE 1
#endif

typedef unsigned int uint;
typedef unsigned long ulong;
typedef uint T_TYPE;
typedef uint N_TYPE;
typedef ulong K_TYPE;

static const char defaultInput[] = "Example.in";
static const char defaultOutput[] = "Default.out";

static const string separator = " ", trueString = "ON", falseString = "OFF";

template<class T>
T StringTo(const string input)
{
	istringstream buffer(input);
	T out;
	buffer >> out;
	return out;
}

string GetStateString(const bool& state)
{
	if(state)
	{
		return trueString;
	}
	else
	{
		return falseString;
	}
}

bool ParseToNK(const string input, N_TYPE& n, K_TYPE& k)
{
	try
	{
		size_t sepPos = input.find(separator);
		string nStr = input.substr(0,sepPos), kStr = input.substr(sepPos + 1);
		n = StringTo<N_TYPE>(nStr);
		k = StringTo<K_TYPE>(kStr);
	}
	catch(...)
	{
		return false;
	}
	return true;
}

bool TestSnappers(N_TYPE n, K_TYPE k)
{
	//The solution is pretty simple: the light is on if (K + 1) % 2^N == 0
	K_TYPE nExp = 1 << K_TYPE(n);
	return ((k + 1) % nExp == 0);
}

int main(int argc, char* argv[])
{
	ifstream file;
	ofstream output;
	bool inOpened = false, outOpened = false;
	//argv[0] is the executable path, argv[1] is the target input
	if(argc >= 2)
	{
		file.open(argv[1]);
		if(file)
		{
			inOpened = true;
		}
		if(argc >= 3)
		{
			output.open(argv[2]);
			if(output)
			{
				outOpened = true;
			}
		}
	}
	if(!inOpened)
	{
		file.open(defaultInput);
		if(file)
		{
			inOpened = true;
		}
		else
		{
			return EXIT_FAILURE;
		}
	}
	if(!outOpened)
	{
		output.open(defaultOutput);
		if(output)
		{
			inOpened = true;
		}
		else
		{
			return EXIT_FAILURE;
		}
	}

	string tStr, line;
	T_TYPE T;
	N_TYPE N;
	K_TYPE K;
	bool result;
	
	getline(file,tStr);
	T = StringTo<T_TYPE>(tStr);
	//output << T;
	for(T_TYPE i = 0;i < T;i++)
	{
		getline(file,line);
		if(!ParseToNK(line, N, K))
		{
			return EXIT_FAILURE;
		}
		result = TestSnappers(N, K);
		output << "Case #" << (i + 1) << ": " << GetStateString(result);
		if(i < T - 1)
		{
			//isn't the last one
			output << "\n";
		}
		//Case #1: OFF
	}

	file.close();
	output.close();

	return EXIT_SUCCESS;
}