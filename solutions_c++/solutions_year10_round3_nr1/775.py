#include<vector>
#include<iostream>
#include<fstream>
#include<string>
#include<map>
#include<set>
#include<sstream>
#include<algorithm>
#include<queue>
#include<cstring>
#include<cmath>
#include<cstdlib>
using namespace std;

int main(){
	//ifstream fin("A-tiny.in");
	//ofstream fout("A-tiny.out");
	//ifstream fin("A-small.in");
	//ofstream fout("A-small.out");
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int ncases;
	fin>>ncases;
	for(int Case=1;Case<=ncases;Case++){
		fout<<"Case #"<<Case<<": ";
		int n;
		fin>>n;
		vector<pair<int,int>  > lines;
		for(int i=0;i<n;i++)
		{
			int x,y;
			fin>>x>>y;
			lines.push_back(pair<int,int>(x,y));
		}
		int count = 0;
		for(int i=0;i<n;i++){
			for(int j=i+1;j<n;j++){
				if(lines[i].first > lines[j].first && lines[i].second < lines[j].second
					|| lines[i].first < lines[j].first && lines[i].second > lines[j].second){
					count++;
				}
			}
		}
		fout<<count<<endl;
	}


	return 0;
}