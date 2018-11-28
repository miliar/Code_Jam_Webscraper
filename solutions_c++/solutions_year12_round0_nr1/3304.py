// H.Marihot
// Google Code Jam 2012
// Qualification Round
// 13th April 2012
// Problem A

#include <iostream>
#include <string.h>
using namespace std;

#define GET_MAP 1
#define TRANSLATE 0
#if TRANSLATE
// get map
int main()
{
	string map1 = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvqz";
	string map2 = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupzq";
	string input = "abcdefghijklmnopqrstuvwxyz";
	unsigned int j;
	
	for (unsigned int i = 0; i < 26; i++)
	{
		j=0;
		while (map2[j]!=input[i])
		{
			j++;
		}
		cout << map1[j];
	}
	return 0;
}
// result :
// ynficwlbkuomxsevzpdrjgthaq

#else

int main()
{
	unsigned short N;
	string input;
	string map = "yhesocvxduiglbkrztnwjpfmaq";
	cin >> N;
	getline(cin,input);
	for(unsigned short i=0; i < N; i++)
	{
		getline(cin,input);
		for(unsigned short j=0; j < input.length(); j++)
		{
			if (input[j] != ' ')
				input[j] = map[input[j]-'a'];				
		}
		cout << "Case #" << i+1 << ": " << input << endl;
		input.clear();
	}
	return 0;
}

#endif // 0
