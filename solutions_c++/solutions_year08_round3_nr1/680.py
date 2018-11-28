#include <fstream>

class Processor
{
public:
	virtual void process(std::ifstream &ifs, std::ofstream &ofs) = 0;
};

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

#include "main.h"

class Feeder
{
private:
	std::ifstream ifs;
	std::ofstream ofs;
	Processor &p;

public:
	Feeder(char const *ifile, char const *ofile, Processor &proc)
		:ifs(ifile), ofs(ofile), p(proc)
	{
		//open the file	
		if(!ifs.is_open())
			throw "Cannot open input file!!";

		if(!ofs.is_open())
			throw "Cannot open output file!!";
	}

	void start()
	{
		int numcases;

		//get the number of test cases
		this->ifs >> numcases;
		int i=1;

		while(!this->ifs.eof() && i <= numcases)
		{
			this->ofs << "Case #" << i++ << ": ";
			p.process(this->ifs, this->ofs);
			this->ofs << std::endl;

		}
	}
};

int main(int argc, char *argv[])
{
	extern Processor &myproc;

	try	{
		//myproc is the new object of class derived from the 
		//Processor abstract class, to process each test case
	Feeder f(argv[1], "output.txt", myproc);

	f.start();

	} catch(char const *msg) {
		std::cerr<<"Error: " << msg << std::endl;
	}

	return 0;
}


#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include "main.h"

#define SQR(x) ((x)*(x))
#define PI 3.1415926
#define RIGHTANGLE 90

class SmsOutrageProc:public Processor
{
public:
	void process(std::ifstream &ifs, std::ofstream &ofs)
	{
		int P;
		int K;
		int L;

		int n = 0;

		ifs >> P >> K >> L;

		std::vector<int> freq(L);

		for(int i=0;i<L;i++)
			ifs >> freq[i];

		std::sort(freq.begin(), freq.end());
		std::reverse(freq.begin(), freq.end());

		int maxI = freq.size()/K;
		int mult = 1;
		int j;
		for(int i=0;(i< maxI) && (mult <= P);i++,mult++)
		{
			int startJ = i*K;
			int endJ = (i+1)*K;

			for(j=startJ;j<endJ;j++)
				n += mult * freq[j];
		}//for

		for(;j<freq.size();j++)
			n += mult * freq[j];

		ofs << n;
	}
};

SmsOutrageProc p;
Processor &myproc = p;


