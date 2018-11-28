#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
#include <sstream>
#include <bitset>
using namespace std;


int main()
{
	
	
	int map[26] = {24, 7, 4, 18, 14, 2, 21, 23, 3, 20, 8, 6, 11, 1, 10, 17, 25, 19, 13, 22, 9, 15, 5, 12, 0, 16};
	char buffer[4096];
	
	FILE *fp1 = fopen ("A-small-attempt1.in", "r");	
	FILE *fp2 = fopen ("output1.txt", "w");
	
	int T, C, D, N;
	fscanf (fp1, "%d\n", &T);
	
	
	for (int i = 0; i < T; ++i)
	{
		
		fgets (buffer, 4096, fp1);
		string s(buffer);
		istringstream in(s);
		
		string g;
		vector<string> vs; 
		while(in >> g)
		{
			int sz = g.size();
			string s = g;
			for (int j = 0; j < sz; ++j)
			{
				s[j] = map[g[j] - 'a'] + 'a';
			}
			
			vs.push_back(s);
		}
		
		
		//print out
		fprintf (fp2, "Case #%d:", i + 1);
		for (int j = 0; j < vs.size(); ++j)
		{
			fprintf (fp2, " %s", vs[j].c_str());
		}
		
		fprintf (fp2, "\n");
	}
	
	return 0;
	
}