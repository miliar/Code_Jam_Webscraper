/*
 * A.cpp
 *
 *  Created on: 22 mai 2010
 *      Author: Rafael
 */
#include<iostream>
#include<fstream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include <set>

using namespace std;
#define ROOT "/"
//map<string,string> PAI;
map<string,bool> CREATED;

vector<string> parse(string s){
	vector<string> ret;
	string u="";
	s+='/';
//	ret.push_back(ROOT);
	u+=s[1];
	for(int i=2;i<s.size();i++){
		if(s[i]=='/')
			ret.push_back(u);
		u=u+s[i];
	}
	return ret;
}

void put1(string s){
	  vector<string> vs = parse(s);
	  for(int i = 0 ; i < vs.size(); i++)
		  CREATED[vs[i]]=1;
}

int put2(string s){
	  vector<string> vs = parse(s);
	  int ret=0;
	  for(int i = 0 ; i < vs.size(); i++)
		  if(!CREATED[vs[i]])
			  {
			  CREATED[vs[i]]=1;
			  ret++;
			  }
	  return ret;
}




void AProblem(){
	int T,N,M;
	cin>>T;
	for(int t = 1; t<=T; t++){
		cout<<"Case #"<<t<<": ";
//		PAI.clear();
		CREATED.clear();
//		PAI[ROOT]=ROOT;
		CREATED[ROOT]=true;
		string s;
		cin>>N>>M;
		for(int i = 0; i < N;i++){
					cin>>s;
					put1(s);
				}
		int ret = 0;
		for(int i = 0; i < M;i++){
					cin>>s;
					ret+=put2(s);
		}
		cout<<ret<<"\n";
	}


}


int main(){
	AProblem();
	return 0;
}
