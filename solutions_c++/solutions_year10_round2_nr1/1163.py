#include <stdint.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <list>

using namespace std;

#define CJ_min(a,b) ((a > b)?a:b)
#define CJ_max(a,b) ((a > b)?b:a)

#define CJ_pow2(a) (1<<a)

#define CJ_Pos2d(arr,w,x,y) (arr[x*w+y])


typedef std::list<std::string> DirectoryList;

int64_t ReadInt(std::ifstream& str)
{
	int64_t val;
	str >> val;
	return val;
}

std::string ReadString(std::ifstream& str)
{
	std::string val;
	str >> val;
	return val;
}

DirectoryList SplitAtSlashes(string str)
{
	DirectoryList tokens;
	
	string::size_type lastSlash = str.find_last_of("/");

    	while (lastSlash > 1)
    	{
        	tokens.push_back(str.substr(0, lastSlash));
        	lastSlash = str.find_last_of("/", lastSlash-1);

    	}


	return tokens;

}

int CountSlashes(string str)
{
	return count(str.begin(),str.end(),'/');
}

int DoFileFixit(DirectoryList existing, DirectoryList toCreate)
{
	//Initialize numMkDirs
	int numMkDirs = 0;
	//Sort the directories to create.
	toCreate.sort();
	while (toCreate.size())
	{
		//Re-sort the existing list
//		existing.sort();
		//Get the next directory to create and remove it from the list.
		string createme = toCreate.front();
		toCreate.pop_front();

		DirectoryList::iterator it=existing.begin();
		int numExistingSlashes = 0;
		int prevExistingSlashes = 0;
		while (it != existing.end())
		{
			int pos = createme.find((*it),0);
			if (pos != 0) { it++; continue;}
			if (((*it).length() == createme.length()) || (createme.at((*it).length()) == '/'))
			{
				//We begin with this directory
				int tmpv = CountSlashes(*it);
				if (tmpv > numExistingSlashes)
				{
					numExistingSlashes = tmpv;
					cout << "[" << tmpv << "]" << *it << endl;
				}
			}
//			else if (numExistingSlashes)
			it++;
		}

		numMkDirs += CountSlashes(createme) - numExistingSlashes;
		cout << "NumMkDirs for " << createme << " is " << CountSlashes(createme) - numExistingSlashes << endl;
	
	
		//Now that it's created, push it onto the existing list
		existing.push_back(createme);
		existing.sort();
		DirectoryList  tmp = SplitAtSlashes(createme);
		DirectoryList& tmp2 = tmp;
		existing.merge(tmp2);
	}
	return numMkDirs;
}

void DoTrial(std::ifstream& in, std::ofstream& out)
{
	int numExisting = ReadInt(in);
	int numToCreate = ReadInt(in);

	DirectoryList existing;
	DirectoryList toCreate;

	for (int i = 0; i < numExisting; ++i)
	{
		existing.push_back(ReadString(in));
	}
	for (int i = 0; i < numToCreate; ++i)
	{
		toCreate.push_back(ReadString(in));
	}

	out << DoFileFixit(existing, toCreate);
	
}

int main(int argc, char **argv)
{
	std::ifstream infile(argc>2?argv[1]:"test.in");
	std::ofstream outfile(argc>2?argv[2]:"test.out");
	int64_t numTrials = ReadInt(infile);
	for (int64_t trial = 1; trial <= numTrials; ++trial)
	{
		outfile << "Case #" << trial << ": ";
		DoTrial(infile,outfile);
		outfile << std::endl;
	}
	return 0;
}
