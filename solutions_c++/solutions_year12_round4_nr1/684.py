#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <math.h>
#include <map>
#include <set>

using namespace std;

int mem[10001];

void doit(int testcase, ifstream &infile, ofstream &outfile) {
	int N;
	infile>>N;
	vector<int> xs, ls;
	for(int i = 0; i < N; i++) {
		int x,l;
		infile>>x>>l;
		xs.push_back(x);
		ls.push_back(l);
	}
	int total;
	infile>>total;
	memset(mem,-1,sizeof(mem));
	mem[0]=xs[0];
	bool ok=false;
	for(int i=0;i<N;i++) {
		if(xs[i]>0) {
			int start=xs[i];
			int reach=xs[i]+mem[i];
			if(reach>=total) { ok=true; break; }
			for(int j=i+1;j<N;j++) {
				if(xs[j]<=reach) {
					int next=min(xs[j]-xs[i],ls[j]);
					if(next>mem[j]) mem[j]=next;
				} else {
					break;
				}
			}
		}
	}
	if(ok) outfile << "Case #" << testcase << ": " << "YES" << endl; 
	else outfile << "Case #" << testcase << ": " << "NO" << endl; 
}

int main()
{
	ifstream infile;
	//infile.open("in.txt");
	//ofstream outfile("out.txt");
	infile.open("A-small-attempt0.in");
	ofstream outfile("A-small-attempt0.out");
	int cases;
	if (infile.is_open()) {
		infile>>cases;
	}
	else {
		return 0;
	}
	for(int i=0;i<cases;i++) {
		doit(i+1,infile,outfile);
	}
	cout<<"DONE"<<endl;
	string zzz;
	cin>>zzz;
	outfile.close();
	return 0;
}