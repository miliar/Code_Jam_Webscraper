#include "Robot.h"

using namespace std;

void Robot::executeDecision(int decision, int robNo)
{
	if(robNo == 0)
	{
		if(decision == 1)
			posO++;
		else if(decision == 2)
			posO--;
		else if(decision == 3)
		{
			this->pushButtonPerformed = true;
			this->JobDoneByO++;
		}
	}
	else if(robNo == 1)
	{
		if(decision == 1)
			posB++;
		else if(decision == 2)
			posB--;
		else if(decision == 3)
		{
			this->pushButtonPerformed = true;
			this->JobDoneByB++;
		}
	}
}

int Robot::makeDecision(Job j)
{
	if(j.belongsTo == 0)
	{
		if(j.belongsTo == -1)
			return 0;
		else if(posO < j.pushButton)
			return 1;
		else if(posO > j.pushButton)
			return 2;
		else if(posO == j.pushButton && j.jobNo == this->finalJobDone)
			return 3;
	}
	else if(j.belongsTo == 1)
	{
		if(j.belongsTo == -1)
			return 0;
		else if(posB < j.pushButton)
			return 1;
		else if(posB > j.pushButton)
			return 2;
		else if(posB == j.pushButton && j.jobNo == this->finalJobDone)
			return 3;
	}
	return 0;


}

int Robot::getResult()
{
	int JobsOfO = 0;
	int JobsOfB = 0;

	int iterator = 0;
	while(iterator != this->totalJobs)
	{
		if(JobQueue[iterator].belongsTo == 0)
			JobsOfO++;
		else
			JobsOfB++;
		iterator++;
	}

	Job * JobO; 
	JobO = new Job[JobsOfO];
	Job * JobB; 
	JobB = new Job[JobsOfB];

	int itO = 0;
	int itB = 0;
	iterator = 0;
	while(iterator != this->totalJobs)
	{
		if(JobQueue[iterator].belongsTo == 0)
		{
			JobO[itO] = JobQueue[iterator];
			itO++;
		}
		else
		{
			JobB[itB] = JobQueue[iterator];
			itB++;
		}
		iterator++;
	}

	int decisionO = 0;
	int decisionB = 0;
	
	int time = 0; 
	while(this->finalJobDone != this->totalJobs)
	{
		Job CurrentJobOfO;
		Job CurrentJobOfB;

		if(JobDoneByO < JobsOfO)
			CurrentJobOfO = JobO[this->JobDoneByO];
		if(JobDoneByB < JobsOfB)
			CurrentJobOfB = JobB[this->JobDoneByB];
	
		decisionO = makeDecision(CurrentJobOfO);
		decisionB = makeDecision(CurrentJobOfB);

		this->executeDecision(decisionO,0);
		this->executeDecision(decisionB,1);

		if(pushButtonPerformed == true)
		{
			this->finalJobDone++;
			pushButtonPerformed = false;
		}

		time++;
	}
	return time;
}