#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <stack>
using namespace std;


typedef long long cybers ;


#define MAX_SIZE 1000
#define INFINITY 1000000000
#define PI 3.1415926

#define PRT_F(a,b) cout<<"Case #"<<a<<": "<<b<<endl;


int main()
{
	char tchar;
	int tvalue;
	freopen("A-large.in","rt",stdin); freopen("A-large.out","wt",stdout);
	int robots[MAX_SIZE];
	int actions[MAX_SIZE];
	int p = 0;
	int T = 0;
	cin>>T;

	while (p<T)
		{
		int result = 0;
		int turns = 0;
		
		int Robo0Pos = 1;
		int Robo1Pos = 1;

		int Robo0Target = 0;
		int Robo1Target = 0;

		int Robo0TargetIndex = 0;
		int Robo1TargetIndex = 0;
		

		cin>>turns;
		int tempcounter = 1;
		while (tempcounter<=turns)
			{
				cin>>tchar>>tvalue;
				actions[tempcounter] = tvalue;
				robots[tempcounter] = (tchar == 'O')?0:1;
				tempcounter++;
			}//datareaded

		int counter = 1;
		while (counter <= turns)
			{
				if (robots[counter] == 0)
					{
					Robo0TargetIndex = counter;
					Robo0Target = actions[counter];
					break;
					}
				counter++;
			}
		if (counter == turns+1)
			{
			Robo0TargetIndex = counter;
			Robo0Target = 1000;
			}
		counter = 1;
		while (counter <= turns)
			{
				if (robots[counter] == 1)
					{
					Robo1TargetIndex = counter;
					Robo1Target = actions[counter];
					break;
					}
				counter++;
			}
		if (counter == turns+1)
			{
			Robo1TargetIndex = counter;
			Robo1Target = 1000;
			}

		//base position set
		int usedtime = 0;
		while (Robo0TargetIndex <= turns || Robo1TargetIndex <= turns)
			{
			
			int Robo0Dis = fabs(double(Robo0Target-Robo0Pos));
			int Robo1Dis = fabs(double(Robo1Target-Robo1Pos));
				if (Robo0TargetIndex<Robo1TargetIndex)
					{
					if (Robo0Dis<=Robo1Dis)
						{
						Robo0Pos = Robo0Target;
							if (Robo1TargetIndex!=turns+1) 
								if (Robo1Pos<Robo1Target)
									{
									Robo1Pos+=Robo0Dis;
									if (Robo1Pos!=Robo1Target)
										Robo1Pos++;
									}
								else
									{
									Robo1Pos-=Robo0Dis;
									if (Robo1Pos!=Robo1Target)
										Robo1Pos--;
									}
							
						}
						else
						{
						Robo0Pos = Robo0Target;
						Robo1Pos = Robo1Target;
						}
						//find new target to robo0
						Robo0TargetIndex++;
						while (Robo0TargetIndex <= turns)
						{
							
							if (robots[Robo0TargetIndex] == 0)
								{
								
								Robo0Target = actions[Robo0TargetIndex];
								break;
								}
							Robo0TargetIndex++;
						}
						if (Robo0TargetIndex == turns+1)
							{
							Robo0TargetIndex = turns+1;
							Robo0Target = 1000;
							}
						//end of search
						usedtime +=(Robo0Dis+1);
						//
					}
				else
					{
						if (Robo1Dis<=Robo0Dis)
						{
						Robo1Pos = Robo1Target;
							if (Robo0TargetIndex!=turns+1) 
								if (Robo0Pos<Robo0Target)
									{
									Robo0Pos+=Robo1Dis;
									if (Robo0Pos!=Robo0Target)
										Robo0Pos++;
									}
								else
									{
									Robo0Pos-=Robo1Dis;
									if (Robo0Pos!=Robo0Target)
										Robo0Pos--;
									}
							
						}
						else
						{
						Robo1Pos = Robo1Target;
						Robo0Pos = Robo0Target;
						}
						//find new target to robo1
						Robo1TargetIndex++;
						while (Robo1TargetIndex <= turns)
						{
							if (robots[Robo1TargetIndex] == 1)
								{
								
								Robo1Target = actions[Robo1TargetIndex];
								break;
								}
							Robo1TargetIndex++;
						}
						if (Robo1TargetIndex == turns+1)
							{
							Robo1TargetIndex = turns+1;
							Robo1Target = 1000;
							}
						//end of search
						usedtime +=(Robo1Dis+1);
						//

					}

			//usedtime++;
			}
			

		 p++;
		 PRT_F(p,usedtime);
		}


	
}

