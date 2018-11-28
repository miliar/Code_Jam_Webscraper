#include "stdafx.h"
#include <iostream>
#include <vector>
using namespace std;

int main(){
	freopen("test.txt", "r", stdin);
	freopen("result.txt", "w", stdout);
	int T, N, S, p, i, su, result;

	cin>>T;
	for(i = 1; i <= T; i++){
		result = 0;
		su = 0;
		cin>>N>>S>>p;
		for(int j = 0; j < N; j++){
			int tmp;
			cin>>tmp;
			if(tmp >= 3 * p - 2){
				result++;
			}
			else if(tmp >= 3 * p - 4 && tmp >= p){
				su++;
			}
		}
		result = result + ((su > S) ? S : su);

		cout<<"Case #"<<i<<": "<<result<<endl;
	}

	return 0;
}
