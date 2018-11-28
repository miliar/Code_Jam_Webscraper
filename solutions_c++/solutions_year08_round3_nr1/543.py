#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

//Compiled using MS VC++ 2005

int main (int argc,char* argv[]) {	
	int cs=0;	//# of cases
	ifstream infile;
	infile.open (argv[1], ifstream::in);
	infile>>cs;
	for (int c=0;c<cs;c++){
		int p=0;
		int l=0;
		int k=0;
		vector<long long> freq;
		infile>>p>>k>>l;
		for (int i=0;i<l;i++){
			int f=0;
			infile>>f;
			freq.push_back(f);
		}
		sort(freq.begin(),freq.end());
		long long total=0;
		int key=0;
		long long press=1;
		for (int i=0;i<l;i++){
			key++;
			if (key>k){
				key=1;
				press++;
			}
			total+=(freq[l-1-i])*(press);
		}
		cout<<"Case #"<<(c+1)<<": "<<total<<endl;
	
	}

	//clean up
	infile.close();
	return 0;
}

