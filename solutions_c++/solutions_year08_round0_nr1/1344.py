/*
care should be taken while providing the input values: there should not be any space or within the same line
remove them by using replace all of any text editor
*/

#include <iostream>
using namespace std;

int inputCount;
int engineCount;
int queryCount;
char engine[100][200];
int engineLen[100];
char query[1000][200];
int queryLen[1000];
int result[20];

int CountSwitches(int);

void main()
{
	int len;

	cout<<endl<<"Enter number of input test cases :";
	cin>>inputCount;
	cout<<endl<<"Enter entire input data at once:"<<endl;

	for(int i=0; i<inputCount; i++)
	{
		cin>>engineCount;
		for(int j=0; j<engineCount; j++)
		{
			cin>>engine[j];
			for(len=0; engine[j][len]!='\0'; len++);
			engineLen[j]=len;
		}
		cin>>queryCount;
		for(int j=0; j<queryCount; j++)
		{
			cin>>query[j];
			for(len=0; query[j][len]!='\0'; len++);
			queryLen[j]=len;
		}
		result[i] = CountSwitches(i);
	}
	
	for(int i=0; i<inputCount; i++)
	{
		cout<<endl<<"Case #"<<i+1<<": "<<result[i];
	}
}

int CountSwitches(int input)
{
	int switchCount=0;
	int querySeq=-1;
	int tempQuerySeq=querySeq;
	bool match;
	bool found;

	while(querySeq+1<queryCount)
	{
		tempQuerySeq=querySeq;

		for(int i=0; i<engineCount; i++)
		{
			found = false;

			for(int j=tempQuerySeq+1; j<queryCount; j++)
			{
				match=true;
				if(engineLen[i]==queryLen[j])
				{
					for(int k=0; k<engineLen[i]; k++)
					{
						if(engine[i][k]!=query[j][k])
						{
							match=false;
							break;
						}
					}
				}
				else
				{
					match=false;
				}
				
				if(match)
				{
					querySeq<j-1?querySeq=j-1:querySeq=querySeq;
					found=true;
					break;
				}
			}

			if(!found)
			{
				return switchCount;
			}
		}

		switchCount++;
	}
	return switchCount;
}