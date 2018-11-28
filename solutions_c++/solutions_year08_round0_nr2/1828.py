/*
 *  Trains.c
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


struct time_table_entry{
	unsigned int departure:12;
	unsigned int arrival:12;
	bool direction; //True = From A to B; False otherwise
	bool served;
	bool may_covered; //Other node can reach it
	vector<time_table_entry *> candidates; //Candidates for departure
	time_table_entry(unsigned int d, unsigned int a, bool dir){
		departure = d;
		arrival = a;
		direction = dir;
		served = false;
		may_covered = false;
	}
	void add_candidate(time_table_entry *cand){
		candidates.push_back(cand);
	}
};
typedef struct time_table_entry tte;

//The time table
vector<tte> time_table_A;
vector<tte> time_table_B;
unsigned int hold_up = 0;
unsigned int number_of_trains_in_A = 0;
unsigned int number_of_trains_in_B = 0;


bool by_departure(tte s1, tte s2){ return (s1.departure < s2.departure);}
bool by_arrival(tte s1, tte s2){ return (s1.arrival < s2.arrival);}

void find_candidates(){
	sort(time_table_A.begin(), time_table_A.end(), by_arrival);
	sort(time_table_B.begin(), time_table_B.end(), by_departure);
	vector<tte>::iterator tt_a_it = time_table_A.begin();
	vector<tte>::iterator tt_b_it;// = time_table_B.begin();
	//bool early = true;
	//We find the candidates of departures from A to B
	for(;tt_a_it < time_table_A.end(); tt_a_it++){
		for(tt_b_it = time_table_B.begin(); tt_b_it < time_table_B.end(); tt_b_it++){
			if((*tt_a_it).arrival + hold_up <= (*tt_b_it).departure){
				(*tt_a_it).add_candidate(&(*tt_b_it));
				(*tt_b_it).may_covered = true;
				//early = false;
			}
			//if(early)
			//	break;
			//early = true;
		}
	}
	//We find the candidates of departures from B to A
	sort(time_table_B.begin(), time_table_B.end(), by_arrival);
	sort(time_table_A.begin(), time_table_A.end(), by_departure);
	//early = true;
	for(tt_b_it = time_table_B.begin(); tt_b_it < time_table_B.end(); tt_b_it++){
		for(tt_a_it = time_table_A.begin();tt_a_it < time_table_A.end(); tt_a_it++){
			if((*tt_b_it).arrival + hold_up <= (*tt_a_it).departure){
				(*tt_b_it).add_candidate(&(*tt_a_it));
				(*tt_a_it).may_covered = true;
				//early = false;
			}
			//if(early)
			//	break;
			//early = true;
		}
	}
}


//vector<tte *> longest_route;

vector<tte *> find_longest_route(tte *hop_it){
	size_t num_hops = 0;
	vector <tte *> hops;
	if(hop_it -> served){
		return hops;
	}
	vector<tte *>::iterator candidates_it = (*hop_it).candidates.begin();
	for(;candidates_it < (*hop_it).candidates.end(); candidates_it++){
		if((*candidates_it) -> served)
			continue;
		vector <tte *> candidates = find_longest_route(*candidates_it);
		if(candidates.size() > hops.size() && !hops.empty()){
			hops = candidates;
			num_hops = candidates.size();
			//hops.push_back(*candidates_it);
		}
		else if(hops.empty()){
			hops = candidates;
		}
	
	}
	hops.push_back(hop_it);
	return hops;
}

vector<tte>::iterator find_root_node(){
	vector<tte>::iterator candidate = time_table_A.end();
	vector<tte>::iterator tt_it = time_table_A.begin();
	for(; tt_it < time_table_A.end(); tt_it++){
		if(candidate != time_table_A.end() && !(*tt_it).served && !(*tt_it).may_covered && 
			!(*tt_it).candidates.empty() && (*tt_it).departure < (*candidate).departure ){
				candidate = tt_it;
		}
		if(candidate == time_table_A.end() && !(*tt_it).served && !(*tt_it).may_covered && !(*tt_it).candidates.empty()){
				candidate = tt_it;
		}
	}
	for(tt_it = time_table_B.begin(); tt_it < time_table_B.end(); tt_it++){
		if(candidate != time_table_A.end() && !(*tt_it).served && !(*tt_it).may_covered && 
			!(*tt_it).candidates.empty() && (*tt_it).departure < (*candidate).departure ){
				candidate = tt_it;
		}
		if(candidate == time_table_A.end() && !(*tt_it).served && !(*tt_it).may_covered && !(*tt_it).candidates.empty()){
				candidate = tt_it;
		}
	}
	return candidate;
}


void solve(){
	sort(time_table_A.begin(), time_table_A.end(), by_departure);
	sort(time_table_B.begin(), time_table_B.end(), by_departure);
	find_candidates();
	vector<tte>::iterator root_node = time_table_A.begin();
	while(1){
		vector<tte *> longest_route;
		//vector<tte>::iterator root_node = time_table_A.begin();
		for(root_node = time_table_A.begin(); root_node < time_table_A.end(); root_node++){
			vector<tte *> route = find_longest_route(&*root_node);
			if(route.size() > longest_route.size() && !longest_route.empty())
				longest_route = route;
			else if(longest_route.empty())
				longest_route = route;
		}
		for(root_node = time_table_B.begin(); root_node < time_table_B.end(); root_node++){
			vector<tte *> route = find_longest_route(&*root_node);
			if(route.size() > longest_route.size() && !longest_route.empty())
				longest_route = route;
			else if(longest_route.empty())
				longest_route = route;
		}
		if(longest_route.empty())
			break;
		vector<tte *>::iterator route_it = longest_route.begin();
		for(; route_it < longest_route.end(); route_it++){
				//cout <<  (*route_it) -> departure << " " << (*route_it) -> arrival << "\n";
				(*route_it) -> served = true;
			}
		if((*(longest_route.end() - 1)) -> direction)
			number_of_trains_in_A++;
		else
			number_of_trains_in_B++;
	}
	/*
	vector<tte>::iterator root_node = find_root_node();
	while(root_node != time_table_A.end()){
		vector<tte *> route = find_longest_route(&*root_node);
		//We mark the found nodes as served
		vector<tte *>::iterator route_it = route.begin();
		//cout << "ROUTE OF:  " << (*root_node).departure << " " << (*root_node).arrival << "\n";
		for(; route_it < route.end(); route_it++){
			//cout <<  (*route_it) -> departure << " " << (*route_it) -> arrival << "\n";
			(*route_it) -> served = true;
		}
		if((*root_node).direction)
			number_of_trains_in_A++;
		else
			number_of_trains_in_B++;
		root_node = find_root_node();
	}*/
	//Once that we finished with the possible multiple routes... 
	//We just add the number of trains remaining per each station
	for(root_node = time_table_A.begin(); root_node < time_table_A.end(); root_node++){
		if(!(*root_node).served)
			number_of_trains_in_A++;
	}
	for(root_node = time_table_B.begin(); root_node < time_table_B.end(); root_node++){
		if(!(*root_node).served)
			number_of_trains_in_B++;
	}
}


