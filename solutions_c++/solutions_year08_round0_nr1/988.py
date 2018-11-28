
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <set>

int Handle(std::map<std::string, int>& e, std::vector<std::string>& q){

	for(std::vector<std::string>::iterator i=q.begin();
		i!=q.end();
		++i)
	{
		e[*i]++;
	}

	// sort now

	std::multimap<int, std::string > byW;
	for(std::map<std::string, int>::iterator i=e.begin();
		i!=e.end();
		++i)
	{
		if(i->second==0){
			return 0;			// exists search engine not in Q-list
		}
		byW.insert( make_pair(i->second, i->first) );
	}

	int sw=0;
	std::set<std::string> current;

	// current seen
	for(int i=0; i<q.size(); i++){
		std::cerr<<" query [ "<<q[i]<<" ]"<<std::endl;

		if( current.find(q[i])==current.end()){
			current.insert(q[i]);
			if(current.size()==e.size()){
				sw++;
				std::cerr<<"switch to [ "<<q[i]<<"]"<<std::endl;

				current.clear();
				current.insert(q[i]);
			}
		}
	}



	return sw;

}

int main(void){

	//const std::string fname="in1";
	//const std::string fname="A-small-attempt1.in";
	//const std::string fname="A-small-attempt2.in";
	const std::string fname="A-large.in";
	std::ifstream rd;
	rd.open(fname.c_str());

	int task_count=0;
	rd>>task_count;
	std::cerr<<"task count "<<task_count<<std::endl;

	for(int cur_task=0; cur_task<task_count; cur_task++){

		int e_count=0;
		rd >> e_count;
		std::cerr<<"e count "<<e_count<<std::endl;

		std::map<std::string, int> engines;

		for(int i=0; i<e_count; ){
			std::string tmp;
			std::getline(rd, tmp);
			if(tmp.length()){
				std::cerr<<"engine added ["<<tmp<<"]"<<std::endl;
				engines.insert( std::make_pair(tmp, 0) );
				i++;
			}
		}

		int q_count=0;
		rd>>q_count;
		std::cerr<<"q count "<<q_count<<std::endl;

		std::vector<std::string> queries;

		std::string last_q;
		for(int i=0; i<q_count; ){
			std::string tmp;
			std::getline(rd, tmp);
			if(tmp.length()){
				if(last_q != tmp ){
					queries.push_back( tmp );
				}
				last_q=tmp;
				i++;
			}
		}

		std::cerr<<"Case #"<<cur_task+1<<": "<<Handle(engines,queries)<<std::endl;

	}

	return 0;

}




