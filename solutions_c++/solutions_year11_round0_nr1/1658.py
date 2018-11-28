#include <iostream>
#include <fstream>
#include <string>
 
#include <windows.h>
using namespace std;
//how many seconds are consumed by this task sequence
void ConsumeSeconds(int line ,ifstream &input ,ofstream &output) ;
//get the position of next button of Robot color , from curMission
inline int NextMissionPos(char color, int curMission ,int* btnPos,char* robColor,int size);

int main()
{
	long start = GetTickCount();
	ifstream input("A-large.in",ios::in);
	if(!input)
	{
		cerr<<"Cannot read target file"<<endl;
		exit(1);
	}

	ofstream output("A-large.out",ios::out);
	if(!output)
	{
		cerr<<"Cannot open output file"<<endl;
		exit(1);
	}
	int lines ;
	input>>lines;
	
	int i =0;
	for (i=0;i<lines;i++)
	{
		ConsumeSeconds(i,input,output);
	}

	input.close();
	output.close();
	long end = GetTickCount();
	cout<<"Time : "<<end - start<<" ms"<<endl;
	system("pause");
	return 0;
}

void ConsumeSeconds(int line ,ifstream &input ,ofstream &output)
{
	int btns , i ;
	input>> btns ;
	// robColor :   color  of each task
	char* robColor= new char[btns];
	//button 's position
	int *btnPos = new int[btns];
	for(i = 0;i<btns ;i++)
	{
		input>>robColor[i];
		input>>btnPos[i] ;
		//cout<<robColor[i]<<btnPos[i] <<" ";
	}

	const char ORNG ='O' ,BLUE='B' ;
	//whom are we waiting for , O ar B?
	char whosTurn = (robColor[0]);
	//our current mission,  starting from 0
	int curMission =0;
	int OCurPos = 1 ;
	int BCurPos=1 ;
	int OTargetPos =NextMissionPos(ORNG,curMission , btnPos, robColor,btns);
	int BTargetPos =NextMissionPos( BLUE ,curMission , btnPos, robColor,btns);
	int seconds =0;
	while(curMission<btns)
	{
		seconds ++;
		bool btnPressed = false; 
		//is ORANGE in the target position £¿
		if(OCurPos < OTargetPos)
			OCurPos ++;
		else if(OCurPos > OTargetPos)
			OCurPos -- ;
		else //if in target positon£¬press the button ,update mission pointer to next ,update whoseturn next 
		{
			if(whosTurn == ORNG)
			{
				curMission++ ;
				 OTargetPos= NextMissionPos( ORNG,curMission , btnPos, robColor,btns);
				 btnPressed = true ;
			}
		}
		
		if(BCurPos < BTargetPos)
			BCurPos ++;
		else if(BCurPos > BTargetPos)
			BCurPos -- ;
		else 
		{
			if(whosTurn == BLUE)
			{
				curMission++ ;
				BTargetPos= NextMissionPos( BLUE,curMission , btnPos, robColor,btns);
				btnPressed = true ;
			}
		}

		if(btnPressed)
			whosTurn = robColor[curMission] ;
	}

	//cout << seconds<<'\n' ;	
	output<<"Case #"<<line+1<<": "<<seconds<<'\n';
	delete[] robColor;
	delete[] btnPos;
}

inline int NextMissionPos(char color, int curMission ,int* btnPos,char* robColor,int size)
{
	for(int i=curMission; i<size;i++)
	{
		if(robColor[i] == color )
			return btnPos[i];
	}
}