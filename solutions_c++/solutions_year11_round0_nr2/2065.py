// googleJam_QP2.cpp : Defines the entry point for the console application.
//

#include <map>
#include <vector>
#include <fstream>

using namespace std;

#define BASENAME "B-large"

/*
God, this is a rather ugly solution, but it was the most expedient, and I'm
approaching these like I would a one-time tool rather than something intended for
reuse, so it'll do. Hopefully it won't be held against me. :)
*/

int main(int argc, char* argv[])
{
	ifstream inFile(BASENAME ".in");
	ofstream outFile(BASENAME ".out");

	int numCases;
	inFile>>numCases;

	
	for (int caseNum=1; caseNum<=numCases; ++caseNum)
	{
		map<char,vector<pair<char,char>>> combinations;
		map<char,vector<char>> oppositions;
		
		int i;

		//read combinations
		inFile>>i;
		while (i-->0)
		{
			char a,b, c;
			inFile>>a>>b>>c;
			map<char,vector<pair<char,char>>>::iterator iter;
			iter=combinations.find(a);
			if (iter==combinations.end())
			{
				combinations[a]=vector<pair<char,char>>();
				combinations[a].push_back(pair<char,char>(b,c));
			}
			else
				iter->second.push_back(pair<char,char>(b,c));			

			iter=combinations.find(b);
			if (iter==combinations.end())
			{
				combinations[b]=vector<pair<char,char>>();
				combinations[b].push_back(pair<char,char>(a,c));
			}
			else
				iter->second.push_back(pair<char,char>(a,c));	
			
		}

		//read oppositions
		inFile>>i;
		while (i-->0)
		{
			char a,b;
			inFile>>a>>b;
			map<char,vector<char>>::iterator iter;
			iter=oppositions.find(a);
			if (iter==oppositions.end())
			{
				oppositions[a]=vector<char>();
				oppositions[a].push_back(b);
			}
			else
				iter->second.push_back(b);			

			iter=oppositions.find(b);
			if (iter==oppositions.end())
			{
				oppositions[b]=vector<char>();
				oppositions[b].push_back(a);
			}
			else
				iter->second.push_back(a);			
		}

		//now we read the sequence itself
		vector<char> elements;

		inFile>>i;
		while (i-->0)
		{
			char e;
			inFile>>e;
			
			if (elements.size()!=0)
			{
				//check for a combo
				map<char,vector<pair<char,char>>>::iterator combIter;
				combIter=combinations.find(e);

				if (combIter!=combinations.end())
				{
					bool found=false;
					for (unsigned int curComb=0; curComb<combIter->second.size(); ++curComb)
					{
						if (combIter->second[curComb].first==elements.back())
						{
							elements.pop_back();
							elements.push_back(combIter->second[curComb].second);
							found=true;
							break;
						}
					}
					if (found)
						continue;
				}
		
				//no combo, check for opposition
				map<char,vector<char>>::iterator oppIter;
				oppIter=oppositions.find(e);
				if (oppIter!=oppositions.end())
				{
					bool found=false;
					for (unsigned int curOpp=0; !found && curOpp<oppIter->second.size(); ++curOpp)
					{
						for (unsigned int curElem=0; !found && curElem<elements.size(); ++curElem)
						{
							if (elements[curElem]==oppIter->second[curOpp])
							{
								found=true;
								elements.clear();
								break;
							}
						}
					}
					if (found)
					{
						continue;
					}
				}
			}
			
			//no combinations or oppositions; just add it.
			elements.push_back(e);
		}
		//output result
		outFile<<"Case #"<<caseNum<<": [";
		
		for (unsigned int i=0; i<elements.size(); ++i)
		{
			if (i!=0)
				outFile<<", ";
			outFile<<elements[i];			
		}
		outFile<<']'<<endl;
	}


	return 0;
}

