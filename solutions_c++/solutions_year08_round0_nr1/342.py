#include <stdio.h>
#include <string>
#include <set>

char buff[128];

void get_buff()
{
	buff[0]='\0';
	gets(buff);
	//printf("Got : %s\n",buff);
}

int get_num()
{
	get_buff();
    return atoi(buff);
}

int main(int argc, char* argv[])
{
	int n=get_num();

	for (int i=0 ; i<n ; ++i)
	{
		int s=get_num();
		std::set<std::string> engines,engines_queried;
		for (int j=0 ; j<s ; ++j)
		{
			get_buff();
			engines.insert(buff);
		}
		
		int q=get_num();
		int switches=0;
		for (int j=0 ; j<q ; ++j)
		{
			get_buff();
			std::string query=buff;
			if (engines.count(query) && 
				engines_queried.insert(query).second &&
				engines_queried.size()==engines.size())
			{
				++switches;
				engines_queried.clear();
				engines_queried.insert(query);
			}
		}
		printf("Case #%d: %d\n",i+1,switches);
	}

	return 0;
}

