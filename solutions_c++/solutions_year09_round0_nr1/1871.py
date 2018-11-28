#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int main(void){
	int N;
	int D;
	int L;
	cin >> L;
	cin >> D;
	cin >> N;
	
	vector<string> Dictionary(D);

	for (int i=0; i < D; i++)
	{
		string s;		
		cin >> s;
		Dictionary[i] = s;
	}

	for (int i=0; i < N; i++)
	{
		string s;
		cin >> s;
		vector<string> parts(50);
		int partsLength[50];
		int indexToParts = 0;
		string part;
		bool isGroup = false;
		for (int k=0; k < s.length(); k++)
		{
			if (!isGroup && (s[k] != '(')) {
				parts[indexToParts] = s[k];
				partsLength[indexToParts] = 1;
				indexToParts++;
				continue;
			}
			if (s[k] == '(')
			{
				isGroup = true;
				part = "";
				continue;
			}
			if (isGroup && (s[k] != ')')) 
			{
				part += s[k];
				continue;
			}
			if (s[k] == ')') 
			{
				isGroup = false;			
				parts[indexToParts] = part;
				partsLength[indexToParts] = part.length();
				indexToParts++;
			}
		}	

		if (indexToParts != L)
			cout << "Problem with part count\n";

		int total = 0;
		for (int ii=0; ii < D; ii++) {

			int matched = 0;
			for (int k=0; k < indexToParts; k++)
			{
				for (int j=0; j < partsLength[k]; j++) 
				{
					if (parts[k][j] == Dictionary[ii][k]) 
					{
						matched++;
						break;
					}
				}
			}
			if (matched == L)
				total++;
		}
		
		cout << "Case #"<< (i+1) << ": " << total << "\n";
	}
}