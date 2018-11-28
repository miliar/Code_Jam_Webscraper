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

main(){
	ofstream fout ("C-small.out");
	ifstream fin ("C-small.in");
	string s="welcome to code jam";
	int N;
	fin>>N;
	for (int k=0;k<N;k++){
		string line;
		getline(fin,line);
		if (k==0){
			getline(fin,line);
		}		
		vector<vector<int> > a(line.size(),vector<int>(s.size(),0));
		for(int i=0;i<line.size();i++){
			for(int j=0;j<s.size();j++){
				if (i>0){ a[i][j]=a[i-1][j];}
				if (line[i]==s[j]){
					if (j==0){
						a[i][j]++;
					}
					else if (i>0) a[i][j]+=a[i-1][j-1];
				}
				a[i][j]%=10000;
			}
		}
		int out=a[line.size()-1][s.size()-1];
		fout<<"Case #"<<k+1<<": ";
		if (out<1000) fout<<"0";		
		if (out<100) fout<<"0";		
		if (out<10) fout<<"0";
		fout<<out<<endl;
	}
	fout.close();
}
