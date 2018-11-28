#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <math.h>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int used[1005];

void doit(int testcase, ifstream &infile, ofstream &outfile) {
	int N,W,L;
	infile>>N>>W>>L;
	vector<int> rs;
	vector<pair<int,int> > mapping;
	for(int i=0;i<N;i++) {
		int r;
		infile>>r;
		mapping.push_back(make_pair(r,i));
	}
	sort(mapping.begin(),mapping.end());
	for(int i=0;i<N;i++) rs.push_back(mapping[i].first);
	memset(used,0,sizeof(used));
	int curX=0,curY=0;
	vector<int> xs(N),ys(N);
	
	for(int i=0;;i++) {
		for(int j=N-1;j>=0;j--) if(!used[j]) {
			used[j]=1;
			if(i==0) {
				ys[j]=0;
			} else {
				ys[j]=curY+rs[j];
			}
			if(ys[j]>L) cout<<"BAD"<<endl;
			xs[j]=0;
			curX=rs[j];
			for(int k=j-1;k>=0;k--) if(!used[k]) {
				if(curX+rs[k]>W) continue;
				used[k]=1;
				xs[k]=curX+rs[k];
				ys[k]=ys[j];
				curX=curX+rs[k]+rs[k];
			}
			if(i==0) {
				curY+=rs[j];
			} else {
				curY+=rs[j]+rs[j];
			}
			break;
		}
		bool allUsed=true;
		for(int j=0;j<N;j++) if(!used[j]) {
			allUsed=false;
		}
		if(allUsed) break;
	}
	
	outfile << "Case #" << testcase << ":";
	for(int i=0;i<N;i++) {
		for(int j=0;j<N;j++) if(mapping[j].second == i)
			outfile<<" "<<xs[j]<<" "<<ys[j];
	}
	outfile<<endl;
}

int main()
{
	ifstream infile;
	//infile.open("in.txt");
	//ofstream outfile("out.txt");
	infile.open("B-large.in");
	ofstream outfile("B-large.out");
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