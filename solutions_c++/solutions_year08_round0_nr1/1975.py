#include<iostream>
#include<fstream>
#include<vector>
#include<map>

using namespace std;

void displayPath(vector<int> laneno) {
	cout<<"The path is :";
	for(int i=0; i<laneno.size(); i++) {
		cout<<laneno[i]<<" ";
	}
	cout<<endl;
}

void displayQueryMap(map<string, vector<int> >& qmap) {
	map<string, vector<int> >::iterator iter;
	cout<<"QMAP IS AS FOLLOWS:\n";
	for(iter=qmap.begin(); iter!=qmap.end(); iter++) {
		cout<<(*iter).first<<": ";
		for(int i=0; i<(*iter).second.size(); i++) 
			cout<<(*iter).second[i]<<" ";
		cout<<endl;
	}
}

void displayStringVector(vector<string> aa) {
	cout<<"A total of "<<aa.size()<<" elements:\n";
	for(int i=0; i<aa.size(); i++) {
		cout<<aa[i]<<endl;
	}
}

void readNLines(ifstream& inFile, vector<string>& vec) {
	int vecsize;
	inFile>>vecsize;
	inFile.get(); // clear out the endline character
	//cerr<<"vecsize="<<vecsize<<endl;

	vec.resize(vecsize, "");
	for(int i=0; i<vecsize; i++) {
		getline(inFile, vec[i]);
	//	cerr<<vec[i]<<endl;
	}
}

void createQueryMap(vector<string>& engine, vector<string>& query, 
		map<string, vector<int> >& qmap) {
	// only engines exist in the query map!
	for(int i=0; i<engine.size(); i++)
		qmap.insert(make_pair(engine[i], vector<int>()));
	map<string, vector<int> >::iterator iter;
	for(int i=0; i<query.size(); i++) {
		iter=qmap.find(query[i]);
		if(iter==qmap.end()) continue;
		(*iter).second.push_back(i);
	}
	for(iter=qmap.begin(); iter!=qmap.end(); iter++)
		(*iter).second.push_back(query.size()+1);
	displayQueryMap(qmap);
}

int runLoLaneChangeHighway(map<string, vector<int> >& qmap, int maxn) {
	vector<int> laneno;
	int currnum=-1, i;
	map<string, vector<int> >::iterator iter;
	int maxnum=-1, maxnumlane;
	vector<int> qmapidx(qmap.size(), 0);
	while(currnum<maxn) {
		for(iter=qmap.begin(), i=0; iter!=qmap.end(); iter++, i++) {
			// remove lanes that are shorter than current longest
			while((*iter).second[qmapidx[i]]-1<currnum) {
				qmapidx[i]++;
			}
			// is this a candidate lane?
			if((*iter).second[qmapidx[i]]-1>maxnum) {
				maxnum=(*iter).second[qmapidx[i]]-1;
				maxnumlane=i;
			}
		}
		laneno.push_back(maxnumlane);
		currnum=maxnum;
	}
	displayPath(laneno);
	int nchanges=laneno.size()-1;
	if(nchanges<0) nchanges=0;
	return nchanges;
}

int processCase(ifstream& inFile) {
	vector<string> engineName, query;
	map<string, vector<int> > qmap;

	readNLines(inFile, engineName);
	//displayStringVector(engineName);

	readNLines(inFile, query);
	//displayStringVector(query);

	createQueryMap(engineName, query, qmap);
	return runLoLaneChangeHighway(qmap, query.size());
}

void processFile(char* infname, char* outfname) {
	// SETUP
	// open all files
	ifstream inFile(infname);
	ofstream outFile(outfname);

	int N=0;
	inFile>>N;
	cerr<<"N="<<N<<endl;
	for(int i=0; i<N; i++) {
		cerr<<"Case #"<<i+1<<" of "<<N<<endl;
		outFile<<"Case #"<<i+1<<": ";
		outFile<<processCase(inFile);
		outFile<<endl;
		cerr<<endl<<endl;
	}

	// CLEANUP
	// close all files
	inFile.close();
	outFile.close();
}

int main(int argv, char** argc) {
	processFile(argc[1], argc[2]);
	return 0;
}
