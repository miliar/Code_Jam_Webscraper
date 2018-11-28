#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>

std::vector<std::string> separateString(std::string text, std::string delimiter)
{
	std::vector<std::string> result;
	size_t begin=0, end=0, length;

	while(end!=text.length())
	{
		begin = text.find_first_not_of(delimiter,end);
		end = text.find_first_of(delimiter, begin);
		if(end==std::string::npos)
			end = text.length();
		length = end - begin;

		result.push_back(text.substr(begin, length));
	}
	return result;
}

struct Train
{
	int dep;
	int arr;
	Train(int _dep=0, int _arr=0)
			: dep(_dep), arr(_arr) {}
};

class TrainCompare
{
    public:
			bool operator()(const Train &s1, const Train &s2)
			{
					return s1.dep > s2.dep;
			}
 };

int main(int argc, char** argv)
{
	std::ifstream iFile(argv[1]);
	if(!iFile.is_open())
	{
		std::cerr << "No input file " << argv[1] <<std::endl;
		return 1;
	}

	std::string tmp;
	int num_case;
	std::getline(iFile, tmp);
	num_case = atoi(tmp.c_str());

	std::ofstream oFile("result.txt");

	for(int c=0; c<num_case; c++)
	{
		int turnaround;
		std::getline(iFile, tmp);
		turnaround = atoi(tmp.c_str());

		std::getline(iFile, tmp);
		std::vector<std::string> NAB = separateString(tmp," ");
		int NA = atoi(NAB[0].c_str());
		int NB = atoi(NAB[1].c_str());

		// sort by departure time
		std::priority_queue<Train, std::vector<Train>, TrainCompare> a2b;
		std::priority_queue<Train, std::vector<Train>, TrainCompare> b2a;
		
		std::vector<std::string> t(4);
		for(int i=0; i<NA; i++)
		{
			std::getline(iFile, tmp);
			t = separateString(tmp," :");
			int dep = atoi(t[0].c_str())*60 + atoi(t[1].c_str());
			int arr = atoi(t[2].c_str())*60 + atoi(t[3].c_str());
			Train tr(dep,arr);
			a2b.push(tr);
		}
		for(int i=0; i<NB; i++)
		{
			std::getline(iFile, tmp);
			t = separateString(tmp," :");
			int dep = atoi(t[0].c_str())*60 + atoi(t[1].c_str());
			int arr = atoi(t[2].c_str())*60 + atoi(t[3].c_str());
			Train tr(dep,arr);
			b2a.push(tr);
		}

		int startA=0, startB=0;
		std::priority_queue<int, std::vector<int>, std::greater<int>> leaveA;
		std::priority_queue<int, std::vector<int>, std::greater<int>> leaveB;
		while(!(a2b.empty() && b2a.empty()))
		{
			Train tr;
			bool isA2B;	// true if the train is from A to B, false otherwise.
			if(!a2b.empty() && !b2a.empty())
			{
				if(a2b.top().dep < b2a.top().dep)
					isA2B = true;
				else if(a2b.top().dep == b2a.top().dep)
				{
					if(a2b.top().arr < b2a.top().arr)
						isA2B = true;
					else
						isA2B = false;
				}
				else
					isA2B = false;
			}
			else if(!a2b.empty())
			{
				isA2B = true;
			}
			else	// !b2a.empty()
			{
				isA2B = false;
			}

			if(isA2B)
			{
				tr = a2b.top();
				if(!leaveA.empty() && (tr.dep >= leaveA.top()))
				{
					leaveA.pop();
				}
				else
				{
					++startA;
				}
				leaveB.push(tr.arr+turnaround);
				a2b.pop();
			}
			else
			{
				tr = b2a.top();
				if(!leaveB.empty() && (tr.dep >= leaveB.top()))
				{
					leaveB.pop();
				}
				else
				{
					++startB;
				}
				leaveA.push(tr.arr+turnaround);
				b2a.pop();
			}
		}

		oFile << "Case #" << c+1 << ": " << startA << " " << startB << std::endl;

	}
	oFile.close();
	return 0;
}
