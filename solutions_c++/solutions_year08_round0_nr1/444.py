#include <iostream>
#include <fstream>
#include <string>
#include <vector>

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
		int num_engine, num_query;
		std::getline(iFile, tmp);
		num_engine = atoi(tmp.c_str());
		std::vector<std::string> engine;
		engine.resize(num_engine);
		for(int e=0; e<num_engine; e++)
		{
			std::getline(iFile, engine.at(e));
		}

		std::getline(iFile, tmp);
		num_query = atoi(tmp.c_str());
		std::vector<std::string> query;	// those match the engines' names
		for(int q=0; q<num_query; q++)
		{
			std::getline(iFile, tmp);
			for(int e=0; e<num_engine; e++)
			{
				if(tmp.compare(engine.at(e))==0)
					query.push_back(tmp);
			}
		}

		int switch_count=0;
		unsigned int pos=0;
		std::vector<int> engine_dist(num_engine);
		while(pos<query.size())
		{
			unsigned int selected_engine=0;
			unsigned int best_distance=0;
			for(int e=0; e<num_engine; e++)
			{
				unsigned int epos=pos;
				while(epos<query.size() && query.at(epos).compare(engine.at(e))!=0 )
					epos++;
				if(epos >= query.size())
				{
					selected_engine = e;
					best_distance = epos-pos;
					break;
				}
				else if(epos-pos > best_distance)
				{
					best_distance = epos-pos;
					selected_engine = e;
				}
			}

			pos += best_distance;
			if(pos < query.size())
				switch_count++;
		}

		oFile << "Case #" << c+1 << ": " << switch_count << std::endl;
	}
	oFile.close();

	return 0;
}

