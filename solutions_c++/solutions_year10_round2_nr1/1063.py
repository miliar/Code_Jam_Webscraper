#include <string>
#include <fstream>
#include <hash_map>
#include <sstream>
#include <vector>
using namespace std;
using namespace stdext;

struct dir{
	hash_map<string, dir> sub;
};

int main(){
	ofstream ofs("out.txt");
	ifstream ifs("in.txt");
	int cas = 1;
	int t;
	ifs>>t;
	while(t--){
		int n,m;
		ifs>>n>>m;
		dir root;
		int dirp = 0;
		for(int i = 0; i != n; ++i){
			string path;
			ifs>>path;
			if(path[path.size()-1] != '/')
				path.push_back('/');
			dir* r = &root;
			int pos = 1;
			int beg = 1;
			vector<int> p;
			while(pos != path.size()){
				if(path[pos] == '/'){
					string str = path.substr(beg, pos- beg);
					if(!r->sub.count(str)){
						r->sub[str];
					}
					beg = pos + 1;
					r = &(r->sub[str]);	
				}
				++pos;
			}
		}

		int coun = 0;
		for(int i = 0; i != m; ++i){
			string path;
			ifs>>path;
			if(path[path.size()-1] != '/')
				path.push_back('/');
			dir* r = &root;
			int pos = 1;
			int beg = 1;
			vector<int> p;
			while(pos != path.size()){
				if(path[pos] == '/'){
					string str = path.substr(beg, pos - beg);
					if(!r->sub.count(str)){
						++coun;
						r->sub[str];
					}
					beg = pos + 1;
					r = &(r->sub[str]);	
				}
				++pos;
			}
		}
		ofs<<"Case #"<<cas++<<": "<<coun<<endl;
		
	}
	return 0;
}
