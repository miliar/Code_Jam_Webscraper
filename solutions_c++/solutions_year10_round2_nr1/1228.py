#include <fstream>
#include <iostream>
#include <windows.h>
#include <time.h>
#include <string>
#include <vector>
using namespace std;
struct file{
	std::string name;
	std::vector<file*> children;
};

int addFile(std::string path,file* topfile){
	unsigned int a = 0;
	int ret = 0;
	file* dir = topfile;
	if(path.size() < 2) return 0;
	while(a != std::string::npos){
		unsigned int b = path.find("/",a+1);
		std::string fname;
		if(b != std::string::npos){
			fname = path.substr(a+1,(b-a)-1);
		}else{
			fname = path.substr(a+1);
		}
		a = b;
		bool found = true;
		for(int i = 0;i < dir->children.size();i++){
			if(dir->children[i]->name == fname){
				dir = dir->children[i];
				found = false;
				break;
			}
		}
		if(found){
			ret++;
			file* n = new file();
			n->name = fname;
			dir->children.push_back(n);
			dir = n;
		}
	}
	return ret;
}
int main(){
	string inname;
	string outname;
	cout << "Enter file name to read: ";
	getline(cin,inname);
	cout << "\nEnter file name to save: ";
	getline(cin,outname);
	ifstream in(inname.data());
	ofstream out(outname.data(),ios::trunc);
	bool good = true;
	if(!in.is_open()){
		good = false;
		cout << "Could not open file " << inname << " for reading";
	}
	if(!out.is_open()){
		good = false;
		cout << "Could not open file " << outname << " for reading";
	}
	if(!good)
		Sleep(10000);
	clock_t st = clock();
	long cases = 0;
	in >> cases;
	for(long casen = 1;casen <= cases;casen++){
		int exist,create;
		int answer = 0;
		file* topfile = new file();
		in >> exist;
		in >> create;
		std::string read;
		std::getline(in,read);
		for(int i = 0;i < exist;i++){
			std::getline(in,read);
			addFile(read,topfile);
		}
		for(int i = 0;i < create;i++){
			std::getline(in,read);
			answer += addFile(read,topfile);
		}
		std::cout << "Completed " << casen << "\n";
		out << "Case #" << casen << ": " << answer << "\n";
	}
	in.close();
	out.close();
	clock_t en = clock();
	cout << "Time: " << ((en-st)/CLOCKS_PER_SEC);
	Sleep(1000000000);
}