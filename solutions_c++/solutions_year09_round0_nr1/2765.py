#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

template <typename T>
T convert(const char* str)
{
	T res;
	stringstream sstr(str);
	sstr >> res;
	return res;
}

template <typename T>
T convert(const string& str)
{
	T res;
	stringstream sstr(str);
	sstr >> res;
	return res;
}


char* readFile(const char* fileName)
{
	FILE* f = fopen(fileName, "r");
	if (!f)
	{
		printf("Could not open file '%s'\n", fileName);
		return NULL;
	}

	fseek(f, 0, SEEK_END);
	long s = ftell(f);
	fseek(f, 0, SEEK_SET);

	char* data = (char*)malloc(s+1);
	memset(data, 0, s+1);
	fread(data, 1, s, f);

	return data;
}

void splitLines(const char* data, vector<string>& lineVec)
{
	lineVec.clear();

	string line;
	while (*data != '\0')
	{
		if (*data != '\r' && *data != '\n')
			line += *data;
		else
		{
			if (!line.empty())
			{
				lineVec.push_back(line);
				line.clear();
			}
		}
		data++;
	}

	if (!line.empty())
	{
		lineVec.push_back(line);
	}
}

int main(int argc, char** argv)
{
	if (argc != 2)
		return -1;

	char* data = readFile(argv[1]);
	if (!data)
		return -1;

	vector<string> lineVec;
	splitLines(data, lineVec);

	if (lineVec.size()==0)
		return -1;

	size_t L=0, D=0, N=0;
	sscanf(lineVec[0].c_str(), "%u %u %u", &L, &D, &N);

	vector<string> wordVec(lineVec.begin()+1, lineVec.begin()+D+1);
	if (wordVec.size() != D)
		return -1;

	for (size_t i = D+1; i<=D+N+1 && i<lineVec.size(); ++i)
	{
		string pat = lineVec[i];

		size_t numPatMatched = 0;

		for (vector<string>::iterator it=wordVec.begin(); it!=wordVec.end(); ++it)
		{
			bool either = false;
			bool cmatched= false;
			bool patMatched = true;
			
			const char* word = it->c_str();

			for (const char *c=pat.c_str(); *c != '\0'; ++c)
			{
				if (*c == '(')
				{
					either = true;
					cmatched = false;
				}
				else if (*c == ')')
				{
					either = false;
					if (!cmatched)
					{
						patMatched = false;
						break;
					}
					++word;
				}
				else
				{
					if (!either)
					{
						if (*c != *word)
						{
							patMatched = false;
							break;
						}
						++word;
					} else {
						if (*c == *word)
						{
							cmatched = true;
						}
					}
				}
			}

			if (patMatched)
				++numPatMatched;
		}

		
		printf("Case #%u: %u\n", i-D, numPatMatched);
	}


	free(data);
	return 0;
}

