/*
CodeJam Round Q Prob A
*/

#include <iostream>
#include <fstream>
#include <ctype.h>
#include <string>
#include <math.h>
#include <vector>

using namespace std;

int main(){
	ifstream infile;
	ofstream outfile;
	infile.open ("input.in");
	outfile.open ("output.out");
	unsigned long long cases, r, k, n, g, money, space, cnt;
	//r,k,n,g,groups
	vector<int> groups;

	infile>>cases;

	for (int cnt2 = 0; cnt2 < cases; cnt2++){

		infile>>r>>k>>n;

		for (int b = 0; b < n; b++){
			infile>>g;
			groups.push_back(g);
		}

		money = 0;

		for (int a = 0; a < r; a++){

			/*
			if (a == 1000000)
				cout<<"Got here."<<endl;
			*/

			space = k;
			cnt = 0;

			while (cnt < groups.size() && space >= groups.front()){
				space -= groups.front();
				money += groups.front();
				groups.push_back(groups.front());
				groups.erase( groups.begin() );
				cnt++;
			}
		}
		
		groups.clear();

		outfile<<"Case #"<<cnt2+1<<": "<<money<<endl;
	}

	return 0;
}