#include <set>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>

using namespace std;

typedef pair<char,char> pcc;

#define IN fin
#define OUT fout

int main()
{
	ifstream fin("B.in");
	ofstream fout("B.out");

	int T;
	IN>>T;
	for(int i=1;i<=T;i++)
	{
		int C;
		char combo[26][26];  //combo[i][j] != 0 implies that [i,j] combine to form combo[i][j]
		int D;
		set<char> oppo[26];  //if oppo[i].contains(j), then [i,j] are opposed
		int N;
		
		string ret = "";
		string input;
		
		for(int j=0;j<26;j++)   for(int k=0;k<26;k++)   combo[j][k] = 0;
		
		IN>>C;
		for(int j=0;j<C;j++)
		{
			string tStr;
			IN>>tStr;
			
			char c1 = tStr[0] - 'A', c2 = tStr[1] - 'A';
			
			combo[c1][c2] = combo[c2][c1] = tStr[2];
		}
		IN>>D;
		for(int j=0;j<D;j++)
		{
            string tStr;
			IN>>tStr;
			
			char c1 = tStr[0] - 'A', c2 = tStr[1] - 'A';
			
			oppo[c1].insert(c2);
			oppo[c2].insert(c1);
		}
		
		IN>>N;
		IN>>input;
		
		for(int j=0;j<N;j++)
		{
			char toAppend = input[j];
			
			if(ret.size() > 0)
			{
				//check for combos
				char c = ret[ret.size() - 1];
				if(combo[toAppend - 'A'][c - 'A'] != 0)
				{
					ret[ret.size() - 1] = combo[toAppend - 'A'][c - 'A'];
					continue;
				}
				else
				{
					//check for opposing pair
                    for(int k=0;k<ret.size();k++)
					{
						if(oppo[toAppend-'A'].find(ret[k] - 'A') != oppo[toAppend-'A'].end() )
						{
							ret = "";
							continue;
						}
					}
					if(ret.size() > 0)
					    ret += toAppend;
				}
			}
			else    ret += toAppend;
		}
		string sep = "";
		OUT<<"Case #"<<i<<": [";
		for(int j=0;j<ret.size();j++)
		{
			OUT<<sep<<ret[j];
			sep = ", ";
		}
		OUT<<"]\n";
	}
	
	return 0;
}
