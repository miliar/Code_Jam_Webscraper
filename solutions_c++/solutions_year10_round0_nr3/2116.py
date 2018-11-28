#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main(){
	freopen("c_small.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int cases;
	cin >> cases;
	for (int casenum=1;casenum<=cases;casenum++){
		int run,carsize,ngroup;
		cin >> run >> carsize >> ngroup;
		vector<int> group;
		for (int i=0;i<ngroup;i++){
			int tmp;
			cin >> tmp;
			group.push_back(tmp);
		}
		int income = 0;
		int curr = 0;
		int sofar = 0;
		int sofarng = 0;
		for (int i=0;i<run;i++){
			while (true){
				if (sofar + group[curr] > carsize || sofarng>=ngroup){
					break;
				}
				sofar += group[curr];
				sofarng++;
				curr++;
				if (curr>=ngroup) curr=0;
			}
			income += sofar;
			sofar = 0;
			sofarng = 0;
		}
		cout << "Case #" << casenum << ": " << income << endl;
	}

}