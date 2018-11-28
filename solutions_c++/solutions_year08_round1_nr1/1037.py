// Minimum Scalar Product.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <fstream>

using namespace std;

struct Coor
{
	int coor;
	Coor* next;
};

int readNextField(ifstream& input, char* field)
{
	if(input.eof())
		return 0;

	char temp;
	int index = 0;

	input.read(&temp, 1);
	while(!input.eof() && temp != ' ' && temp != '\n'){		
		field[index] = temp;
		index++;
		input.read(&temp, 1);
	}
	return index;
}

int skipNextField(ifstream& input)
{
	if(input.eof())
		return 0;

	char temp;
	int index = 0;

	input.read(&temp, 1);
	while(!input.eof() && temp != ' ' && temp != '\n'){		
		index++;
		input.read(&temp, 1);
	}
	return index;
}

int main()
{
	ifstream inputFile("A-small-attempt1.in", ios::in);

	if(!inputFile)
	{
		cerr<<"File could not be opened"<<endl;
		exit(1);
	}

	//read number of cases
	int numberOfCase;
	inputFile>>numberOfCase;

	char* vecA;
	char* vecB;

	//system("pause");
	for(int i=1;i<=numberOfCase;i++)
	{
		int numberOfCoor;
		inputFile>>numberOfCoor;

		//read the vectorA
		Coor* coorHeadA = NULL;
		for(int j=0;j<numberOfCoor;j++)
		{
			Coor* inCoor = new Coor();			

			//read corrdinate
			inputFile>>inCoor->coor;			

			//sort the coor in increasing order
			Coor* temp = coorHeadA;
			Coor* prev = NULL;			
			if(temp != NULL)
			{
				while(inCoor->coor >= temp->coor)
				{
					prev = temp;
					if(temp->next != NULL)
						temp = temp->next;
					else
					{
						temp = NULL;
						break;
					}
				}
				if(prev == NULL)
				{
					inCoor->next = coorHeadA;
					coorHeadA = inCoor;
				}
				else
				{
					inCoor->next = temp;
					prev->next = inCoor;
				}
			}
			else
			{
				inCoor->next = NULL;
				coorHeadA = inCoor;				
			}			
		}

		//read the vectorB
		Coor* coorHeadB = NULL;
		for(int j=0;j<numberOfCoor;j++)
		{
			Coor* inCoor = new Coor();			

			//read corrdinate
			inputFile>>inCoor->coor;			

			//sort the coor in decreasing order
			Coor* temp = coorHeadB;
			Coor* prev = NULL;			
			if(temp != NULL)
			{
				while(inCoor->coor <= temp->coor)
				{
					prev = temp;
					if(temp->next != NULL)
						temp = temp->next;
					else
					{
						temp = NULL;
						break;
					}
				}
				if(prev == NULL)
				{
					inCoor->next = coorHeadB;
					coorHeadB = inCoor;
				}
				else
				{
					inCoor->next = temp;
					prev->next = inCoor;
				}
			}
			else
			{
				inCoor->next = NULL;
				coorHeadB = inCoor;				
			}			
		}

		//calculate the minimum product
		long min = 0;
		Coor* va = coorHeadA;
		Coor* vb = coorHeadB;
		for(int j=0;j<numberOfCoor;j++)
		{
			min += (va->coor)*(vb->coor);
			va = va->next;
			vb = vb->next;
		}

		cout<<"Case #"<<i<<": "<<min<<endl;
		
		Coor* deleteTemp = coorHeadA;
		Coor* deleteNext = NULL;
		while(deleteTemp!=NULL)
		{
			deleteNext = deleteTemp->next;
			delete deleteTemp;
			deleteTemp = deleteNext;
		}
		coorHeadA = NULL;

		deleteTemp = coorHeadB;
		deleteNext = NULL;
		while(deleteTemp!=NULL)
		{
			deleteNext = deleteTemp->next;
			delete deleteTemp;
			deleteTemp = deleteNext;
		}
		coorHeadA = NULL;
	}

	system("pause");

	return 0;
}

