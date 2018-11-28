#include <fstream>
#include <iostream>
#include <assert.h>
#include <string.h>
#include <stdint.h>
#include <stdlib.h>


char map[26];
char mark[26];

#define MAP_SIZE (sizeof(map)/sizeof(map[0]))

void set_map(char from, char to)
{
	assert(from >= 'a' && from <= 'z');

	map[from - 'a'] = to;
	mark[from - 'a'] = 1;
}


void print_map()
{
	printf("MAP: ");
	for (size_t i = 0; i < MAP_SIZE; i++)
	{
		printf("%c:%c%s, ", 'a'+i, map[i], mark[i]? "*":"");
	}

	printf("\n");
}


void set_map_by_sample()
{
	const char * samples[] =
	{
		"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv",
	};

	const char * results[] =
	{
		"our language is impossible to understand",
		"there are twenty six factorial possibilities",
		"so it is okay if you want to just give up",
	};


	for (int i = 0; i < 3; i++)
	{
		const char * sample = samples[i];
		const char * result = results[i];

		size_t len = strlen(sample);
		assert(len == strlen(result));

		for (size_t j = 0; j < len; j++)
		{
			if (sample[j] == ' ')
			{
				continue;
			}
			set_map(sample[j], result[j]);
		}
	}

//	print_map();
}


void init_map()
{
	for (size_t i = 0; i < sizeof(map)/sizeof(map[0]); i++)
	{
		map[i] = 'a' + i;
	}

	// known
	set_map('a', 'y');
	set_map('o', 'e');
	set_map('z', 'q');
	set_map('q', 'z');
	return;
}


char do_map(char from)
{
	if (from < 'a' || from > 'z')
	{
		return from;
	}

	return map[from - 'a'];
}

char * translate(char * line)
{
	size_t len = strlen(line);

	char * ret = (char *) malloc(len + 1);
	memset(ret, 0, len+1);

	for (size_t i = 0; i < len; i++)
	{
		ret[i] = do_map(line[i]);
	}

	return ret;
}


using namespace std;

int main(int argc, char *argv[])
{
	assert(argc == 2);
	init_map();
	set_map_by_sample();

	ifstream ifs(argv[1], ifstream::in);

	int nline = 0;
	char line[128];

	ifs.getline(line, sizeof(line) / sizeof(line[0]));

	nline = strtol(line, NULL, 10);

//	std::cout << "line num " << nline << std::endl;

	for (int i = 1; i <= nline; i++)
	{
		ifs.getline(line, sizeof(line) / sizeof(line[0]));
//		std::cout << "Orig #" << i<< ":" << line << std::endl;

		char * translated = translate(line);
		std::cout << "Case #" << i<< ": " << translated << std::endl;
		free(translated);
	}

	return 0;
}
