#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

long long arr[258];
long long prv[258];

int main(){
	int t;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin >> t;
	for (int I=0; I<t; I++){
		cout << "Case #" << I+1 << ": ";
		memset(arr,0, sizeof arr);
		memset(prv,0, sizeof prv);
		int N, in, del, prev, tec, M;
		cin >> del >> in >> M >> N;

		for (int i=0; i<N; i++){
			cin >> tec;
			// delete
			for (int j=0; j<256; j++){
				arr[j] = prv[j] + del;
			}
			// move + add
			for (int j=0; j<256; j++){
				if (M){
					for (int k=0; k<256; k++){
						arr[j] = min(arr[j], prv[k] + (((abs(j - k)-1)< 0 ? 0 : (abs(j - k)-1))/M)*in + abs(tec - j));
					}
				} else {
					arr[j] = min(arr[j], prv[j] + abs(tec - j));
				}
			}
			memcpy(prv, arr, sizeof arr);
		}
		long long ret = 1<<30;
		for (int i=0; i<256; i++){
			ret = min(ret, prv[i]);
		}
		cout << ret << endl;
	}
	return 0;
}