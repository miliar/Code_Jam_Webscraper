#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

struct dir{
	string name;
	vector< dir* > child;
};

dir* root;
int mks;

void mkdir(dir* f, string path){
	if(path=="") return;
	else{
		int j, n, i;
		string name="", path1;
		
		j=0; n=(int)path.size();
		while(j<n && path[j]!='/'){
			name+=path[j];
			j++;
		}
		if(j==n) path1="";
		else path1=path.substr(j+1, path.size()-j-1);
		
		bool have=false;
		for(i=0; i<(int)f->child.size(); i++){
			if(f->child[i]->name==name){ have=true; break;}
		}
		if(have) mkdir(f->child[i], path1);
		else { 
			mks++;
			dir* t= new dir;
			t->name=name;
			f->child.push_back(t);
			mkdir(t, path1);
		}
	}
}


int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int n, m, t;
	string path;
	cin>>t;
	for(int j=0; j<t; j++){
		cin>>n>>m;

		root =new dir;
		root->name="root";
		
		mks=0;

		for(int i=0; i<n; i++){
			cin>>path;
			path=path.substr(1, path.size()-1);

			mkdir(root, path);
		}
		mks=0;

		for(int i=0; i<m; i++){
			cin>>path;
			path=path.substr(1, path.size()-1);

			mkdir(root, path);
		}

		cout<<"Case #"<<j+1<<": "<<mks<<endl;
	}
	


	return 0;
}




