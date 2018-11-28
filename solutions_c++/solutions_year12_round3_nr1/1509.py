#include<vector>
#include<iostream>
#include<algorithm>
#include<fstream>
#include<stdlib.h>
#include<map>
#include "str.h"
using namespace std;

int reachable(map<int,vector<int> > m,int n){
	vector<int> v;
	map<int,int> m1;
	v.push_back(n);
	for(int i=0;i<v.size();i++){
		vector<int>::const_iterator itr=m[v[i]].begin();
		while(itr!=m[v[i]].end()){
			if(find(v.begin(),v.end(),*itr)!=v.end()){
				return 1;
			}
			else{
				v.push_back(*itr);
			}
			++itr;
		}
	}
	return 0;
}

int main()
 {
	ifstream fin("C:\\users\\Anshul\\Downloads\\A-small-attempt0 (2).in");
	ofstream fout("C:\\users\\Anshul\\Downloads\\out20.txt");
	int T=0;
	fin>>T;
	cout<<T;
	for(int i=0;i<T;i++){
		int N=0, M=0;
		fin>>N;
		cout<<endl<<N;
		map<int,vector<int> > m;
		vector<int> v;
		vector<int> res;
		int c=0,sum=0;
		for(int j=0;j<N;j++){
			fin>>M;
			cout<<endl<<M;
			for(int k=0;k<M;k++){
				int n=0;
				fin>>n;
				m[j+1].push_back(n);
			}
		}
		int test=0;
		for(int j=0;j<N;j++){
			if(reachable(m,j+1)){
				test=1;
				break;
			}
		}
		fout<<"Case #"<<i+1<<": ";
		if(test){
			fout<<"Yes";
		}
		else{
			fout<<"No";
		}
		fout<<endl;
	}	
	system("pause");
	return 0;
 }