#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

int strcmp2(const void* a, const void* b)
{
	return strcmp(*((char**)a), *((char**)b));
}

int combFind(const void* a, const void* b)
{
	char* ca = *(char**)a;
	char* cb = *(char**)b;
	return memcmp(ca, cb, 2);
}

int oppFind(const void* a, const void* b)
{
	char ca = *(char*)a;
	char cb = *(char*)b;
	return ca - cb;
}

int main()
{
	char* buffer = new char[1000];
	std::cin.getline(buffer, 1000);
	int numTests = strtol(buffer, NULL, 10);
	for (int test = 1; test <= numTests; test++)
	{
		std::cin.getline(buffer, 1000);
		char* tmpBuf = buffer;

		int numCombined = strtol(tmpBuf, &tmpBuf, 10);
		tmpBuf++;
		char** combined = new char*[2*numCombined];
		for (int i = 0; i < numCombined; i++)
		{
			char* b = new char[4];
			memcpy(b, tmpBuf, 3);
			b[3] = '\0';
			combined[2*i] = b;
			char* b2 = new char[4];
			b2[0] = b[1];
			b2[1] = b[0];
			b2[2] = b[2];
			b2[3] = b[3];
			combined[2*i+1] = b2;
			tmpBuf += 3;
		}
		qsort(combined, 2*numCombined, sizeof(char*), strcmp2);

		if (numCombined > 0) tmpBuf++;
		int numOpposed = strtol(tmpBuf, &tmpBuf, 10);
		tmpBuf++;
		char** opposed = new char*[2*numOpposed];
		for (int i = 0; i < numOpposed; i++)
		{
			char* b = new char[3];
			memcpy(b, tmpBuf, 2);
			b[2] = '\0';
			opposed[2*i] = b;
			char* b2 = new char[3];
			b2[0] = b[1];
			b2[1] = b[0];
			b2[2] = b[2];
			opposed[2*i+1] = b2;
			tmpBuf += 2;
		}
		qsort(opposed, 2*numOpposed, sizeof(char*), strcmp2);

		if (numOpposed > 0) tmpBuf++;
		int numThings = strtol(tmpBuf, &tmpBuf, 10);
		tmpBuf++;
		std::string s = "";
		for (int i = 0; i < numThings; i++)
		{
			char thing = *(tmpBuf++);
			if (s == "")
			{
				s = thing;
				continue;
			}
			if (numCombined > 0)
			{
				char* t = new char[2];
				t[0] = thing;
				t[1] = s[s.length()-1];
				char** comb = (char**)bsearch(&t, combined, 2*numCombined, sizeof(char*), combFind);
				if (comb)
				{
					s = s.substr(0, s.length()-1) + (*comb)[2];
					delete[] t;
					continue;
				}
				delete[] t;
			}

			if (numOpposed > 0)
			{
				char* t = new char[2];
				t[0] = thing;
				for (int c = 0; c < s.length(); c++)
				{
					t[1] = s[c];
					char** comb = (char**)bsearch(&t, opposed, 2*numOpposed, sizeof(char*), combFind);
					if (comb)
					{
						s = "";
						delete[] t;
						continue;
					}
				}
				if (s == "") continue;
				delete[] t;
			}

			s = s + thing;
		}

		printf("Case #%d: [", test);
		for (int i = 0; i < s.length(); i++)
		{
			if (i) printf(", ");
			printf("%c", s[i]);
		}
		printf("]\n");
	}
	delete[] buffer;
}
