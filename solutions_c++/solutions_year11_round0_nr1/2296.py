#include<iostream>
#include<fstream>
using namespace std;

void move(int &position,int goal,int t)
{
	if(goal == 0 || goal > 100)
		return;
		
	if(position < goal)
	   {
        if(goal - position > t)
			position += t;
        else
			position = goal;
		}
	else if(position > goal)
        {
		if(t < position - goal)
			position -= t;	
		else
			position = goal;
		} 		
}

int main()
{
	ifstream fin("A.in");
	ofstream fout("A.out");
 
	int CaseNum = 0;
	int N;
	int press[101];
	int color[101]; 
	int tmp,time,PositionO,PositionB,GoalO,GoalB;
	char c;
 
	fin>>CaseNum;
 
	for(int i = 1;i <= CaseNum; i++)
	{
        for(int j = 0;j <= 100;j++)
		{
			press[j] = 0;
			color[j] = 0;
        }
		
		time = 0;
        GoalO = 0;
        GoalB = 0;
        PositionO = 1;
        PositionB = 1;
        fin>>N;
         
        for(int j = 1;j<= N;j++)
		{   
			fin>>c;
			fin>>press[j];
			
			if(c == 'O')
				color[j] = 1;//the Jth one is Orange
			else 
				color[j] = 2;//the Jth one is Blue
        }
         
         for(int j = 1; j <= N; j++)
		 {
			if(color[j] == 1)
			{
			//search goal for the other color 
				for(int i = j; i <= N ; i++)
				{
					if(color[i] == 2)
					{	
					GoalB = press[i];
					break;
					}
					else continue;
				}
               
               //press            
				if(PositionO == press[j])
               {
				time += 1;
				move(PositionB,GoalB,1);
				continue;
				}
				
               //move
				if(PositionO < press[j])
					tmp = press[j] -  PositionO + 1;
				else	
					tmp = PositionO - press[j] + 1;
			   
				time += tmp;
				PositionO = press[j];
				move(PositionB,GoalB,tmp);
			}
			else
			{
			//search goal for the other color 
				for(int i = j; i <= N ; i++)
				{
					if(color[i] == 1)
					{	
					GoalO = press[i];
					break;
					}
				}
               
               //press            
				if(PositionB == press[j])
               {
				time += 1;
				move(PositionO,GoalO,1);
				continue;
				}
				
               //move
				if(PositionB < press[j])
					tmp = press[j] -  PositionB + 1;
				else	
					tmp = PositionB - press[j] + 1;
			   
				time += tmp;
				PositionB = press[j];
				move(PositionO,GoalO,tmp);
			}
		}
         
		fout<<"Case #"<<i<<": "<<time<<endl;
	}
         
	fin.close();
	fout.close();
	
	return 0;    
} 
