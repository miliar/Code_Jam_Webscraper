#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
using namespace std;

vector<string> split(string niz,char znak) {
	vector<string> rez;
	string del="";
	int i;
	for (i=0;i<niz.size();i++) {
		if (niz[i]==znak) { rez.push_back(del); del=""; }
		else { del+=niz[i]; }
	}
	rez.push_back(del);
	return rez;
}

vector<vector<string> > fs;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
    cin >> t;
    for (int ti=1;ti<=t;ti++) {
    	fs.clear();
    	int n,m;
    	cin >> n >> m;
    	string p;
    	vector<string> path;
    	for (int i=0;i<n;i++) {
    		cin >> p;
    		p=p.substr(1);
			path=split(p,'/');
    		fs.push_back(path);
    	}
    	vector<vector<string> > make;
    	for (int i=0;i<m;i++) {
    		cin >> p;
    		p=p.substr(1);
			path=split(p,'/');
    		make.push_back(path);
    	}
    	sort(make.begin(),make.end());
    	int r=0;
    	for (int i=0;i<make.size();i++) {
    		int best=make[i].size();
    		for (int j=0;j<fs.size();j++) {
    			int cnt=make[i].size();
    			for (int k=0;k<min(fs[j].size(),make[i].size());k++) {
    				if (fs[j][k]==make[i][k]) cnt--; else break;
    			}
    			if (cnt<best) best=cnt;
    		}
    		r+=best;
    		fs.push_back(make[i]);
    	}
    	printf("Case #%d: %d\n",ti,r);
    }
    return 0;
}
