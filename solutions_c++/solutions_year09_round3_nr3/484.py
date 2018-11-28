/*
 * C.cpp
 */
#include <cassert>
#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

map<string, long> dict;

string toStr(int k) {
	string ret="";
	while(k) {
		ret.append(1, char(k%10+'0'));
		k/=10;
	}
	reverse(ret.begin(), ret.end());
	return ret;
}

string toKey(int q, vector<int> ps) {
	string ret=toStr(q); ret+="#";

	for(int i=0; i<ps.size(); i++)
		ret+=toStr(ps[i])+"#";
	return ret;
}

// release ps prisoners from q de minimum brides
long search(int q, vector<int> ps) {
	
	if(ps.size()==0) {
		return 0;
	}
	
	string key=toKey(q, ps);
	//cout<<" checking key: "<<key<<endl;
	if(dict.find(key)!=dict.end()) {
	//	cout<<"HIT: "<<dict[key]<<endl;
		return dict[key];
	}

	long m=-1;
	vector<int> v1, v2;
	for(int i=1; i<ps.size(); i++) {
		v2.push_back(ps[i]);
	}
	
	int len=ps.size();
	for(int i=0; i<len; i++) {
		long tmp1=search(ps[i]-1, v1);
		vector<int> vv2; 
		for(int j=0; j<v2.size(); j++) 
			vv2.push_back(v2[j]-ps[i]);
		long tmp2=search(q-ps[i], vv2);
		long tmp=q-1+tmp1+tmp2;
		if(m==-1 || tmp<m) m=tmp;
		v1.push_back(ps[i]); 
		if(v2.size()>0)
			v2.erase(v2.begin());
	}
	dict[key]=m;
//	cout<<" return value "<<m <<" for key: "<<key<<endl;
	return m;
}

int main( int argc, const char* argv[] ) {
	if(argc>1) assert(freopen(argv[1], "r",stdin));
	if(argc>2) assert(freopen(argv[2], "w",stdout));
	
	int caseNum; scanf("%d", &caseNum);
	for(int k=0; k<caseNum; k++) {
		int q, no; scanf("%d %d", &q, &no);
		vector<int> ps;
		for(int i=0; i<no; i++) {
			int tmp; scanf("%d", &tmp); ps.push_back(tmp);
		}
		
		dict.clear();
		printf("Case #%d: %ld\n", k+1, search(q, ps));
	}
	
	/////////////////
	
	return 0;
}

