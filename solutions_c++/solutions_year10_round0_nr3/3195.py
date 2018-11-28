/* Karolis Narkevicius */

#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <queue>

using namespace std;

long long park(int &R, int &k, int &N, queue<int> &g)
{
	long long money = 0, rollercoaster, rr;
	int cnt, cnt2 = 0, temp;

	for (rr=1; rr<=R; rr++) {
		rollercoaster = 0;
		cnt = N;
		temp = g.front();
		while((rollercoaster+temp)<=k && cnt>0) {
			rollercoaster += temp;
			g.pop();
			g.push(temp);
			cnt--;
			temp = g.front();
			cnt2++;
		}
		money += rollercoaster;
		//if everyone already had 1 ride we break out
		if (cnt2%N==0) {
			break;
		}
	}
	//check if we've reached the break
	if (rr<R) {

		//we'll make R/rr more such identical loops and will make exactly the same amount of money in each
		money *= R/rr;

		//continue for what's left
		for(rr=(R/rr)*rr+1; rr<=R; rr++) {
			rollercoaster = 0;
			cnt = N;
			temp = g.front();
			while((rollercoaster+temp)<=k && cnt>0) {
				rollercoaster += temp;
				g.pop();
				g.push(temp);
				cnt--;
				temp = g.front();
			}
			money += rollercoaster;
		}
	}

	return money;
}

void run(string in, string out) {
	int CASES, R, k, N, temp;

	ifstream infile;
	ofstream outfile;

	infile.open(in);
	outfile.open (out);
	infile >> CASES;
	for (int i=1; i<=CASES; i++) {
		infile >> R;
		infile >> k;
		infile >> N;
		queue<int> g;
		for (int j=0; j<N; j++) {
			infile >> temp;
			g.push(temp);
		}
		//observing the progress
		cout << "Case #" << i << endl;
		outfile << "Case #" << i << ": " << park(R, k, N, g) << endl;	
	}

	infile.close();
	outfile.close();
}

void runLarge() {

}

int main()
{
	run("A-small.in", "A-small.out");
	//run("A-large.in", "A-large.out");
	return 0;
}