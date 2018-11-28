#include <iostream>
#include <cstdio>
#include <fstream>
#include <map>
#include <string>
#include <sstream>
#include <vector>


class CentralSystem
{
private:
	std::map<std::string, std::string> sengines;
	std::vector<std::string> queries;
	int nswitches;

public:
	CentralSystem()
		:nswitches(0)
	{
	}
	void setSearchEngines(std::map<std::string, std::string> &se)
	{
		this->sengines = se;
	}

	void setQueryList(std::vector<std::string> &q)
	{
		this->queries = q;
	}

	int performQueries()
	{
		//now, we nee to find the search engine with longest "run"
		while(!this->queries.empty())
		{
			this->nextLongestRun();
			this->nswitches++;
		}
		
		return this->nswitches;
	}

	//how long before we need to switch for each engine
	void nextLongestRun()
	{
		int maxrun = 0;

		//select an engine
		for(std::map<std::string, std::string>::iterator i = this->sengines.begin();
			i != this->sengines.end();
			++i)
		{
			int currun = 0;

			for(std::vector<std::string>::reverse_iterator riq = this->queries.rbegin();
				riq != this->queries.rend();
				++riq)
			{
				if(*riq == i->first) break;
				currun++;
			}//for

			if(currun > maxrun)
				maxrun = currun;
		}//for

		//remove the maxrun queries
		for(int i=0;i<maxrun;i++) this->queries.pop_back();
	}

	int get_nswitches()
	{
		return this->nswitches;
	}

	void reset()
	{
		this->sengines.clear();
		this->queries.clear();
		this->nswitches = 0;
	}
};

class Feeder
{
private:
	struct TestcaseInfo
	{
		std::map<std::string, std::string> se;
		std::vector<std::string> qryvec;

		void reset()
		{
			this->se.clear();
			this->qryvec.clear();
		}
	};

	CentralSystem cs;
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

			this->collectSearchEngines(info);
			this->collectQueries(info);
			
			this->performTestcase(i, info);
		}//for
	}

private:
	void collectSearchEngines(TestcaseInfo &info)
	{
		//get the number of search engines
		std::string line;
		std::getline(this->f, line);
		std::istringstream t(line);	
		int n;

		t>>n;

		for(int i=0;i<n;i++)
		{
			std::getline(this->f, line);
			info.se[line] = line;
		}//for

	}

	void collectQueries(TestcaseInfo &info)
	{
		//get the number of queries
		std::string line;
		std::getline(this->f, line);
		std::istringstream t(line);	
		int n;

		t>>n;

		for(int i=0;i<n;i++)
		{
			std::getline(this->f, line);
			info.qryvec.push_back(line);
		}//for
	}

	void performTestcase(int casenum, TestcaseInfo &info)
	{
		//add all the search engines to central system
		cs.setSearchEngines(info.se);
		cs.setQueryList(info.qryvec);
		int n = cs.performQueries();
		cs.reset();

		//print the number of switches
		std::cout<<"Case #"<<casenum+1<<": "<<n<<std::endl;
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