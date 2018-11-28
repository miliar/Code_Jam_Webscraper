#include <iostream>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;
void process(vector<int> googlers,int leastPt,int surprises,int& counter)
{
	int surpriseCout = 0;
	for(size_t i = 0; i < googlers.size(); ++i){
		int googler = googlers.at(i);	
		if(googler < leastPt) // impossible
			continue;
		
		if(googler/3 >= leastPt){
			counter++;
		}
		else{
			
			int rem = (googler - leastPt)/2;
			if( abs(leastPt - rem) <  2 ){
				counter++;
			}
			else if(abs(leastPt - rem) ==  2 ){
				surpriseCout++;
				if(surpriseCout <= surprises){
					counter++;
				}
			}
		}
	}
}

bool isSuprise(int i, int j, int k)
{
	return (abs(i-j) < 1 && abs(i-k) < 2 && abs(j-k) < 2);
}

int main(int argc, char** argv)
{
	if(argc < 2){
		cerr  << "\nargument missing.\n"
				<< "\tUsage : "<< argv[0] << " <<inputFile>>\n\n";
	
		exit(-1);
	}
	
	ifstream infile(argv[1],ifstream::in);
	ofstream ofile("output.in", ofstream::out);
	
	if(!infile || !ofile){
		cerr << "Can't open files\n";
		exit(-1);
	}
	vector<int> googlers;
	int nbCase,N, surprises, leastPt,counter;
	string line;
	
	getline(infile,line);
	istringstream str(line);
	str >> nbCase;
	for(int i = 1; i <= nbCase; ++i){
		getline(infile,line);
		istringstream str1(line);
		str1 >> N >> surprises >> leastPt;
		int ti;
		googlers.clear();
		while (str1 >> ti){
			googlers.push_back(ti);
		}
		counter = 0;
		process(googlers, leastPt, surprises, counter);
		ofile << "Case #" << i << ": " << counter << endl;		
	}
		
	infile.close();
	ofile.close();
	return 0;
}