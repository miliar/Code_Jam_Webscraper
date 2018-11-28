
#include <iostream>
#include <fstream>
#include <map>
#define LSZ 102
#define QSZ 104
using namespace std;
using std::cout;

int main () 
{
    ifstream myfile;
	int datasets=0;
    myfile.open ("A-large.in");
   
	myfile >> datasets;

	for (int i=0; i< datasets; i++) {	
		map<string,int> eng;
		int neng=0;
		int nq=0;
		string engname="";
		string engnamep="";

		int globcount=0;
	
		myfile >> neng;				
							//cout << neng << endl;

		if (neng > 0) {
			myfile.get(); 
		 	for (int j=0; j< neng; j++) {
				char arr[LSZ];
				myfile.getline(arr,LSZ);		
							//check for ws errors, recall usage of null and such
				string engname(arr);
							//myfile >> engname;
							//cout << "engname: " << engname << endl;
				eng.insert(pair<string,int>(engname,0));
		}
		}		

		myfile >> nq;
							//cout << "numqueries "<< nq << endl;

		//usurp first one, last one is relevant, count reflects direction to

		if (nq > 0) {
			myfile.get();
		
							//rethink briefly
							//char arr[LSZ];
							//myfile.getline(arr,LSZ);
							//string engname(arr);
							//myfile >> engname;
							//engnamep = engname;
							//cout << engname << endl;
							//for (int k=1; k< nq; k++) {
							
			// map initialized to 0							
			int count=0;

			for (int k=0; k< nq; k++) {	
				char arr[LSZ];				
				myfile.getline(arr,LSZ);
							//myfile >> engname;
				string engname(arr);
							//cout << engname << endl;
				if (engname != engnamep) {
					//ugly code but oh so sleepy, the good dr.pepp is not pepping
					if (eng.find(engname)->second == 0) count++;
					eng.find(engname)->second++;
							//cout << eng.find(engname)->second << endl;					
					if (count == eng.size()) {

						// clear the map
				        map<string,int>::iterator it;
			        
				        for (it = eng.begin(); it != eng.end(); it++) {
	        	    		(*it).second=0;
						}
						//set ourselves (should be boolean really but eh)
						eng.find(engname)->second++;
						count = 1;

						// switch
						globcount++;
					}

					engnamep = engname;		
				}		
			}
		}

		cout << "Case #" << i+1 << ": " << globcount << endl;

	}




	end:
		//print the output whether any data or no data
	

    myfile.close();
    return 0;
}


