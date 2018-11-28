/*
 *  Saving_The_Universe.c
 *  Google-CodeJam
 *
 *  Created by Odiseo on 7/16/08.
 *  Copyright 2008 __MyCompanyName__. All rights reserved.
 *
 */
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <fstream>
using namespace std;


struct search_engine_switch{
	unsigned int served:11;
	unsigned char server_code;
	bool switched;
	string server_name;
	search_engine_switch(string sn, unsigned char sc){
		server_name = sn;
		server_code = sc;
		switched = false;
		served = 0;
	}
	void set_switched(){
		switched = true;
	}
	bool is_switched(){
		return switched;
	}
	bool matches_query(unsigned char query_code){
		return (query_code == server_code);
	}
	void clean(){
		switched = false;
		served = 0;
	}
	bool increase_served(){
		if(!switched)
			served++;
		return !switched;
	}
	unsigned char get_served(){
		return (unsigned char) served;
	}
	unsigned char get_code(){
		return server_code;
	}
	bool operator==(const search_engine_switch& serv2){
		return (server_code == serv2.server_code);
	}
	bool operator<(const search_engine_switch& serv2){
		return (server_code < serv2.server_code);
	}
};

typedef struct search_engine_switch se;

vector<se>servers;
vector<unsigned short>queries;
vector<unsigned short>::iterator queries_it;

//Sets up the vectors of servers and queries
void set_up(vector<string> ser, vector<string> quer){
	vector<string>::iterator ser_it = ser.begin();
	vector<string>::iterator quer_it = quer.begin();
	unsigned char server_code = 0;
	for(;ser_it < ser.end(); ser_it++){
		servers.push_back(se(*ser_it, server_code++));
	}
	//Now the queries
	for(;quer_it < quer.end(); quer_it++){
		vector<se>::iterator servers_it = servers.begin();
		for(;servers_it < servers.end(); servers_it++){
			if( (*servers_it).server_name == *quer_it )
				queries.push_back((*servers_it).get_code());
		}
	}
	queries_it = queries.begin();
}

bool update_servers(unsigned char not_usable_code){
	vector<se>::iterator found_it = find(servers.begin(), servers.end(), se(" ", not_usable_code));
	(*found_it).set_switched();
	vector<se>::iterator servers_it = servers.begin();
	bool updated = false;
	for(;servers_it < found_it; servers_it++)
		if((*servers_it).increase_served())
			updated = true;
	for(servers_it = found_it + 1; servers_it < servers.end(); servers_it++)
		if((*servers_it).increase_served())
			updated = true;
	return updated;

}

void clean_servers(){
	vector<se>::iterator servers_it = servers.begin();
	for(;servers_it < servers.end(); servers_it++){
		(*servers_it).clean();
	}
}


//Finds the next optimal hop
bool get_next_switch(){
	for(; queries_it < queries.end(); queries_it++){
		if(!update_servers(*queries_it)){
			clean_servers();
			return true;
		}
	}
	clean_servers();
	return false;
}


unsigned int solve(){
	int switches = 0;
	while(get_next_switch()){
		switches++;
	}
	return (unsigned int) switches;
}



void read_and_set_up(ifstream *test_cases_file){
	int num_of_servers;
	int num_of_queries;
	int index;
	string tmp;
	vector<string> servers_names;
	vector<string> orig_queries;
	getline(*test_cases_file,tmp);
	stringstream(tmp) >> num_of_servers;
	for(index = 0; index < num_of_servers; index++){
		string server;
		getline(*test_cases_file, server);
		//cout << "S:  " << server << "\n";
		servers_names.push_back(server);
	}
	getline(*test_cases_file,tmp);
	stringstream(tmp) >> num_of_queries;
	for(index = 0; index < num_of_queries; index++){
		string query;
		getline(*test_cases_file,query);
		//cout << "Q:  " << query << "\n";
		orig_queries.push_back(query);
	}
	set_up(servers_names, orig_queries);
}


int main (int argc, char * const argv[]) {
	ifstream test_cases_file;
	test_cases_file.open(argv[1]);
	int test_cases;
	int index;
	string tsn;
	getline(test_cases_file,tsn);
	stringstream(tsn) >> test_cases;
	for(index = 0; index < test_cases; index++){
		read_and_set_up(&test_cases_file);
		unsigned int switches;
		switches = solve();
		cout << "Case #" << index + 1 << ": " << switches << "\n";
		servers.clear();
		queries.clear();
	}
	test_cases_file.close();
}


