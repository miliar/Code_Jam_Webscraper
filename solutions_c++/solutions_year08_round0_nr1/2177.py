#include <fstream>
#include <string>
#include <sstream>
#include <iostream>
#include <map>

using namespace std;


int main(int argc,char *argv[])
{
	string inputfile,outputfile;
	stringstream temp;
	fstream infile,outfile;
	int cases;
	int searchengines,queries;
	int switches;
	string inputline;
	map<string,int> enginemap;

	if(argc != 2)
	{
		cerr<<"please enter programname inputfile"<<endl;
		return 1;
	}
	inputfile = argv[1];
	infile.open(inputfile.c_str(),ios::in);
	outfile.open("output.txt",ios::out);

	getline(infile,inputline);
	temp << inputline;
	temp >> cases;

	for(int i=0;i<cases;++i)
	{
		switches = 0;
		getline(infile,inputline);
		temp.clear();temp.str("");
		temp << inputline;
		temp >> searchengines;

		//read searchengines
		for(int noofengines=0;noofengines<searchengines;noofengines++)
		{
			getline(infile,inputline);
		}
		getline(infile,inputline);
		temp.clear();temp.str("");
		temp << inputline;
		temp >> queries;

		//read queries
		for(int noq=0;noq<queries;++noq)
		{
			getline(infile,inputline);
			enginemap.insert(make_pair(inputline,1));
			if(enginemap.size()==searchengines)
			{
				switches++;
				enginemap.clear();
				enginemap.insert(make_pair(inputline,1));
			}
		}
		enginemap.clear();
		//write ouput
		outfile << "Case #"<<i+1<<": "<<switches<<endl;
		
	}

	infile.close();
	outfile.close();
	return 0;
}

