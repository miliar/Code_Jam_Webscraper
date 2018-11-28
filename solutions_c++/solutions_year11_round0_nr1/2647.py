#include<stdio.h>
#include<vector>
#include<utility>

#define ORANGE 0
#define BLUE 1

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);
    for(int round = 0;round < T ;round++)
    {
    	vector<int> Orange,Blue;
    	vector<int> task;
    	int N;
    	scanf("%d ",&N);
    	for(int i=0;i<N;i++)
    	{
			char temp[5];
			int button;
			scanf("%s %d",temp,&button);
			if(temp[0] == 'O')
			{
				Orange.push_back(button);
				task.push_back(ORANGE);
			}
			else
			{
				Blue.push_back(button);
				task.push_back(BLUE);
			}
		}
		/*for(int i=0;i<task.size();i++)
			printf("%d ",task[i]);
		for(int i=0;i<Orange.size();i++)
			printf("%d ",Orange[i]);
		for(int i=0;i<Blue.size();i++)
			printf("%d ",Blue[i]);*/
		
		int CurrentPos[2]={1,1};
		int CurrentTask[3] = {0,0,0};
		int sumTime = 0;
		while(CurrentTask[2] != task.size())
		{
			int cTask = 0;;
			if(Orange.size() > 0 && CurrentPos[ORANGE] == Orange[CurrentTask[ORANGE]] && ORANGE == task[CurrentTask[2]])
			{
				CurrentTask[ORANGE]++;
				cTask = 1;
			}
			else if(Orange.size() > 0)
			{
				if(Orange[CurrentTask[ORANGE]] > CurrentPos[ORANGE])
					CurrentPos[ORANGE]++;
				else if(Orange[CurrentTask[ORANGE]] < CurrentPos[ORANGE])
					CurrentPos[ORANGE]--;
			}
			
			if(Blue.size() > 0 && CurrentPos[BLUE] == Blue[CurrentTask[BLUE]] && BLUE == task[CurrentTask[2]])
			{
				CurrentTask[BLUE]++;
				cTask = 1;
			}
			else if(Blue.size() > 0)
			{
				
				if(Blue[CurrentTask[BLUE]] > CurrentPos[BLUE])
					CurrentPos[BLUE]++;
				else if(Blue[CurrentTask[BLUE]] < CurrentPos[BLUE])
					CurrentPos[BLUE]--;
			}
			CurrentTask[2] += cTask;
			//printf("%d %d\n",CurrentPos[BLUE],CurrentPos[ORANGE]);
			sumTime++;
		}
		
		printf("Case #%d: %d\n",round+1,sumTime);
    }
    return 0;
}
