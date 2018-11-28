#include <cstdio>
#include <cstring>
#include <map>
using namespace std;

int main()
{
	int							iNumTestCases;
	char						cGooglerese[101];
	map<char, char>				mTranslator;
	char						alphaKeys[] = "abcdefghijklmnopqrstuvwxyz";
	char						alphaVals[] = "yhesocvxduiglbkrztnwjpfmaq";
	int							iIndex;
	int							iStrItr;
	int							iLength;

	for(iIndex = 0; iIndex < 26; iIndex++)
	{
		mTranslator[alphaKeys[iIndex]] = alphaVals[iIndex];
	}

	mTranslator[' '] = ' ';

	scanf("%d\n", &iNumTestCases);
	
	for(iIndex = 0; iIndex < iNumTestCases; iIndex++)
	{
		gets(cGooglerese);
		iLength = strlen(cGooglerese);

		printf("Case #%d: ", iIndex + 1);

		for(iStrItr = 0; iStrItr < iLength; iStrItr++)
		{
			printf("%c", mTranslator[cGooglerese[iStrItr]]);
		}

		printf("\n");
	}
}