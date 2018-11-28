#include <iostream>
#include <vector>
#include <string>
#include <fstream>




using namespace std;


void removeSwitch(vector<string> &switches,string match)
	{
		
		bool find=false;
		int i=0;
		for(;i<switches.size();i++)
			if(switches[i]==match)
				{
					find=true;
					break;
				}

		if(find)
			switches.erase(switches.begin()+i);
	
	}






void main(){

	int totalCases;
	ifstream infile;
	ofstream outfile;

	
	
	infile.open("input.in");		 // open Input File "Input.in"
	outfile.open("output.in");       // open for Output

	infile>>totalCases;           // read total case from InputFile

	
for(int z=1;z<=totalCases;z++)
	{
		vector<string> switches;
		int countShift=0;
		int totalSwitches;
		int totalQuery;

		infile>>totalSwitches;
		char temp[110];
	    infile.getline(temp,110,'\n');
		for(int s=0;s<totalSwitches;s++)
			{
				
				infile.getline(temp,110,'\n');
				string tempS(temp);
				
				switches.push_back(tempS);	
			}
		
		
		infile>>totalQuery;

		
		vector<string> tempSwitches=switches;
		
		infile.getline(temp,110,'\n');
		for(int q=0;q<totalQuery;q++)
			{
				
				infile.getline(temp,110,'\n');
				string queryString(temp);
					
				if(tempSwitches.size()==1)
					{
					 if(tempSwitches[0]==queryString)
						{
							countShift++;
							tempSwitches=switches;
						}
					}
				removeSwitch(tempSwitches,queryString);
				
			}	

		outfile<<"Case #"<<z<<": "<<countShift<<endl;

	}//totalCases

	infile.close();
	outfile.close();



			
}//main

