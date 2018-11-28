/*
# Text File
# AUTHOR:   gautam
# FILE:     /home/gautam/try/codejam/prog1.cpp
# CREATED:  17:04:57 16/07/2008
# MODIFIED: 17:04:57 16/07/2008
*/
#include <stdio.h>
#include <unistd.h>

#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

#define MAX_N 2
#define MAX_S 3
#define MAX_SIZE 100

class enginet{
public:
	string name;
	int pos;
	int find_next_after(vector<string> qlist, int spos){
		for(int i=spos;i<qlist.size();i++)
			if(name==qlist[i])
				return i;
		return -1;
	}

	enginet(string str){
		name=str;
		pos=0;
	}
};


int main(int argc, char *argv[]){
	unsigned int num=0;
	size_t bytes_read=0;
	char a;
	
	string t_num;
	getline(cin, t_num);
	istringstream ss1(t_num);
	ss1>>num;
#ifdef TRACE
	cout<<"number of cases: "<<num<<endl;
#endif

	for(int t_case=0;t_case<num;t_case++){
		int num_engines;
		string t_num_e;
		getline(cin, t_num_e);
		istringstream ss2(t_num_e);
		ss2>>num_engines;
#ifdef TRACE
		cout<<"Number of engines = "<<num_engines<<endl;
#endif
		vector<enginet> engines;
		for(int i=0;i<num_engines;i++){
			char t_buff[MAX_SIZE+1];
			string t_str;
			getline(cin, t_str);
			enginet t_eng(t_str);
			engines.push_back(t_eng);
#ifdef TRACE
			cout<<"Added engine : "<<t_str<<endl;
#endif
		}
		
		int num_queries;
		string t_num_q;
		getline(cin, t_num_q);
		istringstream ss3(t_num_q);
		ss3>>num_queries;

#ifdef TRACE
		cout<<"Number of queries= "<<num_queries<<endl;
#endif
		vector<string> queries;
		for(int i=0;i<num_queries;i++){
			char t_buff[MAX_SIZE+1];
			string t_str;
			getline(cin, t_str);
			queries.push_back(t_str);
#ifdef TRACE
			cout<<"Added query: "<<t_str<<endl;
#endif
		}


		//queries now holds the list of queries
		//nd engines the list of engines.input file is not
		//checked for any errors
		//
		//
		int start_pos=0, n_switch=0;
		int max=0;

		if(engines.size()==1 && engines[0].find_next_after(queries, 0)!=-1){
			cout<<"case #"<< t_case<< " can't be processed"<<endl;
			continue;
		}
		if(queries.size()==0){
			cout<< "Case #"<<t_case+1<<": "<<n_switch<<endl;
			continue;
		}
			
		
		while(start_pos<=(queries.size()-1)){
			max=0;
			for(int i=0;i<engines.size();i++){
				int here = engines[i].find_next_after(queries, start_pos);
				//cout << "Here = "<<here<<"i = "<<i<<endl;
				//We stop, after we see an engine not present in the sub query list
				if(here==-1){
					n_switch+=1;
					max = queries.size();
					break;
				}
				else if(here>max)
					max=here;
			}
			start_pos=max;
			n_switch+=1;
		}

		n_switch-=2;

		cout<< "Case #"<<t_case+1<<": "<<n_switch<<endl;
	}
	return 0;
}
