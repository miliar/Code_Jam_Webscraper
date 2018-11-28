#include <iostream>

#include <vector>
#include <fstream>
using namespace std;
ifstream input("A-small-attempt1.in");
ofstream output("output.out");


bool solve(int n, int pd, int pg) {
	if(pg == 100 && pd != 100)
		return false;
	if(pd == 0 && pg != 100)
		return true;
	else if(pd == 0 && pg == 100)
		return false;
	
	if(pg == 0 && pd == 0)
		return true;
	else if(pg == 0 && pd != 0)
		return false;
	
	int tn = n;
	while(tn >= 1) {
		if(tn * pd % 100 != 0)
			--tn;
		else {
			int x = tn * pd / 100;
			int y = 0;
			while((x+y)*pg % 100 != 0) {
				++y;
			}
			if(x+y >= n)
				return true;
			else
				--tn;
		}
	}
	
	return false;
}

int main (int argc, char * const argv[]) {
	int caseNum;
	input>>caseNum;
	for(int i=0; i<caseNum; ++i) {
		int n, pd, pg;
		input>>n>>pd>>pg;
		
		output<<"Case #"<<i+1<<": ";
		if(solve(n, pd, pg)) {
			output<<"Possible";
		} else 
			output<<"Broken";
		output<<endl;
	}
	
    return 0;
}
