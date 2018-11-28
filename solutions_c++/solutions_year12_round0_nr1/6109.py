#include <iostream>
#include <string>
#include <sstream>
//#include <stdlib.h>

using namespace std;


int main()
{
	//Initialise translation array
	char arrCharTranslate [128];
	for (int nInit=0; nInit<128; nInit++)
	{
		arrCharTranslate[nInit] = -1;
	}

	//Fill translation array
	//Get original language line
	string strOriginal("ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvyeqz");
	//Get translated line
	string strTranslated("our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upaozq");
	
	for(int nChar=0; nChar<strOriginal.size(); nChar++)
	{
		arrCharTranslate[int(strOriginal[nChar])] = strTranslated[nChar];
	}

	//Get number of cases
	string strCases;
	getline(cin, strCases);
	stringstream strmCases(strCases);
	int nCases;
	strmCases >> nCases;

	for (int nCase=0; nCase < nCases; nCase++)
	{
		//Get translated line
		string strTranslated;
		getline(cin, strTranslated);
		
		//Output translated version
		cout << "Case #" << (nCase + 1) << ": ";
		for (int nChar=0; nChar<strTranslated.size(); nChar++)
		{
			cout << arrCharTranslate[strTranslated[nChar]];
		}
		cout << endl;
	}

	return 0;
}
