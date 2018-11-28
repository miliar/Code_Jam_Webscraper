#include <iostream>
#include <map>
#include <string>

using namespace std;



int main(){
	int ntc; cin >> ntc;
	
	for (int tc = 1; tc <= ntc ; tc++) {
		int nse; cin >> nse;
		map<string, int> servers;
		for (int se = 0; se <= nse; se	++) {
			string name; getline(cin, name);
			if (name=="") continue;
		}
		int nq; cin >> nq;
		int nswitches = 0;
		int nserversused = 0;
		for (int q = 0; q <= nq; q++) {
			string query; getline(cin, query);
			if (query=="") continue;
			if (servers[query]==0) nserversused++;
			servers[query]++;
			if (nserversused==nse) {
				nswitches++;
				map<string,int>::iterator iter;   
				for( iter = servers.begin(); iter != servers.end(); iter++ ) {
					servers[iter->first] = 0;
				}
				servers[query] = 1;
				nserversused = 1;
			}
		}
		cout << "Case #" << tc << ": " << nswitches << endl;
	}
	
	
	return 0;
}