#include <iostream>
#include <fstream>
#include <utility>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

double minexpect(vector<double>& prob, int A, int B);

int main() {
	ifstream infile("A-small-attempt0.in");
	ofstream outfile("A-small-out0.in");

	int T;
	infile >> T;

	for(int i=0;i<T;i++) {
		int A,B;
		infile >> A >> B;
		vector<double> prob;
		for(int j=0;j<A;j++) {
			double x;
			infile >> x;
			prob.push_back(x);
		}
		double fin;
		fin = minexpect(prob, A, B);
		outfile << fixed;
		outfile << "Case #" << i+1 << ": " << setprecision(6) << fin << endl;


	}


	return 0;
}

double minexpect(vector<double>& prob, int A, int B) {
	double keep, back1, back2, enterr;
	double last, seclast;
	int size;
	size = prob.size();
	if(size==0)
		return double(B+1);
	last = prob[size-1];
	if(size>=2) {
		seclast = prob[size-2];
	}
	//keep typing
	double all=1;
	for(int k1=0;k1<size;k1++) {
		all = all*prob[k1];
	}
	keep = (B-A+1)*all + (1.0-all)*(B-A+1+1+B);
	//backspace once
	double once = (all/last)*(1.0-last);
	back1 = (all+once)*(B-A+1+2) + (1.0-all-once)*(B-A+1+1+B+2);

	//backspace twice
	if(size>=2) {
		double twice = ((all/last)/seclast)*(1.0-last)*(1.0-seclast);
		back2 = (all+once+twice)*(4+B-A+1) + (1.0-all-once-twice)*(4+B-A+1+B+1);
	}
	else {
		back2 = 2.0 + B + 1.0;
	}

	//enter straightaway
	enterr = B+2;

	//compare
	if(keep<back1 && keep<back2 && keep<enterr)
		return keep;
	else if(back1<keep && back1<back2 && back1<enterr)
		return back1;
	else if(back2<keep && back2<back1 && back2<enterr)
		return back2;
	else
		return enterr;


}