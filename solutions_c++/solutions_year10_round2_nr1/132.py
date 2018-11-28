#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

int n,m;

int main() {
	int T;
	fin>>T;
	int i,j;
	string s,tmp;
	int t;
	for(t=1;t<=T;++t) {
		fin>>n>>m;
		set<string> dirs;
		dirs.insert("/");
		for(i=0;i<n;++i) {
			fin>>s;
			tmp = "";
			tmp += s[0];
			for(j=1;j<s.size();++j) {
				if(s[j]=='/') {
					dirs.insert(tmp);
				}
				tmp += s[j];
			}
			dirs.insert(s);
		}
		int ret = 0;
		for(i=0;i<m;++i) {
			fin>>s;
			tmp = "";
			tmp += s[0];
			for(j=1;j<s.size();++j) {
				if(s[j]=='/') {
					if(dirs.find(tmp)==dirs.end()) {
						++ret;
						dirs.insert(tmp);
					}
				}
				tmp += s[j];
			}
			if(dirs.find(s)==dirs.end()) {
				++ret;
				dirs.insert(s);
			}
		}
		fout<<"Case #"<<t<<": "<<ret<<endl;
	}
	return 0;
}
