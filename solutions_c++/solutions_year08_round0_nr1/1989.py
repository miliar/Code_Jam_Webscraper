#include <vector>
#include <fstream>
#include <string>
#include <iostream>

using namespace std;

typedef vector<string> VI;

bool Contain(VI & vec, string & str){
	int size = vec.size();
	if (size == 0) return false;
	for (int i = 0; i < size; i++){
		if (str.compare(vec[i]) == 0) return true; 
	}

	return false;
}

int Solve(VI & s_p, VI & qu){
	int num_sp = s_p.size();
	int num_qu = qu.size();

	VI past(0);
	past.clear();

	int result = 0;
	for (int j = 0; j < num_qu; j++){
		if (Contain(past, qu[j])){
			

		} else {
			if ( past.size() == num_sp - 1) {
				result++;
				past.clear();
				//outfile << "clear" << endl;
			}
			past.push_back(qu[j]);
			//outfile << "push" << qu[j] << endl;
			

		}	
	}
	return result;
}



int main(){
	int n = 1;
	int m;
	ifstream file;
	ofstream outfile;
	file.open("../a-large.in");
	
	
	outfile.open("../a-large.out");

	file >> m;

	VI search_prov;
	VI queries;
	int k, l;

	char temp[256];
	while (n <= m){
		search_prov.clear();
		queries.clear();
		 
		file >> k;  // num_searc_provider
		//outfile << k << endl;
        file.getline(temp, 256);

		search_prov.resize(k);
		for(int i = 0; i < k; i++){
			file.getline(temp, 256);		
			search_prov[i] = temp;
			//outfile << i << search_prov[i] << endl;
		}

		file >> l;  //num_queries
		file.getline(temp, 256);
		queries.resize(l);
		for(int i = 0; i < l; i++){
			file.getline(temp, 256);
			queries[i] = temp;
			//outfile << i << queries[i] << endl;
		}

		outfile << "Case #" << n << ": " << Solve(search_prov, queries) << endl;
    
		n++;
	}

	file.close();
	outfile.close();

	return 0;

}