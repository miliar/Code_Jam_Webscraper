// Jai Mata Di
// GCJ 2011 ONline Round 1 Problem No. 1

#include<iostream>
#include<fstream>
#include<vector>
#include<queue>
#include<string>
#include<math.h>
#define level 1000
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

	for(int caseNo=1; caseNo<=noOfTestCases; caseNo++)
	{
		long long wonToday   = -1;
		long long totalToday = -1;
		int percentToday = -1;
		long long atleastGamesToday = -1;
		long long wonEver   = -1;
		long long totalEver = -1;
		int percentEver = -1;
		bool possible = false;
		ip>>atleastGamesToday>>percentToday>>percentEver;

		bool isTodayPossible=false;
		bool isEverPossible=false;

		for(long long i=atleastGamesToday;i>0;i--)
		{
			for(long long j=0;j<=i;j++)
				if(j*100/i==(float)percentToday)
				{ 
					if((j*100)%i == 0)
					{
						isTodayPossible=true;
						wonToday=j;
						totalToday=i;
						goto out;
					}
				}
		}
		out:
		if(isTodayPossible)
		{
			if(percentEver < 50)
			{
				for(long long i=1;i<level;i++)
				{
					for(long long j=0;j<=i;j++)
					{
						wonEver = wonToday + j;
						totalEver = totalToday + i;
						long long percent = (wonEver*100)/totalEver;
						if(percent==(long long)percentEver)
						{
							if((wonEver*100)%totalEver == 0)
							{
								isEverPossible=true;
								goto ExitLabel;
							}
						}
						if(percent > percentEver)
						{
							break;
						}
					}
				}
			}
			else
			{
				for(long long i=1;i<level;i++)
				{
					for(long long j=i;j>=0;j--)
					{
						wonEver = wonToday + j;
						totalEver = totalToday + i;
						long long percent = (wonEver*100)/totalEver;
						if(percent==(long long)percentEver)
						{
							if((wonEver*100)%totalEver == 0)
							{
								isEverPossible=true;
								goto ExitLabel;
							}
						}
						if(percent < percentEver)
						{
							break;
						}
					}
				}
			}

		}
		else
		{
			possible = false;
		}
ExitLabel:
		if(isTodayPossible && isEverPossible)
			op<<"Case #"<<caseNo<<": Possible"<<endl;
		else
			op<<"Case #"<<caseNo<<": Broken"<<endl;
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