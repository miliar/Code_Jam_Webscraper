#include "CentralSystem.h"

CentralSystem::CentralSystem()
{
	machines = new vector<string>();
	queries = new vector<string>();
	result = 0;
}

CentralSystem::~CentralSystem()
{
	delete machines;
	delete queries;
}

void CentralSystem::addMachine(string machine)
{
	machines->push_back(machine);
}

void CentralSystem::addQuerie(string querie)
{
	queries->push_back(querie);
}

void CentralSystem::solve()
{
	int index = -1;
	int i = 0;

	while(true)
	{
		for(vector<string>::iterator itMc = machines->begin();
			itMc != machines->end();
			itMc++)
		{
			string machine = *itMc;
			bool find = false;

			for(int j = i; j < (int)queries->size(); j++)
			{
				if(machine == (*queries)[j])
				{
					find = true;
					if(index < j)
						index = j;
					break;
				}
			}

			if(!find)
			{
				index = -1;
				break;
			}

		}

		if(index != -1)
		{
			i = index;
			index = -1;
			result++;
		}
		else
			break;
	}
}

int CentralSystem::getResult()
{
	return result;
}