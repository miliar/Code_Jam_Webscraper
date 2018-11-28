#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main(){
	ifstream infile("A-large.in.txt");
	if(!infile)
		cout<<"Can not open the input file!";
	ofstream outfile("out.txt");
	if(!outfile)
		cout<<"Can not open the output file!";

	int numOfLine,totalNumOfLine,numOfSearchEngine,numOfQueries;
		
	infile>>numOfLine;	
	totalNumOfLine = numOfLine;
	while(numOfLine){
		infile >> numOfSearchEngine;
		string *searchEngines= new string[numOfSearchEngine];
		int *flagOfQueries= new int[numOfSearchEngine];
		int count=0;
		int totalCount=0;


		char *temp =new char[100];
			//string temp;
			//infile>>temp;
			infile.getline(temp,100);
		for (int i=0;i<numOfSearchEngine;i++)
		{
			char *temp =new char[100];
			//string temp;
			//infile>>temp;
			infile.getline(temp,100);
			searchEngines[i]=temp;
			delete temp;
		}

		
		infile >> numOfQueries;
			infile.getline(temp,100);
			delete temp;
		string query;
		for (i=0;i<numOfQueries;i++)
		{
			char *temp =new char[100];
			infile.getline(temp,100);
			query = temp;
			delete temp;
			for (int j=0;j<numOfSearchEngine;j++)
			{
				if (searchEngines[j]==query)
				{
					if (flagOfQueries[j]!=1)
					{
						flagOfQueries[j]=1;
						count++;
					}

					if (count==numOfSearchEngine)
					{
						totalCount++;
						for (int k=0;k<numOfSearchEngine;k++)
						{
							flagOfQueries[k]=0;
						}
						flagOfQueries[j]=1;
						count=1;
					}
					
				}
			}
		}

		outfile<<"Case #"<<totalNumOfLine-numOfLine+1<<": "<<totalCount<<endl;
		delete [] searchEngines;
		delete [] flagOfQueries;
		numOfLine--;
	}


	return 0;
}