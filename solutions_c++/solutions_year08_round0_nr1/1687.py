#include <iostream>
#include <cstdlib>
#include <fstream>
#include <vector>
using namespace std;

ifstream IN("A-large.in");
ofstream OUT("A-large.out");

vector <string> finders;
vector <string> queries;

int main(){
   int NC;
   IN >> NC;
   
   
   int S,Q;
   for (int cas=1; cas<=NC; cas++){
		string line;
		
		IN >> S;
		getline(IN, line);
		finders.clear();
		for (int i=0; i<S; i++){
			getline(IN, line);
			finders.push_back(line);
		}
		
		IN >> Q;
		getline(IN, line);
		queries.clear();
		for (int i=0; i<Q; i++){
			getline(IN, line);
			queries.push_back(line);
		}
		
		/*
		OUT << "finders:" << endl;
		for (int i=0; i<S; i++){
			OUT << finders[i] << endl;
		}
		OUT << "queries:" << endl;
		for (int i=0; i<Q; i++){
			OUT << queries[i] << endl;
		}
		*/
		int nswitch = 0;
		
		vector <string>::iterator attend = queries.begin();
		
		vector <string> af(finders);
		vector <string>::iterator it;
		while (attend != queries.end()){
			it = find(af.begin(), af.end(), *attend);
			if (it != af.end()) {
				af.erase(it);
			}
			
			if (af.empty()) {
				nswitch++;
				af = finders;
			} else	attend++;
		}
		
		OUT << "Case #" << cas << ": " << nswitch << endl;
	}
}
