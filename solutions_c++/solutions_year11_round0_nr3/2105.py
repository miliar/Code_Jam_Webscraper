/*
TASK: A
LANG: C++
*/
#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;
typedef long long ll;
typedef long double ld;
#define sz(x) ((int)(x).size())

int main(){
	freopen("C-large.in","rt",stdin);
	freopen("t_s.out","wt",stdout);
	vector<int>inputV;
	int N;
	scanf("%d",&N);
	int intT = 0;
	
	for (int iii = 1; iii <= N; iii++) {	
		int NN;
                scanf("%d",&NN);
		
		for (int iT = 0; iT < NN; iT++) {
			scanf("%d",&intT);
			inputV.push_back(intT);			
		}
		sort(inputV.begin(), inputV.end());
		int min = 0;
		for (int iT = 1; inputV.size() > 0 && iT < inputV.size(); iT++) {
			min += inputV[iT];			
		}		
		int lab = 0;
		int intTemp = 0;
		for(int iT = 1; iT <= 50; iT++) {		
			for(int jT = 0; jT < NN; jT++) {
				intTemp = (inputV[jT] % 2 + intTemp)%2 ;
				inputV[jT] = inputV[jT]/2;
			}
			if( intTemp != 0){
				lab = 1 ;
				break;
			}						
		}
		if (lab ==0 && intTemp == 0){
			printf("Case #%d: %d\n",iii,min);
		} else {
			printf("Case #%d: NO\n",iii);
		}
		inputV.clear();
	}
	return 0;
}
