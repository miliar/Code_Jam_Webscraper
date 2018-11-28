#include<iostream>
#include<fstream>
#include<vector>
#include<queue>
#include<string>
#include<set>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstring>
using namespace std;

struct Directory {
	string name;
	vector<Directory*> children;
};

int main()
{
	//ifstream fin("A-tiny.in");
	//ofstream fout("A-tiny.out");
	//ifstream fin("A-small.in");
	//ofstream fout("A-small.out");
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	int ncases;
	fin>>ncases;
	for(int Case = 1; Case<=ncases; Case++){
		fout<<"Case #"<<Case<<": ";

		int n,m;
		fin>>n>>m;
		fin.ignore();
		int count = 0;
		vector<Directory*> dirs;
		Directory *root = new Directory;
		root->name = "/";
		dirs.push_back(root);
		for(int i=0;i<n;i++){
			string line;
			getline(fin, line);
			int start = 1;
			Directory *parent = root;
			int end = line.find_first_of('/',start);
			while(end != string::npos){
				string dir = line.substr(start,end-start);
				int j;
				for(j=0;j<parent->children.size();j++){
					if(parent->children[j]->name == dir){
						break;
					}
				}
				if(j == parent->children.size()){
					Directory *newdir = new Directory;
					newdir->name = dir;
					parent->children.push_back(newdir);
				}
				parent = parent->children[j];
				start = end+1;
				end = line.find_first_of('/',start);
			}
			string dir = line.substr(start,line.length()-start);
			int j;
			for(j=0;j<parent->children.size();j++){
				if(parent->children[j]->name == dir){
					break;
				}
			}
			if(j == parent->children.size()){
				Directory *newdir = new Directory;
				newdir->name = dir;
				parent->children.push_back(newdir);
			}
		}


		for(int i=0;i<m;i++){
			string line;
			getline(fin, line);
			int start = 1;
			Directory *parent = root;
			int end = line.find_first_of('/',start);
			while(end != string::npos){
				string dir = line.substr(start,end-start);
				int j;
				for(j=0;j<parent->children.size();j++){
					if(parent->children[j]->name == dir){
						break;
					}
				}
				if(j == parent->children.size()){
					Directory *newdir = new Directory;
					newdir->name = dir;
					parent->children.push_back(newdir);
					count++;
				}
				parent = parent->children[j];
				start = end+1;
				end = line.find_first_of('/',start);
			}
			string dir = line.substr(start,line.length()-start);
			int j;
			for(j=0;j<parent->children.size();j++){
				if(parent->children[j]->name == dir){
					break;
				}
			}
			if(j == parent->children.size()){
				Directory *newdir = new Directory;
				newdir->name = dir;
				parent->children.push_back(newdir);
				count++;
			}
		}
		fout<<count<<endl;
	}

	return 0;
}