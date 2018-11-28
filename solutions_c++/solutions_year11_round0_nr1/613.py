//#define SMALL
#define LARGE
#ifdef SMALL
#elif defined LARGE
#else
#endif
#include <fstream>
#include <iostream>

//需要注意的是，按键也需要耗费时间
//并且两个人不能够同时Push Button

struct RobotState
{
	int m_iPos;
	int m_iTime;
	RobotState( int iPos = 1, int iTime = 0 ) : m_iPos( iPos ), m_iTime( iTime ){};
};

int main( int argc, char* argv[] )
{
	int iCaseNum;
#ifdef SMALL
	std::ifstream inFile("A-small-attempt0.in");
#elif defined LARGE
	std::ifstream inFile("A-large.in");
#else
	std::ifstream inFile("TestData.txt");
#endif

	std::ofstream outFile("Output.txt");

	inFile >> iCaseNum;
	for ( int iCaseIndex = 0; iCaseIndex < iCaseNum; iCaseIndex++ )
	{
		RobotState robotOrange;
		RobotState robotBlue;
		int iOpNum;
		int iCurrentTime = 0;
		inFile >> iOpNum;
		for ( int iOpIndex = 0; iOpIndex < iOpNum; iOpIndex++ )
		{
			char cColor;
			int iButtonID;
			inFile >> cColor >> iButtonID;
			if ( cColor == 'B' )
			{
				int iCostTime = abs( robotBlue.m_iPos - iButtonID ) + 1;
				if ( robotBlue.m_iTime + iCostTime <= iCurrentTime )
					iCurrentTime ++;
				else
					iCurrentTime = robotBlue.m_iTime + iCostTime;
				robotBlue.m_iTime = iCurrentTime;
				robotBlue.m_iPos = iButtonID;
			}
			else if ( cColor == 'O' )
			{
				int iCostTime = abs( robotOrange.m_iPos - iButtonID ) + 1;
				if ( robotOrange.m_iTime + iCostTime <= iCurrentTime )
					iCurrentTime++;
				else
					iCurrentTime = robotOrange.m_iTime + iCostTime;
				robotOrange.m_iTime = iCurrentTime;
				robotOrange.m_iPos = iButtonID;
			}
		}
		outFile << "Case #" <<iCaseIndex+1 << ": " << iCurrentTime << std::endl;
	}

	outFile.flush();
	outFile.close();
	inFile.close();
	
	return 0;
}