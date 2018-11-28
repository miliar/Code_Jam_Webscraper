#include <iostream>
#include <fstream>
#include <string>
#include <utility>
#include <vector>
#include <cmath>
using namespace std;

void calc(ofstream & outfile,int N,int M,int A){
	for (int x1=0;x1<=N;x1++){
		for (int y1=0;y1<=M;y1++){
			for (int x2=0;x2<=N;x2++){
				for (int y2=0;y2<=M;y2++){
					if (abs(x1*y2-x2*y1)==A){
						outfile<<"0 0 "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<endl;
						return;
					}
				}
			}
		}
	}
	outfile<<"IMPOSSIBLE"<<endl;
}

int main(){
	int C;
	int N;
	int M;
	int A;

	ifstream infile("a.in");
	ofstream outfile("a.out");

	infile>>C;
	for (int i=1;i<=C;i++){
		infile>>N>>M>>A;
		outfile<<"Case #"<<i<<": ";
		calc(outfile,N,M,A);
	}

	return 0;
}