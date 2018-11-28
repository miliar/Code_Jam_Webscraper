//subrata mitra
//subrata4096@gmail.com

#include <fstream>
#include<string>
#include<stdlib.h>
#include <sstream>

using namespace std;

int main (int argc, char *argv[])
{
	string inputfilename = "";
	string outputfilename = "";

	if(argc < 2)
	{
		return 0;
	}	
	inputfilename = argv[1];
	outputfilename = argv[2];

	string line;
	fstream inputfile;
	inputfile.open(inputfilename.c_str(),ios::in);
	if (inputfile.is_open())
	{
		//none;	
	}
	else
	{
		return 0;
	}

	int i = 1;
	unsigned int T = 0;
	stringstream outputstr;
	while (! inputfile.eof() )
	{
		unsigned int N = 0;
		unsigned int K = 0;
		getline (inputfile,line);
		if(!line.empty())
		{
			if(i == 1)
			{
				T = atoi(line.c_str());
				i++;
				continue;
			}
			stringstream ss;
			ss<<line;
			while(!ss.eof())
			{
				ss>>N;
				ss>>K;
			}
			if(N == 0)
			{
				continue;
			}

			unsigned int resetPeriod = 1<<N;
			unsigned int onValue = resetPeriod - 1;

			unsigned int remainder = (K > resetPeriod) ? (K%resetPeriod) : K;
			outputstr<<"Case #" << i-1 <<": ";
			if(remainder == onValue)
			{
				outputstr<<"ON\n";
			}
			else
			{
				outputstr<<"OFF\n";
			}
			i++;

		}
	}
	inputfile.close();	

	fstream myfile;
	myfile.open(outputfilename.c_str(), ios::out);
	myfile << outputstr.str();
	myfile.close();

	return 0;


}

