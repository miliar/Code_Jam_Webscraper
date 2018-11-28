//============================================================================
// Name        : PickingUpChicks.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;

int main() {
	int ntc;
	cin >> ntc;
	for(int ci=0;ci<ntc;ci++){
		int N,K,B,T;
		cin >> N >> K >> B >> T;
		vector<int>X,V;
		for(int i=0;i<N;i++){
			int tmp;
			cin >> tmp;
			X.push_back(tmp);
		}
		for(int i=0;i<N;i++){
			int tmp;
			cin >> tmp;
			V.push_back(tmp);
		}
		vector<int>swap;
		for(int i=0;i<N;i++){
			int tmp=0;
			if(V[i]*T<B-X[i]){
				swap.push_back(N);
				continue;
			}
			for(int j=i;j<N;j++){
				if(V[j]<V[i]){
					double t=(double)(X[j]-X[i])/(V[i]-V[j]);
					if(t*V[i]+(T-t)*V[j]<B-X[i]){
//						cout << i << j << endl;
						tmp++;
					}
				}
			}
			swap.push_back(tmp);
		}
		sort(swap.begin(),swap.end());
		int result=0;
		bool is_pos=true;
		for(int i=0;i<K;i++){
			result+=swap[i];
			if(swap[i]==N){
				is_pos=false;
				break;
			}
		}
		cout << "Case #" << ci+1 << ": ";
		if(is_pos)
			cout << result;
		else
			cout << "IMPOSSIBLE";
		cout << endl;
	}
	return 0;
}
