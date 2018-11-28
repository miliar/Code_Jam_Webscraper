#include <iostream>
#include <fstream>
#include <string>
#include <map>

#define MAX_BUFF 200

using namespace std;

class CSearchEngines
{
private:
	map<string,int> engines;
public:
	void add( const char* eng_name ) { engines.insert(pair<string,int>(eng_name,0)); }
	void mark_visited( const char* eng_name ) { engines[eng_name] = 1; }
	void reset() {
		map<string,int>::iterator iter = engines.begin();
		for(; iter != engines.end(); ++iter ) {
			iter->second = 0;
		}
	}
	void clear() { engines.clear(); }
	bool isSwitchReqd() {
		map<string,int>::iterator iter = engines.begin();
		for(; iter != engines.end(); ++iter ) {
			if( iter->second == 0 ) {
				return false;
			}
		}
		return true;
	}
};

int main()
{
	ifstream in;
	ofstream out;
	in.open("in.txt",ios::in);
	out.open("out.txt",ios::out);
	int iterations = 0;
	int engines = 0;
	int queries = 0;
	int nSwitches = 0;
	char buffer[MAX_BUFF];
	CSearchEngines visited_eng;
	in >> iterations >> ws;
	for( int ite=1; ite <= iterations ; ite++ ) {
		nSwitches = 0;
		visited_eng.clear();
		in >> engines >> ws;
		for( int j=1; j <= engines ; j++ ) {
			in.getline(buffer,MAX_BUFF);
			visited_eng.add(buffer);
		}
		in >> queries >> ws;
		for( int j=1; j <= queries ; j++ ) {
			in.getline(buffer,MAX_BUFF);
			visited_eng.mark_visited(buffer);
			if( visited_eng.isSwitchReqd() ) {
				visited_eng.reset();
				visited_eng.mark_visited(buffer);
				++nSwitches;
			}
		}
		out << "Case #" << ite << ": " << nSwitches << endl;
	}
	in.close();
	out.close();
	return 0;
}