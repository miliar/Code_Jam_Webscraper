#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <set>
#include <cmath>
#include <string>
using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

int T,t;
int k;
string s,ss;

int fact(int n) {
	int ret=1;
	int i;
	for(i=1;i<=n;i++)ret*=i;
	return ret;
}

int main() {
	fin>>T;
	vector<int> vec;
	int i,j,p;
	int ret,tmp;
	for(t=1;t<=T;t++) {
		fin>>k>>ss;
		vec.resize(k);
		for(i=0;i<k;i++)vec[i]=i;
		ret=-1;
		for(p=1;p<=fact(k)+2;p++) {
			s=ss;
			for(i=0;i<ss.size();i+=k) {
				for(j=0;j<k;j++) {
					s[i+vec[j]]=ss[i+j];
				}
			}
			tmp=1;
			for(i=1;i<s.size();i++) {
				if(s[i]!=s[i-1])tmp++;
			}
			if(ret==-1 || tmp<ret){ret=tmp;}
			next_permutation(vec.begin(),vec.end());
		}
		fout<<"Case #"<<t<<": "<<ret<<endl;
	}
	return 0;
}