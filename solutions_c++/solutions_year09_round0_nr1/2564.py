#include <stdio.h>
#include <string.h>

typedef char* string;

long next(string pattern, long index)
{
	for(long j = index + 1;pattern[j];++j)
	{
		if(pattern[j] == ')')
			return j;
	}
	return index;
}

bool isfound(string pattern, long first, long last, char c)
{
	for(long i = first + 1;i < last;++i)
	{
		if(pattern[i] == c)
			return true;
	}
	return false;
}

bool iscompatible(string word, string pattern)
{
	long i = 0, j = 0, nextj;

	while(word[i] != 0)
	{
		if(pattern[j] == '(')
		{
			nextj = next(pattern, j);
			if(!isfound(pattern, j, nextj, word[i]))
				return false;
			j = nextj;
		}
		else
		{
			if(word[i] != pattern[j])
				return false;
		}
		++i, ++j;
	}
	return true;
}

int main(int argc, char* argv[])
{
	long i, j, count;
	long L, D, N;
	string* words;
	char buffer[1024];

	scanf("%ld %ld %ld", &L, &D, &N);
	words = new string[D];
	for(i = 0;i < D;++i)
	{
		words[i] = new char[L + 1];
		scanf("%s", words[i]);
	}
	for(i = 0;i < N;++i)
	{
		scanf("%s", buffer);
		for(j = 0, count = 0;j < D;++j)
		{
			if(iscompatible(words[j], buffer))
				++count;
		}
		printf("Case #%ld: %ld\n", i + 1, count);
	}
	for(i = 0;i < D;++i)
		delete [] words[i];
	delete [] words;
	return 0;
}
