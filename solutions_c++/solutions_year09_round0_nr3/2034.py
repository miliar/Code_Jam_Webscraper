#include <fstream>
#include <string>
#include <iostream>
#include <list>
#include <vector>
#include <map>


typedef std::list<unsigned> TLettersPositions;
typedef std::vector< TLettersPositions > TDataVector;
typedef std::map< char, TLettersPositions > TLetterMap;

unsigned getVariantsNumber( const TDataVector& data, unsigned phraseIndex, unsigned sentenceIndex )
{
	TLettersPositions::const_iterator it = data[phraseIndex].begin();
	unsigned ind = 0;
	for(; it != data[phraseIndex].end(); it++, ind++)
	{
		if( *it >= sentenceIndex )
			break;
	}
	if (it == data[phraseIndex].end() )
		return 0;
	if (phraseIndex == 18)
		return data[phraseIndex].size() - ind;
	unsigned ret(0);
	for(; it != data[phraseIndex].end(); it++)
	{
		ret += getVariantsNumber( data, phraseIndex+1, (*it) + 1 );
		ret %= 10000;
	}
	return ret;
}

const char* phrase = "welcome to code jam";
void SolveTask( const char* inputFileName, const char* outputFileName )
{
	std::ifstream inFile( inputFileName );
	std::ofstream oFile( outputFileName );

	unsigned N(0);
	inFile >> N;
	std::string bufStr;
	std::getline(inFile, bufStr);
	for( unsigned i = 0; i < N; i++ )
	{
		std::getline(inFile, bufStr);
		std::cout << bufStr << std::endl;
		TLetterMap letterMap;
		TDataVector data(19);
		bool isNull = false;
		for (unsigned j = 0; j < 19; j++)
		{
			if(letterMap.find( phrase[j] ) != letterMap.end() )
			{
				data[j] = letterMap[phrase[j]];
				continue;
			}
			TLettersPositions letPos;
			letterMap[phrase[j]] = letPos;
			for (unsigned k = 0; k < bufStr.size(); k++)
			{
				if(bufStr[k] == phrase[j])
					letterMap[phrase[j]].push_back(k);
			}
			data[j] = letterMap[phrase[j]];
			if( data[j].size() == 0 )
			{
				isNull = true;
				break;
			}
		}
		// cut upper
		if ( !isNull )
		{
			for(unsigned j = 1; j < 19; j++)
			{
				for( TLettersPositions::iterator it = data[j].begin();
					it != data[j].end();)
				{
					if( (*it) > *( data[j-1].begin() ) )
						break;
					data[j].pop_front();
					it = data[j].begin();
				}
				if (data[j].size() == 0)
				{
					isNull = true;
					break;
				}
			}
		}
		// cut buttom
		if( !isNull )
		{
			for(int j = 17; j >= 0; j--)
			{
				for( TLettersPositions::reverse_iterator it = data[j].rbegin(); it != data[j].rend(); )
				{
					if( ( *it ) < *( data[j+1].rbegin() ) )
						break;
					data[j].pop_back();
					it = data[j].rbegin();
				}
				if (data[j].size() == 0)
				{
					isNull = true;
					break;
				}
			}
		}
		unsigned ret = 0;
		if(!isNull)
			ret = getVariantsNumber(data, 0, 0);
		oFile << "Case #" << (i+1) << ": ";
		if( ret < 10 )
			oFile << "000";
		else if (ret < 100)
			oFile << "00";
		else if (ret < 1000)
			oFile << "0";
		oFile << ret << std::endl;
	}
}

void main()
{
	SolveTask( "d:/1.txt", "d:/2.txt");
}