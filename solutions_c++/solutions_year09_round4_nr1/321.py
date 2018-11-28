#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <sstream>
#include <iomanip>

using namespace std;
#define x first
#define y second
#define INF 1000000

	
int main(){
	int Tc;
	cin >> Tc;
	for(int tc=1;tc<=Tc;tc++){
		int N;
		cin >> N;
		vector<string> T(N);
		for(int i=0;i<N;i++) cin >> T[i];

		int r=0;
		for(int i=0;i<N;i++){
			for(int j=0;j<T.size();j++){
				int p=0;
				for(int k=0;k<N;k++) if(T[j][k]=='1') p = k;
				if(p <= i){
					r += (j+i)-i;
					T.erase(T.begin()+j);
					break;
				}
			}
		}



		cout << "Case #" << tc << ": "<<r << endl;
	}
}


















