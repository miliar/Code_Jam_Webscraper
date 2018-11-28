
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <map>

using namespace std;

int ascitime_2_min(char *asciitime)
{
	int minutes = 0;
	char * token;

	token = strtok (asciitime,":");
	minutes = atoi(token) * 60;
	token = strtok (NULL, ":");
	minutes += atoi(token);
	return minutes;
}

int main(int argc, char*argv[])
{
	char line[255];
	FILE *fp;
	int no_cases, ta_time, i, j, na, nb, trainsata, trainsatb, found;
	int arr_min, dep_min;
	multimap <int, int> a2b;
	multimap <int, int> b2a;
	multimap <int, int> readyata;
	multimap <int, int> readyatb;
	multimap <int, int>::iterator itdep;
	multimap <int, int>::iterator itready;
	char * token, *arr, *dep;

	fp = fopen(argv[1], "rb");
	if (!fp)
		return -1;

	fgets(line, 255, fp);
	no_cases = atoi(line);

	for(i=0;i<no_cases;i++)
	{
		a2b.clear();
		b2a.clear();
		readyata.clear();
		readyatb.clear();
		na = nb = ta_time = trainsata = trainsatb = 0;
		
		fgets(line, 255, fp);
		ta_time = atoi(line);

		// Read the number of trains from A and B respectively
		fgets(line, 255, fp);

		token = strtok (line," \t\n");
		na = atoi(token);
		token = strtok (NULL, " \t\n");
		nb = atoi(token);

		for(j=0;j<na;j++)
		{
			fgets(line, 255, fp);

			dep = strtok (line," \t\n");
			arr = strtok (NULL, " \t\n");
			
			dep_min = ascitime_2_min(dep);
			arr_min = ascitime_2_min(arr);
			a2b.insert(pair<int, int>(dep_min, arr_min));
			readyatb.insert(pair<int, int>(arr_min+ta_time,0));
		}
		for(j=0;j<nb;j++)
		{
			fgets(line, 255, fp);

			dep = strtok (line," \t\n");
			arr = strtok (NULL, " \t\n");
			
			dep_min = ascitime_2_min(dep);
			arr_min = ascitime_2_min(arr);
			b2a.insert(pair<int, int>(dep_min, arr_min));
			readyata.insert(pair<int, int>(arr_min+ta_time,0));
		}
		// Now check which trains are needed from A to B
		for(itdep = a2b.begin(); itdep != a2b.end(); itdep++)
		{
			found = 0;
			for(itready = readyata.begin(); itready != readyata.end() 
						&& (*itdep).first >= (*itready).first; itready++)
			{
				if((*itready).second == 0)
				{
					(*itready).second = 1;
					found = 1;
					break;
				}
			}
			if(!found)
				trainsata++;
		}
		// Now check which trains are needed from B to A
		for(itdep = b2a.begin(); itdep != b2a.end(); itdep++)
		{
			found = 0;
			for(itready = readyatb.begin(); itready != readyatb.end() 
						&& (*itdep).first >= (*itready).first; itready++)
			{
				if((*itready).second == 0)
				{
					(*itready).second = 1;
					found = 1;
					break;
				}
			}
			if(!found)
				trainsatb++;
		}
		printf("Case #%d: %d %d\n", i+1, trainsata, trainsatb);
	}

	fclose(fp);
	return 0;
}
