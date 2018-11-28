#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
using namespace std;

int main()
{
	ifstream ifs("C-small-attempt0.in");
	ofstream ofs("res.out");

	bool a[110];
	int total;
	int rele[10];
	int P, Q;

	int T, caseNo;
	ifs >> T;
	for(int caseNo = 1; caseNo <= T; ++caseNo)
	{
		ifs >> P >> Q;
		for(int i = 0; i < Q; ++i)
			ifs >> rele[i];
		sort(rele, rele + Q);
		int tmp = 0;
		total = 100000000;
		do{
			memset(a, true, sizeof(a));
			for(int i = 0; i < Q; ++i)
			{
				a[rele[i]] = false;
				int k = rele[i]+1;
				while(k <= P && a[k]) ++k, ++tmp;
				k = rele[i]-1;
				while(k > 0 && a[k]) --k, ++tmp;
			}
			if(tmp < total)
				total = tmp;
			tmp = 0;
		}while(next_permutation(rele, rele+Q));
		ofs << "Case #" << caseNo<< ": " << total << endl;
	}

	ifs.close();
	ofs.close();
	
	return 0;
}