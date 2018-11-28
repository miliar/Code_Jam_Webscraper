#include<iostream>

using namespace std;
int main()
{
	int testCases;
	char currentRobot;int lastO,lastB;
	int num;
	cin >> testCases;
	for(int ctr = 1 ; ctr <= testCases ; ctr++)
	{
		int motion[2][100000];
int sequence[100000][3];
int stepCount;
		cin >> stepCount ;
		lastO=0,lastB=0;
		for(int i = 1 ; i <= stepCount ; i++)
		{
			cin >> currentRobot >> num ;
			if(currentRobot=='O')
			{
				sequence[i][0]=1,sequence[i][1]=num,sequence[i][2]=-1;
				sequence[lastO][2]=num;
			}
			else
			{
				sequence[i][0]=2,sequence[i][1]=num,sequence[i][2]=-1;
				sequence[lastB][2]=num;
			}
		}
	
	int botNo,currentOIndex=0,currentBIndex=0,oLocation=1,bLocation=1,destination;
	motion[0][currentOIndex]=1,motion[1][currentBIndex]=1;
	for(int i = 0 ; i <= stepCount ; i++)
	{
		botNo=sequence[i][0];
		destination=sequence[i][1];		
		if(botNo==1)
		{
			oLocation=motion[0][currentOIndex];
			if(oLocation<destination)
			{
				while(oLocation<destination)
				{
					oLocation++;
					currentOIndex++;
					motion[0][currentOIndex]=oLocation;
				}
			}
			else
			{
				while(oLocation>destination)
				{
					oLocation--;
					currentOIndex++;
					motion[0][currentOIndex]=oLocation;
				}
			}
			//motion[0][currentOIndex++]=destination;
			while(currentOIndex<currentBIndex)			
				{
					++currentOIndex;
					motion[0][currentOIndex]=destination;
				}
			currentOIndex++;
			motion[0][currentOIndex]=destination;
		}
		if(botNo==2)
		{
			bLocation=motion[1][currentBIndex];
			if(bLocation<destination)
			{
				while(bLocation<destination)
				{
					bLocation++;
					currentBIndex++;
					motion[1][currentBIndex]=bLocation;
				}
			}
			else
			{
				while(bLocation>destination)
				{
					bLocation--;
					currentBIndex++;
					motion[1][currentBIndex]=bLocation;

				}
			}
			while(currentBIndex<currentOIndex)			
				{
					++currentBIndex;
					motion[1][currentBIndex]=destination;
				}
			++currentBIndex;
			motion[1][currentBIndex]=destination;
		}
		
	}	

		if(currentOIndex>currentBIndex)cout<<"Case #"<<ctr<<": "<<currentOIndex<<"\n";
		else	cout<<"Case #"<<ctr<<": "<<currentBIndex <<"\n";
	}
	
}
