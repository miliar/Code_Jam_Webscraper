#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>
using namespace std;

#define ulli unsigned long long int
#define lli long long int

#define f(i,n) for(ulli i = 0; i < n; i++)

typedef struct dir{
	string name;
	vector <struct dir> child;
} dir;

int insdir(dir* par,string ndir){
	//cout<<ndir<<endl;
	int nins = 0;
	int t;
	if(ndir.size()==0){
		return 0;
	}
	int sl = ndir.find('/');
	if (sl>=ndir.size()){sl = ndir.size();}
	string c = ndir.substr(0,sl);
	//cout<<"c:"<<c<<endl;
	int found = 0;
	int i=0;
	for(i =0; i < par->child.size();i++){
		if(par->child[i].name==c){
			found = 1;
			//cout<<"found"<<endl;
			if(sl<ndir.size()){
				nins += insdir(&par->child[i],ndir.substr(sl+1));
			}
			break;
		}
	}
	if(!found){
		//cout<<"notfound"<<endl;
		nins++;
		dir newdir;
		newdir.name = c;
		par->child.push_back(newdir);
		if(sl<ndir.size()){
			nins += insdir(&par->child[par->child.size()-1],ndir.substr(sl+1));
		}
	}
	return nins;
	
}


int main(){
	int ntc = 0;
	cin>>ntc;
	
	f(tc,ntc){
		ulli n, m;
		cin >> n;
		cin >> m;
		string ndir;
		string path;
		dir root;
		root.name = "root";
		int totins =0;
		int tmpins = 0;
		for(int i = 0; i < n; i++){
			cin>>ndir;
			tmpins=insdir(&root,ndir.substr(1));			
		}
		for(int i = 0; i < m; i++){
			cin>>ndir;
			totins+=insdir(&root,ndir.substr(1));			
		}
	
		
		
		cout << "Case #"<<tc+1<<": "<<totins<<endl;;
	}
	return 0;
}
