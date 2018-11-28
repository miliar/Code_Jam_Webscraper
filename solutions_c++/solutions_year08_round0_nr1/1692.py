#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	ifstream fin;
	fin.open("A-small.in");
	ofstream fout;
	fout.open("output.txt");
	int N;
	fin >> N;
	int S;
	int Q;
	cout << N;
	for(int i=0;i<N;i++){
		vector <string> engines;
		string engine;
		string query;
		vector <string> queries;
		map <string,int> mp;
		fin >> S;
		cout << S << endl;
		fin.get();
		for(int j=0;j<S;j++){
			getline(fin,engine);
			engines.push_back(engine);
			mp[engine]=0;
		}
		cout << "Hello" << endl;
		fin >> Q;
		cout << "JJD" << Q << endl;
		fin.get();
		for(int j=0;j<Q;j++){
			getline(fin, query);
			cout << "sss" << endl;
			queries.push_back(query);
		}
		int switches = 0;
		int remfree = engines.size();
		for(int j=0;j<Q;j++){
			if(mp.count(queries[j])!=0){
				cout << "&&&&&&&&" << endl;
				if(mp[queries[j]]==0){
					remfree--;
				}
				if(remfree==0){
					switches++;
					for(int k=0;k<S;k++){
						mp[engines[k]]=0;
					}
					remfree = engines.size()-1;
				}
				mp[queries[j]] = mp[queries[j]]+1;
			}
		}
		fout << "Case #" << i+1 << ": " << switches << endl;


	}

	return 0;

}