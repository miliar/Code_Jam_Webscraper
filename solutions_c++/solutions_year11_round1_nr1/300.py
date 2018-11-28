#include <cstdlib>
#include <cctype>
#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <assert.h>

using namespace std;

int main()
{
	ifstream cin("C:\\Users\\Bryan\\Desktop\\TestFile.in");
	ofstream cout("C:\\Users\\Bryan\\Desktop\\Output.txt");

	int T;
	cin >> T;

	for(int counter=1;counter<=T;counter++)
	{
		long long N, Pd, Pg;
		cin >> N >> Pd >> Pg;

		bool isPossible=false;

		if(N>=100)
		{
			isPossible=true;
		}
		else
		{
			for(int numG=1;numG<=N;numG++)
			{
				for(int numW=0;numW<=numG;numW++)
				{
					if((100*numW)%numG==0 && (100*numW)/numG==Pd)
					{
						isPossible=true;
						break;
					}
				}
				if(isPossible)
				{
					break;
				}
			}
		}

		if(Pg==100 && Pd<100)
		{
			isPossible=false;
		}
		if(Pg==0 && Pd>0)
		{
			isPossible=false;
		}

		cout << "Case #" << counter << ": ";

		if(isPossible)
		{
			cout << "Possible\n";
		}
		else
		{
			cout << "Broken\n";
		}
	}

	return 0;
}