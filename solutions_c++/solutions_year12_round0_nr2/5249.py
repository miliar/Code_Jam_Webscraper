#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <stdlib.h>
using namespace std;
int calculate(char word[10][110]);
int main(int argc, char* argv[])
{
	int NO,a,i=0;
	string line;
	char MAX[10];
	
	char word[10][110];
	ifstream myfile (argv[1]);
	ofstream out ("output.txt");
	if (myfile.is_open())
	{
		
		while (!myfile.eof())
		{
			
			if(i!=0)
			{
				out<<"Case #"<<i<<": ";
				myfile>>word[0]>>word[1]>>word[2];
				for(int j=3;j<3+atoi(word[0]);j++)
				{
					myfile>>word[j];
				}
				out<<calculate(word);
				out<<endl;	
			}
			else
				myfile>>MAX;
			i++;
		}
		myfile.close();
		out.close();
	}
}
int calculate(char line[10][110])
{
	int NO=atoi(line[0]),SUR=atoi(line[1]),point=atoi(line[2]);
	int Arr[10],n=0;
	for(int j=0;j<NO;j++)
	{		Arr[j]=atoi(line[j+3]);
	}
	for(int j=0;j<NO;j++)
	{
		int goo=Arr[j]%3;
		int score=Arr[j]/3;
		if(goo==0)
		{
			if(score>=point)
				n++;
			else
			{
				if(SUR>0 && score>0 && score+1>=point)
				{
					n++;
					SUR--;
					
				}
			}
		}
		else if(goo==1)
		{
			if(score>=point || score+1>=point)
				n++;
			else
			{
				if(SUR>0 && score+1>=point)
				{
					n++;
					SUR--;
				}
			}
		}
		else if(goo=2)
		{
			if(score+1>=point || score>=point)
				n++;
			else
			{
				if(SUR>0 && score+2>=point)
				{
					n++;
					SUR--;
				}
			}
		}
		
	}
	return n;
}


