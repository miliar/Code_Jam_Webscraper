
#include<iostream>
#include<fstream>
#include<string>
#include<set>

using namespace std;


ifstream filein("A-large.in");
ofstream fileout("file2.out");


int main(){
	int i,j,k,u,v,w,n,s,q;
	string str[101],qstr[1001],strtemp;
	bool app;
	set <string> a;
	filein>>n;
	for(i = 0; i<n;i++){
		filein>>s;
		for(j = 0;j<s+1;j++){
			getline(filein,str[j]);
		}
		v = 0;
		filein>>q;
		a.clear();
		for(j = 0 ; j< q+1;j++){
			getline(filein,strtemp);
			if(j){
				a.insert(strtemp);
			}
			if(a.size()==s){
				//fileout<<strtemp<<'\t'<<a.size()<<'\t';
				a.clear();
				v++;
				a.insert(strtemp);
			}
		}
		/*
		u = 1;
		v = 0;
		w = 1;
		for(k=2;k<=q;){
			app = false;
			for(j= u;j<k;j++){
				if(qstr[k].compare(qstr[j])==0)
					app = true;
			}
			if(!app)w++;
			if(w>s-1){
				v++;
				u = k;
				w = 1;
			}
			k++;
		}
		*/
		fileout<<"Case #"<<i+1<<": "<<v<<endl;
	}
	return 0;
}