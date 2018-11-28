#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>

using namespace std;

class Directory{
	public:
		string name;
		vector<Directory> child;
};


string getFirstDir(string s){
	stringstream firstDir;
	for (int i = 1; i < s.size(); i++){
		if (s[i] == '/'){
			return firstDir.str();
		}
		firstDir << s[i];
	}
	return firstDir.str();
}

string getRemaining(string s){
	stringstream remaining;
	for (int i = 1; i < s.size(); i++){
		if (s[i] == '/'){
			for (int j = i; j < s.size(); j++){
				remaining << s[j];
			}
			return remaining.str();
		}
	}
	return "";
}

int add(Directory &d, string &path){
	int created = 0;
	Directory *currentDir = &d;
	string remaining = path;
	string first;
	while(remaining.size()){
		first = getFirstDir(remaining);
		remaining = getRemaining(remaining);
		bool found = false;
		for (int i = 0; i < currentDir->child.size(); i++){
			if (currentDir->child[i].name == first){
				found = true;
				currentDir = &currentDir->child[i];
				break;
			}
		}
		if (!found){
			created++;
			Directory newD;
			newD.name = first;
			currentDir->child.push_back(newD);
			currentDir = &currentDir->child[currentDir->child.size()-1];
		}
	}
	return created;
}
int main(int argc, char *argv[]){
	if (argc != 2){
		cerr << "Error: " << argv[0] << " file" << endl;
		exit(-1);
	}
	ifstream file(argv[1]);
	if (!file.is_open()){
		cerr << "Error: file " << argv[0] << " could not be opened" << endl;
	}
	
	int T;
	file >> T;
	for (int i = 0; i < T; i++){
		int N, M;
		file >> N >> M;
		Directory root;
		for (int j = 0; j < N; j++){
			string directory;
			file >> directory;
			add(root, directory);
		}
		long creations = 0;
		for (int j = 0; j < M; j++){
			string directory;
			file >> directory;
			creations += add(root, directory);
		}
		cout << "Case #" << (i+1) << ": " << creations << endl;
	}


	file.close();
}
