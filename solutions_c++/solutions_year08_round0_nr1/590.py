#include<fstream>
#include<iostream>
#include<string>

using namespace std;
#define MAX_QUERY 1000
#define MAX_ENGINE 100
struct ENGINES {
	string name;
	int occurances[MAX_QUERY];
	int numofoccurances;
} engines[MAX_ENGINE];

void initEngines()
{
	for(int i=0;i<MAX_ENGINE;i++)
	{
		engines[i].name="";
		memset(engines[i].occurances,-1,MAX_QUERY*sizeof(int));
		engines[i].numofoccurances=0;
	}
}
void cutOccurence(int occurances[], int *numofoccurnces)
{ //cuts the first occurence from the occurence list
	for(int i=0;i<*numofoccurnces-1;i++)
		occurances[i]=occurances[i+1];
	occurances[*numofoccurnces-1]=-1;
	*numofoccurnces--;
}
bool getOccurence( string engine, int numofengines, int *whichenginehasthebiggest, int *biggestoccurence)
{ //gives back the biggest occurance of the not equal engines
  // or -1 if there is one engine which doesnt have any occurances left
  // if engine="" than we search between all engines
	bool havenegative=false;
	*biggestoccurence=-1;
	for(int i=0;i<numofengines;i++)
	{
		if(engines[i].name!=engine)
		{
			if(engines[i].occurances[0]==-1)
			{
				havenegative=true;
				break;
			}
			else if(engines[i].occurances[0]>*biggestoccurence)
			{
				*biggestoccurence=engines[i].occurances[0];
				*whichenginehasthebiggest=i;
			}
		}
	}
	return havenegative;
}
int solveProblem(int numofengines)
{
	int biggest=0;
	int biggestplace=0;
	int switches=0;
	string currentengine="";
	while(!getOccurence(currentengine,numofengines,&biggestplace,&biggest))
	{
		currentengine=engines[biggestplace].name;
		switches++;
		for(int i=0;i<numofengines;i++)
		{
			while(engines[i].occurances[0]<=biggest && engines[i].occurances[0]>-1)
				cutOccurence(engines[i].occurances,&engines[i].numofoccurances);
		}
	}
	return switches;
}
void main ( void )
{
	ofstream myoutput;
	myoutput.open("output.txt");
	ifstream myinput;
	myinput.open("input.txt");
	cout<<myinput.fail()<<endl;

	int N;
	myinput>>N;
	for(int i=0;i<N;i++)
	{ //we go on each case
		int S=0;
		int Q=0;
		initEngines();
		myinput>>S;
		for(int j=0;j<S;j++)
		{ //read the engine names
			getline(myinput,engines[j].name);
			if(engines[j].name=="")
				j--; /*something is wrong with the readbuffer*/
		}
		myinput>>Q;
		for(int j=0;j<Q;j++)
		{ //check the queries
			string query;
			getline(myinput,query);
			if(query!="")
			{
			for(int k=0;k<S;k++)
				if(query==engines[k].name)
					engines[k].occurances[engines[k].numofoccurances++]=j;
			}
			else
				j--; /*it is very rude solution but something seems to be worng with the read function*/
		}
		//now we should simply solve the problem from the occurances
		myoutput<<"Case #"<<i+1<<": "<<solveProblem(S)<<endl;
	}
}