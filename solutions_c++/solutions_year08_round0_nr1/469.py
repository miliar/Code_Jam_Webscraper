#include "iostream"
#include "sstream"
#include "fstream"
#include "vector"
#include "algorithm"

using namespace std;

ifstream in("A-large.in");
ofstream out("out.txt");

int main(){
	int N = 0;
	in >> N;
	for(int i = 0; i < N; i++){
		int S = 0;
		in >> S;
		vector<string> names;
		vector<vector<int> > used;
		in.get();
		for(int i = 0; i < S; i++){
			string temp;
			getline(in, temp, '\n');
			names.push_back(temp);
			used.push_back(vector<int>());
		}
		int Q = 0;
		in >> Q;
		in.get();
		for(int i = 0; i < Q; i++){
			string temp;
			getline(in, temp, '\n');
			int tmp = find(names.begin(), names.end(), temp)-names.begin();
			used.at(tmp).push_back(i);
		}
		//Processing

		int result = 0;
		for(size_t i = 0; i < used.size(); i++){
			if(used.at(i).empty()){
				used.clear();
				break;
			}
		}
		int last = -1;
		while(used.size() == S){
			result++;
			int mx = 0;
			for(size_t i = 0; i < used.size(); i++){
				if(i == last)
					continue;
				if(used.at(i).at(0) > mx){
					last = i;
					mx = used.at(i).at(0);
				}
			}
			for(size_t i = 0; i < used.size(); i++){
				for(size_t k = 0; k < used.at(i).size(); k++){
					if(used.at(i).at(k) >= mx){
						used.at(i).erase(used.at(i).begin(), used.at(i).begin()+k);
						break;
					}
					if(k == used.at(i).size()-1)
						used.at(i).clear();
				}
				if(used.at(i).empty()){
					used.erase(used.begin()+(i--));
					break;
				}
			}
		}
		out << "Case #" << i+1 << ": " << result << endl; 
	}
}