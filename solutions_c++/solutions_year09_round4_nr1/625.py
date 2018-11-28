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

vector<int> a;

void swap(int i, int j){
	int pom=a[i];
	a[i]=a[j];
	a[j]=pom;
}

main(){
	ofstream fout ("A-small.out");
	ifstream fin ("A-small.in");
	int T;
	fin>>T;
	for (int k=0;k<T;k++){
		int N;
		fin>>N;
		a.clear();
		a.resize(N,0);
		for(int i=0;i<N;i++){
			string pom;
			fin>>pom;
			for(int j=0;j<pom.size();j++){
				if (pom[j]=='1') a[i]=j;
			}
		}
		
		int out=0;
		for(int i=0;i<N;i++){
			if (a[i]>i){
				int p=0;
				for(int j=i+1;j<N;j++){
					if (a[j]<=i){
						p=j;
						break;
					}
				}
				for (int j=p;j>i;j--){
					swap(j,j-1);
					out++;
				}
			}
		}

		fout<<"Case #"<<k+1<<": "<<out<<endl;
	}
	fout.close();
}
