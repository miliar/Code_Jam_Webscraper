#include <cstdio>
#include <string>
#include <queue>
#include <iostream>

struct step {
	int button;
	int order;
};

int howLong(std::queue<step>& q1, std::queue<step>& q2);
int main(int argc, char** argv)
{
	int tests, time1, time2, n, button;
	char bot[2];
	FILE* input, * output;
	input = fopen(argv[1], "r");
	output = fopen("output.txt", "w");
	fscanf(input, "%d", &tests);
	std::queue<step> q1, q2;
	step s;
	for(int i = 0; i < tests; i++)
	{
		fscanf(input, "%d", &n);
		for(int j = 0; j < n; j++)
		{
			fscanf(input, "%s", &bot);
			fscanf(input, "%d", &s.button);
			s.order = j;
			if(bot[0] == 'O')
				q1.push(s);
			else
				q2.push(s);
		}
		fprintf(output, "Case #%d: %d\n", i+1, howLong(q1, q2));
	}
	fclose(input);
	fclose(output);
	return 0;
}

int howLong(std::queue<step>& qO, std::queue<step>& qB)
{
	step currentStepO;
	currentStepO.order = -1;
	currentStepO.button = -1;
	step currentStepB;
	currentStepB.order = -1;
	currentStepB.button = -1;
	int time = 0;
	int locationO = 1, locationB = 1;
	while(!qO.empty() || !qB.empty())
	{
		if(!qO.empty())
			currentStepO = qO.front();
		if(!qB.empty())
			currentStepB = qB.front();
		if((currentStepB.order < currentStepO.order || qO.empty()) && !qB.empty())
		{
			while(locationB != currentStepB.button) 
			{
				if(locationO < currentStepO.button)
					locationO++;
				else if(locationO > currentStepO.button)
					locationO--;
				if(locationB < currentStepB.button)
					locationB++;
				else
					locationB--;
				time++;
			}
			if(!qB.empty())
			{
				qB.pop();
				if(locationO < currentStepO.button)
					locationO++;
				else if(locationO > currentStepO.button)
					locationO--;
				time++;
			}
		}
		else if(!qO.empty())
		{
			while(locationO != currentStepO.button) 
			{
				if(locationO < currentStepO.button)
					locationO++;
				else
					locationO--;
				if(locationB < currentStepB.button)
					locationB++;
				else if(locationB > currentStepB.button)
					locationB--;
				time++;
			}
			if(!qO.empty())
			{
				qO.pop();
				if(locationB < currentStepB.button)
					locationB++;
				else if(locationB > currentStepB.button)
					locationB--;
				time++;
			}
		}
	}
	return time;
}
