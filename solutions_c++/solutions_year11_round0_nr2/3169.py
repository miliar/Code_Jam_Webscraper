// CodeJam 2011 - Qualification Round - Magicka
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
   int T, C, D, N, i, j, k;
   char **comb, **oppose, *elem, ch;
   vector<char> sls;
   ifstream infile("B-small-attempt0.in");
   ofstream outfile("B-small.out");
      
   infile >> T;
   for(i=1; i<=T; i++)
   {
	sls.clear();
	infile >> C;
	comb = new char*[C];
	for(j=0; j<C; comb[j++]=new char[3]);
	for(j=0; j<C; j++)
	{
		infile >> ch;
		comb[j][0] = ch;
		infile >> ch;
		comb[j][1] = ch;
		infile >> ch;
		comb[j][2] = ch;
	}
	infile >> D;
	oppose = new char*[D];
	for(j=0; j<D; oppose[j++]=new char[2]);
	for(j=0; j<D; j++)
	{
		infile >> ch;
		oppose[j][0] = ch;
		infile >> ch;
		oppose[j][1] = ch;
	}

	infile >> N;
	for(j=0; j<N; j++)
	{
		infile >> ch;
		sls.push_back(ch);
		if(j==0) continue;
		while(sls.size() > 1)
		{
		   for(k=0; k<C; k++)
		   {
			if( (sls.back() == comb[k][0] && sls[sls.size()-2] == comb[k][1]) || (sls.back() == comb[k][1] && sls[sls.size()-2] == comb[k][0]) )
			{
				sls.pop_back(); sls.pop_back();
				sls.push_back(comb[k][2]);
				break;
			}
		   }
		   if(k == C) break;
		}
	   	for(k=0; k<D && !sls.empty(); k++)
	  	{
		   if(sls.back() == oppose[k][0])
		   {
			for(int l=0; l<sls.size()-1; l++)
			{
				if(sls[l] == oppose[k][1])
				{
					sls.clear();
					break;
				}
			}
		   }
		   if(sls.back() == oppose[k][1])
		   {
			for(int l=0; l<sls.size()-1; l++)
			{
				if(sls[l] == oppose[k][0])
				{
					sls.clear();
					break;
				}
			}
		   }
	   	}		
	}
		
	outfile << "Case #" << i << ": [";
	for(j=0; j<sls.size(); j++)
	{
		if(j!=0) outfile << " ";
		outfile << sls[j];
		if(j != sls.size()-1) outfile << ",";
	}
	outfile << "]" << endl;
	delete[] comb; delete[] oppose;
   }
   infile.close();
   outfile.close();
   return 0;
}

