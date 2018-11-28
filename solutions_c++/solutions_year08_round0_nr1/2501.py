#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char **argv)
{
	if(argc!=2){
		cerr<<"wrong number of parameters ... abort!\n";
		exit(1);
	}

	// read file ...
	ifstream inFile;
	inFile.open(argv[1]);
	if(!inFile){
		cerr<<"could not open inputfile "<<argv[1]<<", abort!\n";
		exit(2);
	}

	vector<string> searchEngine;
	vector<string> query;
	string tmpLine;
	int N=0, S=0, Q=0;

	// read number of cases
	inFile>>N;

	// loop over all cases
	for(int i=0;i<N;++i){
		// read number of search engines
		inFile>>S;
		getline(inFile, tmpLine);
		// read all search engines
		for(int j=0; j<S; ++j){
			getline(inFile, tmpLine);
			searchEngine.push_back(tmpLine);
		}
		// read number of querys
		inFile>>Q;
		getline(inFile, tmpLine);
		// read all querys
		for(int j=0; j<Q; ++j){
			getline(inFile, tmpLine);
			query.push_back(tmpLine);
		}

		int counter=0;
		int runs=0;	
		
		for(int a=0;a<(int)query.size();++a){

			for(int k=0; k<(int)searchEngine.size();++k){
				for(int j=a;j<(int)query.size();++j){
					if(searchEngine[k]==query[j]){
						if(j>counter){ 
							counter=j;
						}
						break;
					}else if(j==(int)query.size()-1){
						k=(int)searchEngine.size();
						counter=(int)query.size()+1;
					}
				}
			}			
			--counter;
			a=counter;
			if(a<(int)query.size())++runs;
		}
		searchEngine.clear();
		query.clear();
		cout<<"Case #"<<i+1<<": "<<runs<<"\n";
	}
	return 0;
}
