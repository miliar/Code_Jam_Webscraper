// Jai Mata Di
// GCJ 2011 Problem No. 1

#include<iostream>
#include<fstream>
#include<vector>
#include<queue>
#include<string>
using namespace std;
int main()
{
	try{

	// Prepare File Stream
	ifstream ip("ip.txt");
	ofstream debug("debug.txt");
	ofstream op("op.txt");
	if(!ip.is_open() || !op.is_open())
	cout<<"Cannot Open File";
	
	int noOfTestCases=0;
	ip>>noOfTestCases;

	for(int i=0; i<noOfTestCases; i++)
	{
		debug<<endl;
		int noOfPushes=0;
		ip>>noOfPushes;
		queue< vector<int> > schedule;
		queue< int > sequenceOfO;
		queue< int > sequenceOf1;
		
		//Gather Info
		for(int j=0; j<noOfPushes; j++)
		{
			vector<int> push;
			char who;
			ip>>who;
			
			int wher;
			ip>>wher;

			if(who=='O')
			{
				push.push_back(0);
				push.push_back(wher);
				sequenceOfO.push(wher);
			}
			else
			{
				push.push_back(1);
				push.push_back(wher);
				sequenceOf1.push(wher);
			}
			schedule.push(push);
		}

		//Let The Journey Begin
		int afterSeconds=0;
		bool isFinished = schedule.empty();
		
		vector<int> targetPosition;
		targetPosition.push_back(-1);
		targetPosition.push_back(-1);
		if(!sequenceOfO.empty())
		{
			targetPosition[0] = sequenceOfO.front();
			sequenceOfO.pop();
		}
		else
		{
			targetPosition[0] = -1;
		}

		if(!sequenceOf1.empty())
		{
			targetPosition[1] = sequenceOf1.front();
			sequenceOf1.pop();
		}
		else
		{
			targetPosition[1] = -1;
		}

		vector<int> currentPosition;
		currentPosition.push_back(1);
		currentPosition.push_back(1);

		int whoIsExpected    =-1;
		int wherIsItExpected =-1;
		if(!schedule.empty())
		{
			whoIsExpected = schedule.front()[0];
			wherIsItExpected = schedule.front()[1];
			schedule.pop();
		}
		
		while(isFinished != true)
		{
			//Let the journey begin

			vector<int> whatDoing;
			whatDoing.push_back(0);
			whatDoing.push_back(0);

			if(currentPosition[0] == targetPosition[0] || targetPosition[0] == -1)
			{
				if(whoIsExpected == 0)
				{
					//Double Check
					if(wherIsItExpected = currentPosition[0])
					{
						whatDoing[0] = 3;
					}
					else
					{
						debug<<" Double Check Failed for 0";
					}
				}
				else
				{
					whatDoing[0] = 0;
				}
			}
			else
			{
				if(currentPosition[0] < targetPosition[0]  || targetPosition[0] == -1)
				{
					whatDoing[0] = 2;
				}
				else
				{
					whatDoing[0] = 1;
				}
			}

			// For 1
			if(currentPosition[1] == targetPosition[1] || targetPosition[1] == -1)
			{
				if(whoIsExpected == 1)
				{
					//Double Check
					if(wherIsItExpected = currentPosition[1])
					{
						if(whatDoing[0] != 3)
						{
							whatDoing[1] = 3;
						}
						else
						{
							whatDoing[1] = 0;
						}
					}
					else
					{
						debug<<" Double Check Failed for 1";
					}
				}
				else
				{
					whatDoing[1] = 0;
				}
			}
			else
			{
				if(currentPosition[1] < targetPosition[1])
				{
					whatDoing[1] = 2;
				}
				else
				{
					whatDoing[1] = 1;
				}
			}

			afterSeconds++;
			//Processing and Status
			debug<<"At End Of "<<afterSeconds<<" Seconds:  ";
			for(int i=0; i<2; i++)
			{
				debug<<i<<"   ";
				if(whatDoing[i] == 0)
				{
					debug<<" Staying at "<<currentPosition[i]<<"   ";
				}
				else if (whatDoing[i] == 1)
				{
					currentPosition[i]--;
					debug<<"Moving down to "<<currentPosition[i]<<"   ";
				}
				else if(whatDoing[i] == 2)
				{
					currentPosition[i]++;
					debug<<"Moving up to "<<currentPosition[i]<<"   ";
				}
				else if (whatDoing[i] == 3)
				{
					debug<<"Pushing button at "<<currentPosition[i]<<"   ";

					if(i == 0)
					{
						if(!sequenceOfO.empty())
						{
							targetPosition[0] = sequenceOfO.front();
							sequenceOfO.pop();
						}
					}
					else
					{
						if(!sequenceOf1.empty())
						{
							targetPosition[1] = sequenceOf1.front();
							sequenceOf1.pop();
						}
					}
					
					if(!schedule.empty())
					{
						whoIsExpected = schedule.front()[0];
						wherIsItExpected = schedule.front()[1];
						schedule.pop();
					}
					else
					{
							isFinished = true;
					}
				}
			}
			debug<<endl;

			
		}

		debug<<" -------- END ------"<<endl<<"Time Taken = "<<afterSeconds;
		op<<"Case #"<<i+1<<": "<<afterSeconds<<endl;
	}
	
	//Closure
	ip.close();
	op.close();
	}
	catch(exception e)
	{
		cout<<"Excp";	
	}
	cout<<"End";
	return 0;
}

/*_____________________Code Dump____________________________
____________________Code Dump End____________________________*/