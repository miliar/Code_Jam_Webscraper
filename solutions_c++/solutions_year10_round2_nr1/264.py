#include<iostream>
#include<map>

using namespace std;

class filesystem {
	map<string, filesystem*> dirs;
	public:

	filesystem(): dirs(){}
	int mkdir(string str){
		str = str.substr(1);
		int k = str.find_first_of('/');
		string name = str.substr(0, k);
		map<string, filesystem*>::iterator it;
		if((it = dirs.find(name)) != dirs.end()){
			if(k >= str.length()) return 0;
			return it->second->mkdir(str.substr(k));
		}

		filesystem* ptr = dirs[name] = new filesystem;
		if(k >= str.length()) return 1;
		return 1 + ptr->mkdir(str.substr(k));
	}
	~filesystem(){
		for(map<string, filesystem*>::iterator it = dirs.begin(); it != dirs.end(); ++it){
			delete it->second;
		}
	}
};

int main(){
	int csn;

	cin >> csn;
	for(int cs = 1; cs <= csn; ++cs){
		int m, n;
		int k  = 0;
		filesystem fs;
		string str;

		cin >> m >> n;

		for(int i = 0; i < m; ++i){
			cin >> str;
			fs.mkdir(str);
		}

		for(int i = 0; i < n; ++i){
			cin >> str;
			k += fs.mkdir(str);
		}

		cout << "Case #" << cs << ": " << k << endl;
	}

	return 0;
}
