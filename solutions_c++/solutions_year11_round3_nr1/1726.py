// Jai Mata Di
// GCJ 2011 Online Round 3 Problem No. A

#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;
int main()
{
	try{

	// Prepare File Stream
	ifstream ip("ipA.txt");
	ofstream debug("debugA.txt");
	ofstream op("opA.txt");
	if(!ip.is_open() || !op.is_open())
		cout<<"Cannot Open File";
	
	int noOfTestCases=0;
	ip>>noOfTestCases;

	for(int testCaseNo=1; testCaseNo<=noOfTestCases; testCaseNo++)
	{
		bool possible = true;

		int rows=0;
		int cols=0;
		ip>>rows>>cols;

		vector<vector<char> > grid;
		for(int i=0;i<rows;i++)
		{
			vector<char> line;
			for(int j=0;j<cols;j++)
			{
				char c;
				ip>>c;

				line.push_back(c);
			}
			grid.push_back(line);
		}

		for(int i=0;i<rows;i++)
		{
			for(int j=0;j<cols;j++)
			{
				if(grid[i][j] =='#')
				{
					if(j==cols-1)
					{
						possible = false;
						goto exitLabel;
					}
					else if(grid[i][j+1]=='#')
					{
						if(i==rows-1)
						{
							possible = false;
							goto exitLabel;
						}
						else if(grid[i+1][j] == '#' && grid[i+1][j+1]=='#')
						{
							grid[i][j]    ='/';
							grid[i][j+1]  ='\\';
							grid[i+1][j]  ='\\';
							grid[i+1][j+1]='/';
						}
						else
						{
							possible = false;
							goto exitLabel;
						}
					}
					else
					{
						possible = false;
						goto exitLabel;
					}
				}
			}
		}
exitLabel:
		if(possible)
		{
			op<<"Case #"<<testCaseNo<<": "<<endl;
			for(int i=0;i<rows;i++)
			{
				for(int j=0;j<cols;j++)
				{
					op<<grid[i][j];
				}
				op<<endl;
			}
		}
		else
		{
			op<<"Case #"<<testCaseNo<<": "<<endl<<"Impossible"<<endl;
		}
	}
	
	//Closure
	ip.close();
	op.close();
	}
	catch(exception e)
	{
		cout<<"Excp"<<e.what();	
	}
	cout<<"EndOfProgram";
	return 0;
}

/*_____________________Code Dump____________________________
____________________Code Dump End____________________________*/