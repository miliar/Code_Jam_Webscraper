#include <iostream>
#include <vector>
#include <map>
#include <list>

using namespace std;

char mapping[256];
bool used[256];

#define kNumberOfSample 	4

const char*  encodedText[kNumberOfSample] = 
{	
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv",
	"y qee"
};

const char* clearText[kNumberOfSample] = 
{ 	
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up",
	"a zoo"
};


void buildMappingTable()
{
	bzero(mapping, sizeof(mapping));
	bzero(used, sizeof(used));


	for(int i = 0; i < kNumberOfSample; i++)
	{
		const char *p1 = encodedText[i];
		const char *p2 = clearText[i];

	   	while(*p1)
	   	{
	   		mapping[*p1] = *p2;
	   		used[*p2] = true;
	   		p1++;
	   		p2++;
	   	}
	}
}

void checkMappingTable()
{
	int MappingIndex = 0, UnusedIndex = 0;

	for(int i = 'a'; i <= 'z'; i++)
	{
		if( !mapping[i] ) 
		{	
			if(MappingIndex)
			{
				printf("Too many possibilities\n");
				exit(1);
			}

			MappingIndex = i;
		}

		if(!used[i])
		{
			if(UnusedIndex)
			{
				printf("Too many possibilities [u]\n");
				exit(1);
			}

			UnusedIndex = i;
			
			// printf("%c is unused\n");
		}
	}

	mapping[MappingIndex] = UnusedIndex;
}

void processCase()
{
	string s;
	getline(cin, s);	// get input until eol

	for(int i = 0; i < s.size(); i++)
		s[i] = mapping[s[i]];

	cout << s;
}

int main(int argc, const char * argv[])
{

	buildMappingTable();
	checkMappingTable();

	int T;
	cin >> T;

	string s;
	getline(cin, s);	// get input until eol

	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
			processCase();
		printf("\n");
	}

    return 0;
}
