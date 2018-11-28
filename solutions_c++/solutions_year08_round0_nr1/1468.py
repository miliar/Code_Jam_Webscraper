#include <set>
#include <iostream>
#include <string>
//#define DEBUG

int main(){
	int N;
	std::cin >> N;
	//for each test case:
	for (int cases = 1; cases <= N; ++cases){
		int S, Q;
		std::cin >> S;
		std::set<std::string> search_engines;
		//get the name of the search engines:
		std::cin.ignore(1000, '\n');
		for(int engines = 1; engines <= S; ++engines){
			char engine_name[101]; //extra 1 for the null character
			std::cin.getline(engine_name, 101);
			#ifdef DEBUG
				std::cout<<"	engine_name: "<< engine_name<<std::endl;
			#endif
			std::string engine_str(engine_name);
			search_engines.insert(engine_str);
		}
		#ifdef DEBUG
			std::cout << "	search_engines.size(): " << search_engines.size() <<std::endl;
			for(std::set<std::string>::iterator engines_iterator = search_engines.begin();
								engines_iterator != search_engines.end();
								++engines_iterator)
			{
				std::cout<< "	*engines_iterator: " << *engines_iterator <<std::endl;
			}
		#endif
		//then test the queries to get the minimum number of changes
		std::cin >> Q;
		int switches = 0;
		std::set<std::string> copy_of_engines = search_engines;
		std::cin.ignore(1000, '\n');
		for(int queries = 1; queries <= Q; ++queries){
			//here we see the search engine we must use to get the least
			//number of switches.
			//this is done by removing elements from the copy_of_engines set
			//until it's empty. the last element removed would be the first search
			//engine we start with, before we must switch. to find out which
			//engine we should switch to, this process is carried out again
			//(but with the first search engine already being switched away from, it
			//obviously can't be the one it switches to)
			char query[101]; //again includes one for null character
			std::cin.getline(query, 101);
			copy_of_engines.erase(std::string(query));
			if(copy_of_engines.empty()){
				++switches;
				copy_of_engines = search_engines;
				copy_of_engines.erase(std::string(query));
			}
		}
		//then print the number of switches we made.
		std::cout << "Case #" << cases << ": " << switches <<std::endl;
	}
	return 0;
}