//---------------------------------------------------------- READING ----------------------------------------------------------//

void set_up(vector<string> A_time_table, vector<string> B_time_table){
	vector<string>::iterator time_table_it = A_time_table.begin();
	for(;time_table_it < A_time_table.end(); time_table_it++){
		string departure, arrival;
		departure = (*time_table_it).substr(0,5);
		arrival = (*time_table_it).substr(6,10);
		departure.erase(2,1);
		arrival.erase(2,1);
		unsigned int dep, arriv;
		stringstream(departure) >> dep;
		stringstream(arrival) >> arriv;
		time_table_A.push_back( tte(dep,arriv,true) );
	}
	for(time_table_it = B_time_table.begin();time_table_it < B_time_table.end(); time_table_it++){
		string departure, arrival;
		departure = (*time_table_it).substr(0,5);
		arrival = (*time_table_it).substr(6,10);
		departure.erase(2,1);
		arrival.erase(2,1);
		unsigned int dep, arriv;
		stringstream(departure) >> dep;
		stringstream(arrival) >> arriv;
		time_table_B.push_back( tte(dep,arriv,false) );
	}
}

void read_and_set_up(ifstream *test_cases_file){
	string tmp;
	vector<string> A_time_table;
	vector<string> B_time_table;
	unsigned int a_entrances;
	unsigned int b_entrances;
	getline(*test_cases_file, tmp);
	stringstream(tmp) >> hold_up;
	getline(*test_cases_file, tmp);
	string num_a, num_b;
	size_t white = tmp.find(" ");
	num_a = tmp.substr(0, white);
	num_b = tmp.substr(white+1, tmp.size());
	stringstream(num_a) >> a_entrances;
	stringstream(num_b) >> b_entrances;
	unsigned int index = 0;
	for(;index < a_entrances; index++){
		getline(*test_cases_file, tmp);
		A_time_table.push_back(tmp);
	}
	for(index = 0; index < b_entrances; index++){
		getline(*test_cases_file, tmp);
		B_time_table.push_back(tmp);
	}
	set_up(A_time_table, B_time_table);
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
		solve();
		cout << "Case #" << index + 1 << ": " << number_of_trains_in_A << " " << number_of_trains_in_B << "\n";
		number_of_trains_in_A = 0;
		number_of_trains_in_B = 0;
		hold_up = 0;
		time_table_A.clear();
		time_table_B.clear();
	}
	test_cases_file.close();
	return 0;
}


