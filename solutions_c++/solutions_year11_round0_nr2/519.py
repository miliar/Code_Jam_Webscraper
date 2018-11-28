#include <map>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

ifstream inf;
ofstream outf;
	

int main(void){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	inf.open("input.txt");
	outf.open("output.txt");
	int tests;
	inf >> tests;
	for (int test = 0; test < tests; test++)
	{		
		int c, d, n;		
		char opp[300][300], comb[300][300];

		memset (opp, 0, sizeof(opp));
		memset (comb, 0, sizeof(comb));

		inf >> c;		
		for (int i = 0; i < c; i++)
		{
			string tmp;
			inf >> tmp;
			comb[tmp[0]][tmp[1]] = tmp[2];
			comb[tmp[1]][tmp[0]] = tmp[2];
		}
		inf >> d;
		for (int i = 0; i < d; i++)
		{
			string pair;
			inf >> pair;
			opp[pair[0]][pair[1]] = opp[pair[1]][pair[0]] = 1;
		}
		inf >> n;
		string st;
		inf >> st;
		string cs = "";
		for (int i = 0; i < n; i++)
		{
			char next = st[i];
			if (cs.length() == 0)
			{
				cs = next;
				continue;
			}
			// len > 0
			if (comb[cs[cs.length() - 1]][next])
			{				
				cs[cs.length() - 1] = comb[cs[cs.length() - 1]][next];				
			}
			else
			{
				cs = cs + next;
				for (int j = 0; j < cs.length() - 1; j++)
					if (opp[cs[j]][next])
					{
						cs = "";
						break;
					}

			}
				
			
		}
		outf << "Case #" << test+1 << ": ";
		outf << "[";
		for (int i = 0; i < cs.length(); i++)
			outf << cs[i] << ((i != cs.length() - 1) ? ", ": "");
		outf << "]" << endl;
	}

	outf.close();
	return 0;
}
