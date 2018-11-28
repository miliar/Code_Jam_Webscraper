#include<cstdio>
#include<cstdlib>
#include<cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>

using namespace std;

int main()
{
	char filename[500] = "K:\\Settings And Documents\\Document\\Visual Studio 2008\\Projects\\Round1A\\Debug\\A";
	char outfile[500];

	//scanf("%s", filename);
	strcpy(outfile, filename);
	strcat(outfile, ".out");
	FILE *ofp=fopen(outfile, "w+");

	int n;
	scanf("%d", &n);
	for(int i=0; i < n; i++)
	{
		set<char> charset;
		char buff[100];
		scanf("%s", buff);
		int size = strlen(buff);
		for(int j=0;j < size; j++)
		{
			charset.insert(buff[j]);
		}
		int base = charset.size();
		if(base == 1)
		{
			base = 2;
		}
		map<char, int> mapping;
		int value = 1;
		for(int j=0;j<size;j++)
		{
			if(mapping.find(buff[j]) == mapping.end())
			{
				mapping.insert(pair<char,int>(buff[j], value));
				if(value == 1)
				{
					value = 0;
				}
				else if(value == 0)
				{
					value = 2;
				}
				else
				{
					value++;
				}
			}
		}
		unsigned long long ans=0;
		for(int j=0;j<size;j++)
		{
			ans = ans*base + mapping[buff[j]];
			//buff[j] = mapping[buff[j]]+48;
		}
		fprintf(ofp, "Case #%d: %llu\n", i+1, ans);
	}
	return 0;
}