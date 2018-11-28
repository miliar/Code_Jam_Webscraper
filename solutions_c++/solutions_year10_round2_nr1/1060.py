#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <fstream>

using namespace std;

class Directory{
public:
	string name;
	int level;
	vector<Directory> subs;

	Directory(string _name,int _level){
		name = _name;
		level = _level;
	}
	int getSubIdx(string _name){
		for(int i = 0 ; i < subs.size() ; i++){
			if(subs[i].name == _name) return i;
		}
		return -1;
	}
	int mkDir(vector<string> _name){
		if(_name.size() == 0) return 0;

		string subDirName = _name[0];
		_name.erase(_name.begin());
		
		int subIdx = getSubIdx(subDirName);
		if(subIdx == -1){
			subs.push_back(Directory(subDirName,level+1));
			return subs[subs.size()-1].mkDir(_name) +1;
		}
		else{
			return subs[subIdx].mkDir(_name);
		}
	}
};

void tokenize(const string& str,vector<string>& tokens,const string& delimiters = " "){
	string::size_type lastPos	= str.find_first_not_of(delimiters,0);
	string::size_type pos		= str.find_first_of(delimiters,lastPos);

	while(string::npos != pos || string::npos != lastPos){
		tokens.push_back(str.substr(lastPos,pos-lastPos));
		lastPos = str.find_first_not_of(delimiters,pos);
		pos		= str.find_first_of(delimiters,lastPos);
	}
}

int main(){

	ifstream ifs;
	ofstream ofs;

	ifs.open("A-large.in");
	ofs.open("A-large.out");

	int T;
	ifs>>T;

	for(int caseN = 1 ; caseN <= T ; caseN++){

		int N,M;
		ifs>>N>>M;

		Directory root("root",0);
		vector<string> dirs;
		for(int i = 0 ; i < N ; i++){
			dirs.clear();
			string dirStr;
			ifs>>dirStr;
			tokenize(dirStr,dirs,"/");
			root.mkDir(dirs);
			//cout<<root.mkDir(dirs)<<endl;
		}
		int result = 0;
		for(int i = 0 ; i < M ; i++){
			dirs.clear();
			string dirStr;
			ifs>>dirStr;
			tokenize(dirStr,dirs,"/");
			result += root.mkDir(dirs);
		}
		ofs<<"Case #"<<caseN<<": "<<result<<endl;
	}

	ifs.close();
	ofs.close();

	return 0;
}