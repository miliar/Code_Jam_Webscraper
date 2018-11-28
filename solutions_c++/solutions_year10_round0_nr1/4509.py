#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <stdlib.h>
using namespace std;
bool oposto(bool bl)
{
	if(bl)
	{
		return false;
	}
	return true;
}
bool calcula(int n, int k)
{
	bool* snappers;
	snappers=new bool[n];
	for(int a=0; a<=n-1; a++)
	{
		snappers[a]=false;
	}
	for(int a=0; a<=k-1; a++)
	{
		for(int a=0; a<=n-1; a++)
		{
			if(snappers[a])
			{
				snappers[a]=false;
			}
			else
			{
				snappers[a]=true;
				break;
			}
		}
	}
	for(int a=0; a<=n-1; a++)
	{
		if(!snappers[a])
		{
			return false;
		}
	}
	delete[] snappers;

	return true;
}
int main()
{
	int t,n;
	long k;
	char* auxiliar;
	fstream fileIn, fileOut;
	string input, output;
	fileIn.open("A-small.in", ios::in);
	fileOut.open("A-small.out", ios::out);
	
	getline(fileIn, input);
	t=atoi(&input[0]);
	for(int a=1; a<=t; a++)
	{
		getline(fileIn, input);
		auxiliar=strtok(&input[0]," ");
		n=atoi(auxiliar);
		auxiliar=strtok(NULL, " ");
		k=atoi(auxiliar);
		if(calcula(n,k))
		{
			fileOut<<"Case #"<<a<<": ON"<<endl;
		}
		else
		{
			fileOut<<"Case #"<<a<<": OFF"<<endl;
		}
	}
	
	fileIn.close();
	fileOut.close();
}
