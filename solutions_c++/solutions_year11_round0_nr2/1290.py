#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;


int main(){
    int T;
    cin >> T;
    for(int TT=1;TT<=T;++TT){
	map<string, char> c;
	set<string> d;
	string ret;
	string inv;
	int t;
	cin >> t;
	for(int i=0;i<t;++i){
	    string ts;
	    cin >> ts;
	    string ss;
	    ss.push_back(ts[0]);
	    ss.push_back(ts[1]);
	    c[ss]=ts[2];
	    reverse(ss.begin(),ss.end());
	    c[ss]=ts[2];
	}
	
	cin >> t;
	for(int i=0;i<t;++i){
	    string ts;
	    cin >> ts;
	    d.insert(ts);
	    reverse(ts.begin(),ts.end());
	    d.insert(ts);
	}
	cin >> t;
	cin >> inv;
	for(int i=0;i<inv.size();++i){
	    if(ret.empty()){
		ret.push_back(inv[i]);
		continue;
	    }
	    string x(1,inv[i]);
	    x.push_back(ret[ret.size()-1]);
	    if(c.count(x)!=0){
		ret[ret.size()-1] = c[x];
		continue;
	    }
	    for(int j=0;j<ret.size();++j){
		string y(1,ret[j]);
		y.push_back(inv[i]);
		if(d.count(y)) ret = "";
	    }
	    if(!ret.empty()) ret.push_back(inv[i]);
	}
	cout << "Case #" << TT << ": [";
	string sep;
	for(int i=0;i<ret.size();++i){
	    cout << sep;
	    sep = ", ";
	    cout << ret[i];
	}
	cout << "]" << endl;
    }
}
