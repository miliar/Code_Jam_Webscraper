#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <cmath>
#include <fstream>
using namespace std;

#define INFILE "A-large.in"
#define OUTFILE "A-large.out"
#define MAX_SEARCH 110

int main()
{
	ifstream in;
	ofstream out;
	int N,S,Q,sFree;
	int nS[MAX_SEARCH]={0};
	string sS[MAX_SEARCH],sC;
	int icase,i,j,k,nsw;

	in.open(INFILE);
	out.open(OUTFILE);

	if (!in || !out)
		return 0;
	
	in >> N;

	for (icase = 0; icase<N; icase++)
	{
		nsw = 0;
		
		in >> S;
		for (k=0; k<S; k++)
		{
			nS[k] = 0;
		}

		for (i=0; i<S; i++)
		{
			sS[i] = "";
			while(sS[i].length() == 0)
			{
				getline(in,sS[i]);
			}
		}
		sFree = S;

		in >> Q;
		
		for (i=0; i<Q; i++)
		{
			//in >> sC;
			sC = "";
			while(sC.length() == 0)
				getline(in, sC);
			for(j=0; j<S; j++)
			{
				if (sC.compare(sS[j]) == 0)
				{		
					if ((++nS[j]) ==1 )
						sFree--;
					break;
				}
			}

			if (sFree==0)
			{
				nsw++;
				sFree = S-1;
				for (k=0; k<S; k++)
				{
					nS[k] = 0;
				}
				nS[j]++;
			}

		}
		out << "Case #"<<icase+1<<": "<<nsw<<endl;
	}
	
	in.close();
	out.close();
	return 0;
}

