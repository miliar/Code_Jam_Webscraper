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
		int n,m;
		inf >> n >> m;
		string words[11000];		
		for (int i = 0; i < n; i++)
			inf >> words[i];
		outf << "Case #" << test+1 << ": ";		
		for (int im = 0; im < m; im++)
		{
			string alph;
			inf >> alph;
			int best = 0;
			int besti = 0;
			for (int cw = 0; cw < n; cw++)
			{
				bool delme[11000];
				memset(delme, false,sizeof(delme));
				string xword = words[cw];
				string board = xword;
				for (int i = 0; i < board.length(); i++)
					board[i] = '0';
				int price = 0;
				for (int t = 0; t < alph.length(); t++)
				{
					char c = alph[t];
					bool usec = false;
					for (int i = 0; i < n; i++)
					{
						if (words[i].length() != board.length() )
							continue;
						if (delme[i])
							continue;
						bool bad = false;
						for (int ch = 0; ch < words[i].length(); ch++)
						//zabil plo[ie bukve
						if ((words[i][ch] == board[ch]) || (board[ch] == '0'))
							bad = bad;
							else
								bad = true;
						
						if (bad)
							continue;
						//ne protivorechit						
						//has the letter he is thinking of,
						for (int ch = 0; ch < words[i].length(); ch++)						
							if (words[i][ch] == c)
							{
								usec = true;
								break; 
							}						
					}
					if (usec)
					{
						//nazvano
					bool corr = false;
					for (int ch = 0; ch < board.length(); ch++)
						if (xword[ch] == c)
						{
							corr = true;
							board[ch] = c;
						}
					if (!corr)
						price++;
					}
					for (int i = 0; i < n; i++)
					{
						if (words[i].length() != board.length() )
							continue;
						if (delme[i])
							continue;
						for (int ch = 0; ch < words[i].length(); ch++)						
							if ((words[i][ch] == c) && (board[ch] != c))
							{
								delme[i] = true;
							}						

					}

						

				}
				if (board != xword)
					outf << "WTF";
				if (price > best)
				{
					best = price;
					besti = cw;
				}

			}

			//outf << words[besti] <<" " << best;
			outf << words[besti];
			if (im < m-1) 
				outf << " ";

		}
		outf << endl;


		
	}

	outf.close();
	return 0;
}
