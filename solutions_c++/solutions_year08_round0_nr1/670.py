#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef vector< string > vecstring;

int calculate_distance(vecstring queries, string engine, int index)
{
	for(int i = index + 1; i < (int) queries.size(); i++) {
		if(queries.at(i) == engine) {
			return i - index;
		}
	}

	return 0;
}

string max_distance(vecstring engines, vecstring queries, int index)
{
	int max = calculate_distance(queries, engines.at(0), index);
	string max_engine = engines.at(0);
	if(max == 0) {
		return max_engine;
	}

	for(int i = 1; i < (int) engines.size(); i++) {
		int distance = calculate_distance(
				queries,
				engines.at(i),
				index
				);

		if(distance == 0) {
			max_engine = engines.at(i);
			return max_engine;
		}

		if(distance > max) {
			max = distance;
			max_engine = engines.at(i);
		}
	}

	return max_engine;
}

int calculate_steps(vecstring engines, vecstring queries, string first)
{
	string current = first;

	int count = 0;
	for(int i = 0; i < (int) queries.size(); i++) {
		if(queries.at(i) == current) {
			vecstring copy = engines;
			vecstring::iterator p;
			while((p = find(copy.begin(), copy.end(), current))
					!= copy.end()) {
				copy.erase(p);
			}
			current = max_distance(
					copy,
					queries,
					i);
			count++;
		}
	}

	return count;
}

int min_steps(vecstring engines, vecstring queries)
{
	int min = calculate_steps(engines, queries, engines.at(0));

	for(int i = 1; i < (int) engines.size(); i++) {
		int steps = calculate_steps(
				engines,
				queries,
				engines.at(i)
				);
		if(steps < min) {
			min = steps;
		}
	}

	return min;
}

int main(int argc, char *argv[])
{
	int ncases;
	string dummy;
	cin>>ncases;
	getline(cin, dummy);

	for(int i = 0; i < ncases; i++) {
		string str;

		vecstring engines;
		int nengines;
		cin>>nengines;
		getline(cin, str);
		for(int j = 0; j < nengines; j++) {
			getline(cin, str);
			engines.push_back(str);
		}

		vecstring queries;
		int nqueries;
		cin>>nqueries;
		getline(cin, str);
		for(int j = 0; j < nqueries; j++) {
			getline(cin, str);
			queries.push_back(str);
		}

		int min = min_steps(engines, queries);
		cout<<"Case #"<<i + 1<<": "<<min<<endl;
	}

	return 0;
}

