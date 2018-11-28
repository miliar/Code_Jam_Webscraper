#include <iostream>
#include <algorithm>
#include <cstdio>
#include <fstream>
#include <map>
#include <string>
#include <sstream>
#include <vector>

class Feeder
{
private:

	struct TestcaseInfo
	{
		int turnaround;
		std::vector<int> fromA; //times at which trains must start from A
		std::vector<int> fromB; 
		std::vector<int> atA; //times at which trains are available at A
		std::vector<int> atB;
		
		void reset()
		{
			this->fromA.clear();
			this->fromB.clear();
			this->atA.clear();
			this->atB.clear();
			this->turnaround = 0;
		}
	};

	std::fstream f;

public:
	Feeder(char const *filename)
		:f(filename)
	{
		//open the file	
		if(!f.is_open())
		{
			throw "Cannot open the file!!";
		}
	}

	void start()
	{
		std::string line;

		//get the number of test cases
		std::getline(this->f, line);
		std::istringstream t(line);	
		int numcases;

		t>>numcases;
		TestcaseInfo info;

		//for each test case
		for(int i=0;i<numcases;i++)
		{
			info.reset();

			this->collect(info);
			
			this->performTestcase(i, info);
		}//for
	}

private:
	void collect(TestcaseInfo &info)
	{
		//get the turnaround time
		std::string line;
		std::getline(this->f, line);
		std::stringstream  t;
		
		t.str(line);	
		t>>info.turnaround;

		std::getline(this->f, line);
		t.str(line);
		int na, nb;

//		t>>na>>nb;
		sscanf(line.c_str(), "%d %d", &na, &nb);
		//t>>nb;

		for(int i=0;i<na;i++)
		{
			std::getline(this->f, line);

			int ah,am, dh, dm;
			sscanf(line.c_str(), "%d:%d %d:%d", &dh, &dm, &ah, &am);

			info.fromA.push_back(dh*60+dm);
			info.atB.push_back(ah*60+am+info.turnaround);
		}//for

		for(int i=0;i<nb;i++)
		{
			std::getline(this->f, line);
			int ah,am, dh, dm;
			sscanf(line.c_str(), "%d:%d %d:%d", &dh, &dm, &ah, &am);

			info.fromB.push_back(dh*60+dm);
			info.atA.push_back(ah*60+am+info.turnaround);
		}//for
	}

	void performTestcase(int casenum, TestcaseInfo &info)
	{
		int na = 0;
		int nb = 0;

		std::sort(info.atA.begin(), info.atA.end());
		std::sort(info.atB.begin(), info.atB.end());
		std::sort(info.fromA.begin(), info.fromA.end());
		std::sort(info.fromB.begin(), info.fromB.end());

		for(std::vector<int>::iterator i=info.fromA.begin();
			i != info.fromA.end();
			++i)
		{
			bool found_train = false;
			for(std::vector<int>::iterator j=info.atA.begin();
				j != info.atA.end();
				++j)
			{
				if(*j <= *i)
				{
					found_train = true;
					info.atA.erase(j);
					break;
				}
			}//for

			if(!found_train) na++;
		}//for

		for(std::vector<int>::iterator i=info.fromB.begin();
			i != info.fromB.end();
			++i)
		{
			bool found_train = false;
			for(std::vector<int>::iterator j=info.atB.begin();
				j != info.atB.end();
				++j)
			{
				if(*j <= *i)
				{
					found_train = true;
					info.atB.erase(j);
					break;
				}
			}//for

			if(!found_train) nb++;
		}//for

		std::cout<<"Case #"<<casenum+1<<": "<<na<<" "<<nb<<std::endl;
	}
};

int main(int argc, char *argv[])
{
	try	{
	Feeder f(argv[1]);

	f.start();

	} catch(...) {
		std::cerr<<"Error\n";
	}

	return 0;
}
