#include <iostream>
#include <string>
#include <vector>

using namespace std;
bool contains(vector<string>container, string target);
int main(){
	int T = 0;
	int N = 0;
	int M = 0;
	

	cin >> T;
	for(int i = 0; i < T; i++){
		cin >> N;
		cin >> M;
		vector<string> map ;
		for(int j = 0; j <N; j++){
			string path;
			cin >> path;
			int current = 1;
			while(path.find("/", current) != string::npos){
				current = path.find_first_of("/", current);
				string pt = path.substr(0, current);
				map.push_back(pt);
				current ++;
			}
			map.push_back(path);
		}
		int steps = 0;
		for(int j = 0; j < M; j++){
			string path;
			cin >> path;
			int current = 1;
			while(path.find("/", current) != string::npos){
				current = path.find_first_of("/", current);
				string pt = path.substr(0, current);
				if(!contains(map, pt)){
					map.push_back(pt);
					steps++;
				}
				current++;
			}
			if(!contains(map, path)){
				map.push_back(path);
				steps++;
			}
		}
		cout << "Case #" << i+1 << ": " << steps << endl;
	}
	return 0;
}

bool contains(vector<string>container, string target){
	for(int i = 0; i < container.size(); i++){
		if(container[i] == target){
			return true;	
		}
	}
	return false;
}