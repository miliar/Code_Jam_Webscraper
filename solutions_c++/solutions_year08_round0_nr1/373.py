#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

//Compiled using MS VC++ 2005

/*
We will use count off how many search engines we have queried for.
Once that == the # of engines, we'll have to switch to query for that last engine.
Let's assume we use this method to come up  with our answer. let's also assume we have at least 2 "segments" b/c
the case with a switch of 0 is trivial (use the engine not queried for).  A switch of 1 is also trivial since every engine was search for at least
once, u can't do better than 1 switch. We also assume at least 3 engines otherwise again, its trivial.
So we need to find a situation where using this method results in 3 segments when 2 segments could do. assume thats the case.
Say we use A for the 1st segment and B for the 2nd.  The 3rd is either A, or C, but that doesnt matter.
For the 1st segment, we cant just change A and reduce the # of switches, since 1st seg contais every other engine (so does the 2nd!).
We have to change the 1st and 2nd engine.  if we change the 1st, we have to switch earlier, and then we cant use a or b for the 2nd segment we 
have to use a different engine, but thats also contained in the 2nd segment, requiring another switch!
*/

//Takes the input file as only argument and spits to cout
int main (int argc,char* argv[]) {	
	char buffer[256];	//each line <=100 
	int cs=0;	//# of cases
	ifstream infile;
	infile.open (argv[1], ifstream::in);
	infile>>cs;
	string query;
	for (int c=0;c<cs;c++){
		int es=0;	//# of engines
		int qs=0;	//# of queries
		int s=0;	//# of switches
		map<string,bool> queried;	//keep trackwhich engines were queried for
		infile>>es;
		//Eat the newline. Not using ignore in case of encoding problems
		//infile.ignore(1,'\n');
		infile.getline(buffer,256);		
		for (int e=0;e<es;e++){
			infile.getline(buffer,256);
		}
		infile>>qs;
		infile.getline(buffer,256);
		for (int q=0;q<qs;q++){
			infile.getline(buffer,256);
			query=buffer;
			queried[query]=true;
			if (queried.size()==es){
				s++;
				queried.clear();
				queried[query]=true;	//count the new engine in the NEXT switch
			}
		}
		cout<<"Case #"<<(c+1)<<": "<<s<<endl;
	}

	//clean up
	infile.close();
	return 0;
}

