#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(){
	ifstream infile("/home/hawkwing/Desktop/B-large.in");
	int cases;
	infile >> cases;
	int N[cases],S[cases],p[cases];
	vector< vector<int> > points;
	for(unsigned int i=0;i<cases;i++){
		infile >> N[i] >> S[i] >> p[i];
		vector<int> pts;
		for(unsigned int j=0;j<N[i];j++){
			int pt;
			infile >> pt;
			pts.push_back(pt);
		}
		points.push_back(pts);
	}
	infile.close();
	
	ofstream outfile("/home/hawkwing/Desktop/Problem 2-output-large");
	int numbest[cases];
	for(unsigned int i=0;i<cases;i++){
		vector<int> del;
		numbest[i]=0;
		int numbestp=0;
		for(unsigned int j=0;j<N[i];j++){
			if(points[i][j]/3.0>p[i]-1){
				numbest[i]+=1;
			}
			else if(points[i][j]>0 and points[i][j]/3.0>p[i]-1.5){
				numbestp+=1;
			}
		}
		if(numbestp<S[i]){
			numbest[i]+=numbestp;
		}
		else{
			numbest[i]+=S[i];
		}
		outfile << "Case #" << i+1 << ": " << numbest[i] << endl;
	}
	
	return 0;
}