#include <iostream>
#include <istream>
#include <ostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <functional>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cstdio>

using namespace std;
/*
///if all the process has been processed, then return this
static const int MATCH_MARK = -1;

int search_last(set<string>& engine_names, vector<string>& search_names, int& index)
{
		
	if(index == search_names.size()){
		return MATCH_MARK;
	}

	deque<string> copy_list(engine_names.begin(), engine_names.end());
	for(; index < search_names.size(); index++)
	{
		set<string>::iterator found_it;
		if(copy_list.size() == 0){
			break;
		}
		
		if(binary_search(engine_names.begin(), engine_names.end(), search_names.at(index)))
		{
			remove_if(copy_list.begin(), copy_list.end(), bind2nd(equal_to<string>(), search_names.at(index)));
		}
	}

	if(copy_list.size() != 0){
		return MATCH_MARK;
	}else{
		return index;
	}
}
*/

vector<string>::iterator search_last(set<string>& engines, vector<string>& names, vector<string>::iterator& cur)
{
	vector<string>::iterator result = cur;
	for(set<string>::iterator temp = engines.begin(); temp != engines.end(); temp++)
	{
		vector<string>::iterator found = find(cur, names.end(), *temp);
		if(found == names.end())
		{
			return names.end();	///found
		}else
		{
			///move the pointer to the last engine
			if(result < found){
				result = found;
			}
		}
	}
	return result;
}

///////////////////////   IO	///////////////////////
///input and output 
static ifstream in("testcase.txt");
static ofstream out("output.txt");
static const int buf_sz = 100;
static char rdbuf[buf_sz];

void read_engine(int num, set<string>& engines)
{
	rdbuf[0] = '\0';	///init 
	for(;num > 0;)
	{
		do{
			in.getline(rdbuf, buf_sz);
		}while(strcmp(rdbuf, "") == 0);
		engines.insert(string(rdbuf));
		num--;
	}
}

void read_name(int num, vector<string>& names)
{
	names.reserve(num);
	rdbuf[0] = '\0';	///init 
	for(;num > 0;)
	{
		do{
			in.getline(rdbuf, buf_sz);
		}while(strcmp(rdbuf, "") == 0);
		names.push_back(string(rdbuf));
		num--;
	}
}

void process_one_case(int case_num)
{
	vector<string> names;
	set<string>	engines;
	int engine_num = 0;
	int name_num = 0;

	in >> engine_num;
	read_engine(engine_num, engines);
	in >> name_num;
	read_name(name_num, names);

	///////begin search
	int count = 0; ///swtich count
	vector<string>::iterator cur = names.begin();
	while((cur = search_last(engines, names, cur)) != names.end())
	{
		count ++;
	}
	out << "Case #" << case_num << ": " << count <<endl;
}


int main(int argc, char** argv)
{
	int case_num;
	in >> case_num;

	for(int i = 1; i <= case_num; i++)
	{
		process_one_case(i);
	}

	return 0;
}