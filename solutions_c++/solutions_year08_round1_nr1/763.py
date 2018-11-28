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
		int n=0;
		vector<int> x;
		vector<int> y;
		infile>>n;
		for (int i=0;i<n;i++){
			int t=0;
			infile>>t;
			x.push_back(t);
		}
		for (int i=0;i<n;i++){
			int t=0;
			infile>>t;
			y.push_back(t);
		}
		sort(x.begin(),x.end());
		sort(y.begin(),y.end());
		int total=0;
		for (int i=0;i<n;i++){
			total+=x[i]*y[n-1-i];
		}
		cout<<"Case #"<<(c+1)<<": "<<total<<endl;
	
	}

	//clean up
	infile.close();
	return 0;
}

