#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main()
{
	int nCases;
	stringstream *input;
	string buf;
	
	getline(cin, buf);
	input = new stringstream(buf);
	*input >> nCases;
	
	for (int casenum = 1; casenum <= nCases; casenum++)
	{
		int s;
		getline(cin, buf);
		delete input;
		input = new stringstream(buf);
		*input >> s;		
		
		string engines[s];
		int actualS = 0;
		for (int i = 0; i < s; i++)
		{
			string tmp;
			getline(cin, tmp);
			
			//This junk is un-necessary; I thought that there MAY be duplicate engine names. But there cannot;
			/*
			bool unique = true;
			for (int j = 0; j < actualS; j++)
			{
				if (engines[j] == tmp)
				{
					unique = false;
					break;
				}
			}
			
			if (unique)
			{*/
				engines[actualS] = tmp;
				actualS++;
			//}
		}
		
		int q;
		getline(cin, buf);
		delete input;
		input = new stringstream(buf);
		*input >> q;
				
		string queries[q];
		for (int i = 0; i < q; i++)
		{
			getline(cin, queries[i]);
		}
		
/*		cout << "--------SSSSS: " << s  << " " << actualS << endl;
		for (int i = 0; i < s; i++) cout << engines[i] << endl;
		cout << "--------QQQQQ: " << q << endl;
		for (int i = 0; i < q; i++) cout << queries[i] << endl;
		cout << "--------" << endl; */
		
		bool seen[actualS];
		for (int i = 0; i < actualS; i++) seen[i] = false;
		
		int swaps = 0;
		for (int i = 0; i < q; i++)
		{
			int index = -1;
			for (int j = 0; j < actualS; j++)
			{
				if (engines[j] == queries[i])
				{
					index = j;
					break;
				}
			}
			
			if (index >= 0)
			{
				seen[index] = true;
				
				bool allSeen = true;
				for (int j = 0; j < actualS; j++)
				{
					if (seen[j] == false)
					{
						allSeen = false;
						break;
					}
				}
				
				if (allSeen == true) //Must have just swapped
				{
					swaps++;
					for (int j = 0; j < actualS; j++) seen[j] = false;
					seen[index] = true; //See the one that we are on now
				}
			}
		}
		
		cout << "Case #" << casenum << ": " << swaps << endl;
	}
	
	return 0;
}