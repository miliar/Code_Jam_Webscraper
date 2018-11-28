#include<iostream>
#include<fstream>
#include<string>

#include<sstream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<map>
using namespace std;

int main(){
	int testcase;
	ifstream infile;
	ofstream outfile;
	infile.open("B-large.in"); //filename//
	outfile.open("result.txt");
	
	infile>>testcase;

	for(int i=0;i<testcase;i++){
		int n, s, p;
		int result;
		//do something
		infile>>n>>s>>p;

		int bwos, bws;
		if(p==0){// p == 0 --> all value is accepted(no comp need)
			result = n;
			string temp;
			getline(infile, temp);
		}
		else{
			bws = p * 3 - 4;
			bwos = p * 3 - 2;
			int bwoscnt = 0;
			int bwscnt = 0;
			if(bws<0) bws = 30;//impossible
			for(int i=0;i<n;i++){
				int temp;
				infile>>temp;
				if(temp>=bwos)
					bwoscnt++;
				else if(temp>=bws)
					bwscnt++;
			}
			if(s<bwscnt) bwscnt = s;
			result = bwoscnt+bwscnt;

			//condition:: p == 1 -> bws is never happen
			
		}

		//do something end
		outfile<<"Case #"<<i+1<<": "<<result<<"\n";
	}
	infile.close();
	outfile.close();
	return 0;
}