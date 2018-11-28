#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
using namespace std;

int main()
{
	int tCase;
	cin >> tCase;

	for(int _case=1; _case <= tCase; ++_case){
	
		int numPrison, Q;
		scanf("%d %d", &numPrison, &Q);

		int prison;
		vector<int> vP;
		for(int i=0; i < Q; ++i){
			scanf("%d",&prison);
			vP.push_back(prison);
		}
		
		vector<int> allCase;
		for(int i=0; i < Q; ++i) allCase.push_back(i);

		int minGold=0x0fffffff;		
		int leftRel=0;
		int rightRel=Q;		
		
		do{
			vector<bool> cells(numPrison+2);
			int gold=0;
			for(int i=0; i < Q; ++i){
				int p = allCase[i];
				for(int l = vP[p]-1; l > 0 ; --l ) {
					if( cells[l]==false)
						++gold;
					else
						break;
				}
				for(int r = vP[p]+1; r <= numPrison ; ++r ) {
					if( cells[r]==false)
						++gold;
					else
						break;
				}
				cells[ vP[p] ]=true;
			}
			minGold = min(gold, minGold);

		}while( next_permutation(allCase.begin(), allCase.end()) );


		printf("Case #%d: %d\n", _case, minGold);
		
	}
	

	return 0;
}
