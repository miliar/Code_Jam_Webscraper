#include<iostream>
#include<algorithm>
#include<string>
#include<map>
#include<vector>

using namespace std;

int main(){
	map<char,map<char,char> > me;
	map<char,map<char,int> > mo;
	vector<char>v;
	int t;
	int x,y,z;
	string a,b,c;
	cin>>t;
	for(int k=1;k<t+1;k++){
		me.clear();
		mo.clear();
		v.clear();
		cin>>x;
		for(int i=0;i<x;i++){
			cin>>a;
			me[a[0]][a[1]]=a[2];
			me[a[1]][a[0]]=a[2];
		}
		cin>>x;
		for(int i=0;i<x;i++){
			cin>>a;
			mo[a[0]][a[1]]=1;
			mo[a[1]][a[0]]=1;
		}
		cin>>x;
		cin>>a;/*
		if(x==1){
			v.push_back(a[0]);
		}else{
			v.push_back(a[0]);
			v.push_back(a[1]);
			if(me[a[0]][a[1]]!=0){
				v.clear();
				v.push_back(me[a[0]][a[1]]);
			}else if(mo[a[0]][a[1]]==1){
				v.clear();
			}
		}*/
		for(int i=0;i<x;i++){
			if(v.size()>=1){
				if(me[v[v.size()-1]][a[i]]!=0){
					v[v.size()-1]=me[v[v.size()-1]][a[i]];
				}else{
					v.push_back(a[i]);
				}
				for(int j=0;j<v.size()-1;j++){
					if(mo[v[v.size()-1]][v[j]] == 1){
						v.clear();
						break;
					}
				}
			}else{
				v.push_back(a[i]);
			}
	//		for(int j=0;j<v.size();j++){
	//			cout<<v[j];
	///		}
	//		cout<<endl;
		}
		cout<<"Case #"<<k<<": [";
		for(int i=0;i<v.size();i++){
			if(i==v.size()-1){
				cout<<v[i];
			}else{
				cout<<v[i]<<", ";
			}
		}
		cout<<"]"<<endl;
	}
	return 0;
}
