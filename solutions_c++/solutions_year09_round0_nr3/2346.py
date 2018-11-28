#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <queue>
#include <vector>

using namespace std;


ifstream o("C-small-attempt0.in");
ofstream oo("c.out");

int N;

//for reading data
const int LINE_LENGTH = 500; 
char str[LINE_LENGTH];

//phrase
string phrase="welcome to code jam";
const int PHRASE_LENGTH = phrase.length();

//the number of paths to here
int **paths = NULL;

void read()
{
	
	o>>N;
	cout<<N<<endl;
	o.getline(str,LINE_LENGTH);
	
}

void onecase(int n)
{
	int i, j;

	string temp;
	o.getline(str,LINE_LENGTH);
	
	cout<<"case "<<n<<": "<<str<<"......"<<endl;
	
	//paths
	if(paths !=NULL)
	{
		for(i=0; i<LINE_LENGTH; i++)
			delete paths[i];
		delete paths;
	}
	paths = new int*[LINE_LENGTH];
	for(i=0; i<LINE_LENGTH; i++)
	{
		paths[i] = new int[PHRASE_LENGTH];
		for(j=0; j<PHRASE_LENGTH; j++)
			paths[i][j] = 0;
	}

	//start
	for(i=0; str[i]!='\0'; i++)
	{
		char cc=str[i];
		if(cc==phrase[0])
			paths[i][0]=1;
	}
	//calculate
	for(i=0; str[i]!='\0'; i++)
	{
		char cc=str[i];
		for(j=1; j<PHRASE_LENGTH; j++)
		{
			if(cc==phrase.at(j))
			{
				
				for(int k=0; k<i; k++)
					paths[i][j]+=paths[k][j-1];
			}
		}
	}
	//end
	int result=0;
	for(i=0; str[i]!='\0'; i++)
	{
		char cc=str[i];
		if(cc==phrase[PHRASE_LENGTH-1])
			result+=paths[i][PHRASE_LENGTH-1];
	}
//	stringstream ss;
	//	ss<<str;
//		while(ss>>temp)
//			cout<<temp<<endl;

    char cresult[5];
	for(i=0; i<4; i++)
		cresult[i]='0';
	cresult[4]='\0';
	for(i=3; i>=0; i--)
	{
		cresult[i]='0'+result%10;
		result=result/10;
		if(result==0)
			break;
		
	}
	oo<<"Case #"<<n<<": "<<cresult[0]<<cresult[1]<<cresult[2]<<cresult[3]<<"\n";
	cout<<"Case #"<<n<<": "<<cresult[0]<<cresult[1]<<cresult[2]<<cresult[3]<<"\n";
}

int main()
{
	int result;
	read();
	cout<<"READ!"<<endl;
	for(int i=1; i<=N; i++)
	{	
		onecase(i);	
	}
	oo.close();
	return 0;
}
