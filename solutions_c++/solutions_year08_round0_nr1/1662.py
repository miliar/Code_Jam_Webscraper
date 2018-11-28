/* Prints the default gateway IP address for this m/c */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main(int argc, char*argv[])
{
	char line[255];
	string temp_str;
	FILE *fp;
	int no_cases, no_engines, no_terms, i, j, k, no_switch, count;
	vector <string> ses;
	vector <string> sts;
	map <string, char> store;

	fp = fopen(argv[1], "rb");
	if (!fp)
		return -1;

	fgets(line, 255, fp);
	no_cases = atoi(line);

	for(i=0;i<no_cases;i++)
	{
		ses.clear();
		sts.clear();
		store.clear();
		// Read the number of search engines:
		fgets(line, 255, fp);
		no_engines = atoi(line);
		for(j=0;j<no_engines;j++)
		{
			fgets(line, 255, fp);
			temp_str.assign(line);
			ses.push_back(temp_str);
		}
		// Read the number of search terms:
		fgets(line, 255, fp);
		no_terms = atoi(line);
		for(j=0;j<no_terms;j++)
		{
			fgets(line, 255, fp);
			temp_str.assign(line);
			sts.push_back(temp_str);
		}
		for(j=0;j<no_engines;j++)
		{
			store[ses[j].c_str()] = 0;
		}
		count = 0;
		no_switch = 0;
		for(j=0;j<no_terms;j++)
		{
			if(store[sts[j].c_str()] == 0)
			{
				if(count == no_engines - 1)
				{
					count = 0;
					no_switch++;
					for(k=0;k<no_engines;k++)
					{
						store[ses[k].c_str()] = 0;
					}
				}
				store[sts[j].c_str()] = 1;
				count++;
			}
		}
		printf("Case #%d: %d\n",i+1,no_switch);
	}

	fclose(fp);
	return 0;
}
