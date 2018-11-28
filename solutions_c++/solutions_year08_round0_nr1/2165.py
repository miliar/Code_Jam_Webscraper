#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>

using namespace std;

int main()
{
	ifstream ifs = ifstream("A-large.in");
	ofstream ofs = ofstream("out.txt");
	char buf[110];
	int cases;
	ifs >> cases;
	for(int c = 1; c <= cases; ++c){
		int numName, numQueries, switches=0;
		ifs >> numName;
		ifs.getline(buf,110);//read newline
		vector<string> names;
		vector<string> queries;
		set<string> s;
		for(int i = 0; i < numName; ++i){
			ifs.getline(buf, 110);
			string s(buf);
			names.push_back(s);
		}
		ifs >> numQueries;
		ifs.getline(buf,110);//read newline
		for(int i = 0; i < numQueries; ++i){
			ifs.getline(buf, 110);
			string s(buf);
			queries.push_back(s);
		}
		for(int i = 0; i < numQueries; ++i){
			if(s.find(queries[i]) == s.end()){//not already in map
				s.insert(queries[i]);
				if(s.size() == numName){
					switches++;
					s.clear();
					s.insert(queries[i]);
				}
			}
		}
		ofs << "Case #" << c << ": " << switches << endl;
	}
	ifs.close();
	ofs.close();	
	return 0;
}