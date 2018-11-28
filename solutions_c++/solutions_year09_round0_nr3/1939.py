#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

const string refer = "welcome to code jam.";
const char allowedChars[12] = {'w','e','l','c','o','m','d','j',' ','.','t','a'};
const int refer_length = 20;
const int refer_lengthminus2 = refer_length - 2;

int runCounts = 0;

int testExists1(string s, int strLength, int positionInRefer, int positionInString)
{
	runCounts++;
	int totalCount = 0;
	char c = refer[positionInRefer];
	
	if (positionInString > (strLength - (refer_length - positionInRefer - 1))) 
	{
		return 0;
	}

	if (positionInRefer < (refer_lengthminus2)) 
	{
		for (int i = positionInString; i < strLength; i++)
		{
			if (s[i] == c)
			{										
				totalCount += testExists1(s, strLength, positionInRefer+1, i+1);
			} 
		}
	} else 
	{
		for (int i = positionInString; i < strLength; i++)
		{
			if (s[i] == c)
			{						
				totalCount++;
			} 
		}
	}
	return totalCount;
}

int main(void)
{	
	int N;
	
	cin >> N;
	
	for (int i=0; i < (N + 1); i++)
	{
		int position = 0;
		int counts[refer_length];
		int lastPositions[refer_length];
		for (int k=0; k < refer_length; k++)
		{
			counts[k] = 0;
			lastPositions[k] = 0;
		}

		string s;
		getline(cin, s);

		string s1 = "";
		
		for (int k=0; k < s.length(); k++)
		{
			for (int p=0; p < 12; p++)
			{
				if (s[k] == allowedChars[p]) 
				{
					s1 += s[k];
					break;
				}
			}
		}		

		if (i == 0) continue;

		int occ = testExists1(s1, s1.length(), 0, 0);
		
		int occ1 = (occ > 9999) ? occ % 1000 : occ;	

		if (occ1 == 0)
			cout << "Case #" << i << ": 0000";
		else if (occ1 < 10)
			cout << "Case #" << i << ": 000" << occ1;
		else if (occ1 < 100)
			cout << "Case #" << i << ": 00" << occ1;
		else if (occ1 < 1000) 
			cout << "Case #" << i << ": 0" << occ1;
		else
			cout << "Case #" << i << ": " << occ1;		
		cout << "\n";
	}
}