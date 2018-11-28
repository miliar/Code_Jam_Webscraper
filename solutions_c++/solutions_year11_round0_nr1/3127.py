#include <sstream>
#include <iostream>
#include <fstream>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
using namespace std;

#define FOR(i,a) for (int (i)=0;(i)<(a);++(i))
#define FORR(i,a,b) for (int (i)=(a);(i)<(b);++(i))
#define sz(a) int((a).size()) 
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end() 

vector<string> rozdel(const string& st, string oddelovac){
	vector<string> vystup(0);
	int odkial, kam;
	odkial=st.find_first_not_of(oddelovac,0);
	while(odkial!=-1){
		kam=st.find_first_of(oddelovac,odkial);
		if (kam==-1) kam=st.size();
		vystup.push_back(st.substr(odkial,kam-odkial));
		odkial=st.find_first_not_of(oddelovac,kam);
	}
	return vystup;
}

int strToInt(const string& x){
	return atoi( x.c_str() );
}

main(){
	ofstream fout ("A-large-0.out");
	ifstream fin ("A-large-0.in");
	int num;
	fin>>num;
	string line;
	getline(fin,line);

	FOR(temp,num){
//		int out=0;
		getline(fin,line);
//		cout<<line<<endl;
		vector<string> a=rozdel(line," ");
		int lastT[2]={0,0};
		int lastPos[2]={1,1};
		int time=0;
		for(int i=1;i<a.size();i+=2){
			int act=(a[i]=="O"? 1 : 0);
			time=max(time+1,abs(lastPos[act]-strToInt(a[i+1]))+lastT[act]+1);
			lastT[act]=time;
			lastPos[act]=strToInt(a[i+1]);
		}
		fout<<"Case #"<<temp+1<<": "<<time<<endl;
	}
	fout.close();
}
