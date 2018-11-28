#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;

int T;
string G;

char translate[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(){
	ifstream in("A-small-attempt0.in");
	ofstream out("A-small-attempt0.out");
	
	in >> T;
	
	string tmp;
	getline(in, tmp);
	
	for(int i = 1; i <= T; ++i){
		string result = "";
		getline(in, G);
		for(unsigned j = 0; j < G.size(); ++j){
			if(G[j] >= 'a' && G[j] <= 'z')
				result += translate[G[j] - 'a'];
			else
				result += G[j];
		}
		
		out << "Case #" << i << ": " << result << endl;
	}
	return 0;
}
