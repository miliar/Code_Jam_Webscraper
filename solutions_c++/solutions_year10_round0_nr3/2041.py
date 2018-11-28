#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<deque>
#include<string>
#include<cctype>
#include<cmath>
#include<sstream>
#include<numeric>
#include<complex>
#include<queue>
using namespace std;

#define big long long
big R, K, N, arr[10000];
int iterationOfIndex[10000];
big accum[10000];

int main(){

//	freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
//	freopen("C-small-attempt0.in", "rt", stdin);
//	freopen("C-small-attempt0.out", "wt", stdout);
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);

	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){
		cin >> R >> K >> N;
		for(int i = 0 ; i < N ; i++)
			cin >> arr[i];

		memset(iterationOfIndex, -1, sizeof iterationOfIndex);
		memset(accum, 0, sizeof accum);

		int itr = 0, pos = 0;
		bool cycle = false;
		big res = 0;
		for(itr = 0 ; itr < R ; itr++){

			iterationOfIndex[pos] = itr;

			big current = 0;
			int pp = pos;
			while(true){
				if(current + arr[pp] > K)break;
				current+=arr[pp];
				pp = (pp+1)%N;
				if(pp == pos)
					break;
			}
			pos = pp;

			accum[itr] = current;
			if(itr)accum[itr]+=accum[itr-1];

			if(iterationOfIndex[pos] != -1){
				cycle = true;

				int idx = iterationOfIndex[pos];
				big clength = itr-idx+1;
				big ccost = idx ? accum[itr]-accum[idx-1] : accum[itr];
				big remainingIterations = R-idx;
				big ncycles = remainingIterations/clength;

				//precycle
				res = idx ? accum[idx-1] : 0;
				//cycles
				res += ncycles*ccost;
				//postcycle
				int postCylceIterations = remainingIterations%clength;
				if(postCylceIterations)
					res += idx ? accum[idx+postCylceIterations-1]-accum[idx-1] : accum[idx+postCylceIterations-1];

//				cout << "cylce details: " << clength << " " << ccost << " " << remainingIterations << " " << ncycles << " " << postCylceIterations << endl;

				break;
			}
		}

		cout << "Case #" << t+1 << ": ";
		if(!cycle){
			cout << accum[R-1] << endl;
		}else{
			cout << res << endl;
		}

	}

	return 0;
}
