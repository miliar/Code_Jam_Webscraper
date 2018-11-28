// 2011_1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	FILE * in	= fopen("small.in","rt");
	FILE * out	= fopen("out_small.txt","wt");

	char buffer[256];
	int n;
	fscanf(in,"%d\n",&n);
	for(int i = 0; i<n; i++)
	{
		map<pair<char,char>, char> combine;
		map<char, char> opposed;
		vector<char>    result;

		int k;
		fscanf(in,"%d ",&k);
		for(int i = 0; i<k; i++)
		{
			char a,b,c;
			fscanf(in,"%c%c%c ",&a,&b,&c);
			combine[make_pair(a,b)] = c;
			combine[make_pair(b,a)] = c;
		}

		fscanf(in,"%d ",&k);
		for(int i = 0; i<k; i++)
		{
			char a,b;
			fscanf(in,"%c%c ",&a,&b);
			opposed[a] = b;
			opposed[b] = a;
		}

		fscanf(in,"%d ",&k);
		fscanf(in,"%s\n",buffer);
		for(int i = 0; i<k; i++)
		{
			char a = buffer[i];
			if(result.size() == 0)
			{
				result.push_back(a);
				continue;
			}
			while(result.size() && combine.find(make_pair(result.back(),a)) != combine.end())
			{
				a = combine[make_pair(result.back(),a)];
				result.pop_back();
			}

			if(opposed.find(a) != opposed.end() && find(result.begin(),result.end(),opposed[a]) != result.end())
			{
				result.clear();
				continue;
			}
			result.push_back(a);
		}
		fprintf(out,"Case #%d: [",i+1);
		for(int j = 0; j<result.size(); j++)
		{
			fprintf(out,"%c",result[j]);
			if(j+1 < result.size()) fprintf(out,", ");
		}
		fprintf(out,"]\n",i);
	}
	fclose(in);
	fclose(out);
	return 0;
}

