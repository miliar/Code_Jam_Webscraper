//============================================================================
// Name        : saveuni.cpp
// Author      : Lahiru Lakmal Priyadarshana
// Version     :
// Copyright   : 
// Description : Saving the Universe | Google Code Jam 2008
//============================================================================

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <map>

using namespace std;

int main() {
	
	int rounds = 0;
	int engcnt = 0;
	int qcnt = 0;
	string tmpstr;
	
	ifstream infile ("/home/lahiru/workstation/workspace/CodeJam/src/A-small.in");
	ofstream outfile ("/home/lahiru/workstation/workspace/CodeJam/src/A-small.out");
	if (infile.is_open())
	{
		infile >> rounds;
		int rrounds = rounds;
		
		while ( (rounds!=0) && (!infile.eof()) )
	    {
			infile >> engcnt;
			string engine[engcnt];
			getline(infile, tmpstr);
	      
	      for (int i = 0; i < engcnt; ++i) {
	    	  //infile >> engine[i];
	    	  getline(infile, engine[i]);
	    	  //cout << engine[i] << endl;
	      }
	      
	      infile >> qcnt;
  	      string query[qcnt];
  	      getline(infile, tmpstr);
  	      
  	      for (int i = 0; i < qcnt; ++i) {
  	    	  //infile >> query[i];
  	    	  getline(infile, query[i]);
  	    	  //cout << query[i] << endl;
  	      }
  	      
  	        map<int,int> enginemap;
			map<int,int>::iterator it;
			
			int maincounter = 0;
			int switches = 0;
			int temp = 0;
			
			while(maincounter < qcnt){
			
				for (int x = 0; x < engcnt; ++x) {
					temp = 0;
					for (int y = maincounter; y < qcnt; ++y) {
						if(engine[x] != query[y]){
							temp++;
						}
						else {
							break;
						}
					}
					if(temp != 0){
						enginemap.insert ( pair<int,int>(x,temp) );
					}
				}
				
				int max = 0;
				for ( it=enginemap.begin() ; it != enginemap.end(); it++ ){
					if( (*it).second > max )
						max = (*it).second;
					//cout << (*it).first << " => " << (*it).second << endl;
				}
				
				maincounter += max;
				//cout << maincounter;
				enginemap.clear();
				
				if(maincounter < qcnt){
					switches++;
				}
			}
			
			//cout << switches;
	      
  	      rounds--;
	      outfile << "Case #" << (rrounds-rounds) << ": " << switches << endl;
	    }
	    infile.close();
	    outfile.close();
	}
	else {
		
		cout << "Unable to open file";
		return 0;
	}
	
	return 0;
}