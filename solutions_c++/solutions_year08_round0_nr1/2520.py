#include <iostream>
#include "Reader.h"

using namespace std;

int getMaxRange(vector<string>& queries, string searcher, int posInQueries) {
    for(int i=posInQueries; i<queries.size(); i++) {
	if(searcher == queries.at(i)) {
	    return i;
	}
    }
    return -1;
}

int algorithm(vector<string>& searchers, vector<string>& queries) {
/*    cout<<"searchers :" <<endl;
    for(int i =0; i<searchers.size(); i++) {
	cout<<i<<" : "<<searchers.at(i)<<endl;
    }
    cout<<"queries : "<<endl;
    for(int i=0;i<queries.size(); i++) {
	cout<<i<<" : "<<queries.at(i)<<endl;
    }*/

    // calculate max range this is our next switch
    int maxRange = 0;
    int switches = 0;
    while(1) {
	    int actPos = maxRange;
	    for(int sNr=0; sNr<searchers.size(); sNr++) {
		int newRange = getMaxRange(queries, searchers.at(sNr), actPos);
		if(newRange == -1) {
		    return switches; 
		}
		if (newRange>maxRange) {
		    maxRange=newRange;
		}
	    }
	    switches++;
    }
}


void processData(Reader& reader) {
    int cases = reader.GetIntData(0);
    int globPos = 1;
    for(int case_=0; case_<cases; case_++) {
	int numSearcher = reader.GetIntData(globPos);
	++globPos;
	vector<string> searchers;
	for(int i=0; i<numSearcher; i++) {
	    searchers.push_back(reader.GetData(globPos));
	    globPos++;
	}
	string test = reader.GetData(globPos);
	//cout<<"test : "<<test<<endl;
	int numQueries = reader.GetIntData(globPos);
	++globPos;
	vector<string> queries;
	for(int i=0; i<numQueries; i++) {
	    queries.push_back(reader.GetData(globPos));
	    globPos++;
	}
	int result = algorithm(searchers, queries);
	cout<<"Case #"<<case_+1<<": "<<result<<endl;
    }
}

int main(int argc, char* argv[]) {
    if(argc<2) {
	cout<<"Usage 'cmd file'"<<endl;
    }
    string fileName(argv[1]);
    Reader reader;
    reader.Parse(fileName);
    processData(reader);
}
