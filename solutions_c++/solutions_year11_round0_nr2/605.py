//#define SMALL
#define LARGE
#ifdef SMALL
#elif defined LARGE
#else
#endif
#include <fstream>
#include <iostream>
#include <vector>
using std::vector;

char convertPair[30][30];
bool clearMap[30][30];
bool isClearElement[30];
int showNumber[30];

int main( int argc, char* argv[] )
{
	int iCaseNum;
#ifdef SMALL
	std::ifstream inFile("B-small-attempt4.in");
#elif defined LARGE
	std::ifstream inFile("B-large.in");
#else
	std::ifstream inFile("TestData.txt");
#endif

	std::ofstream outFile( "Output.txt" );

	inFile >> iCaseNum;
	for ( int iCaseIndex = 0; iCaseIndex < iCaseNum; iCaseIndex++ )
	{
		memset( convertPair, 0, sizeof( convertPair ) );
		memset( clearMap, 0, sizeof( clearMap ) );
		memset( isClearElement, 0, sizeof( isClearElement ) );
		memset( showNumber, 0, sizeof( showNumber ) );

		vector<char> charStack;

		int iConvertPairNum;
		int iClearPairNum;
		int iPushCharNum;

		inFile >> iConvertPairNum;
		for ( int iConvertIndex = 0; iConvertIndex < iConvertPairNum; iConvertIndex++ )
		{
			char convertRule[5];
			inFile >> convertRule;
			convertPair[convertRule[0] - 'A'][convertRule[1] - 'A'] = convertRule[2];
			convertPair[convertRule[1] - 'A'][convertRule[0] - 'A'] = convertRule[2];
		}

		inFile >> iClearPairNum;
		for ( int iClearIndex = 0; iClearIndex < iClearPairNum; iClearIndex++ )
		{
			char clearRule[5];
			inFile >> clearRule;
			clearMap[clearRule[0] - 'A'][clearRule[1] - 'A'] = true;
			clearMap[clearRule[1] - 'A'][clearRule[0] - 'A'] = true;
			isClearElement[clearRule[0] - 'A'] = true;
			isClearElement[clearRule[1] - 'A'] = true;
		}

		char inStr[120];
		inFile >> iPushCharNum;
		inFile >> inStr;
		for( int iPushIndex = 0; iPushIndex < iPushCharNum; iPushIndex++ )
		{
			char currChar = inStr[iPushIndex];
			if ( charStack.size() == 0 )
			{
				charStack.push_back( currChar );
				showNumber[currChar - 'A']++;
			}
			else
			{
				char lastChar = charStack[charStack.size()-1];
				//最后两个字符匹配Convert的
				if ( convertPair[lastChar-'A'][currChar-'A'] != '\0' )
				{
					charStack.pop_back();
					showNumber[lastChar-'A']--;
					charStack.push_back( convertPair[lastChar-'A'][currChar-'A'] );
					showNumber[ convertPair[lastChar-'A'][currChar-'A'] - 'A' ]++;
				}
				//如果最后两个字不匹配
				else
				{
					//检查需要插入的字符是否属于ClearElement
					if ( isClearElement[currChar-'A'] )
					{
						int iIndex = 0;
						//如果与该ClearElement的字符出现在了栈中
						for ( iIndex = 0; iIndex < 26; iIndex++ )
						{
							if ( clearMap[currChar-'A'][iIndex] && ( showNumber[iIndex] > 0 ) )
								break;
						}
						//clear Pair没有在栈中，不需要清空，直接插入
						if ( iIndex == 26 )
						{
							charStack.push_back( currChar );
							showNumber[currChar - 'A']++;
						}
						//需要清空栈
						else
						{
							charStack.clear();
							memset( showNumber, 0, sizeof( showNumber ) );
						}
					}
					//不属于Convert也不属于Clear，直接插入并且记录
					else
					{
						charStack.push_back( currChar );
						showNumber[currChar - 'A']++;
					}
				}
			}
		}

		outFile << "Case #" <<iCaseIndex+1 << ": [";
		for ( int iIndex = 0; iIndex < charStack.size(); iIndex++ )
		{
			outFile << charStack[iIndex];
			if ( iIndex < charStack.size() - 1 )
				outFile << ", ";
		}
		outFile << "]" << std::endl;
	}

	outFile.flush();
	outFile.close();
	inFile.close();
	return 0;
}