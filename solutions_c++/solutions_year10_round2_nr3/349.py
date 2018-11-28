#include <sstream>
#include <set>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cstdio>
#include <map>
using namespace std;

int solve(int n){
	int res = 0;
	for(int nmask = 0; nmask < (1 << n); nmask++) if((nmask & 1) == 0){
		int mask = nmask | (1 << n);
		//if(n == 4) cout << mask <<endl;
		int pivot = n;
		while(true){
			//cout << n << " " << mask << " " << pivot <<endl; 
			int index = 0;
			for(int j = 0; j <= n; j++)
				if(mask & (1 << j)){
					if(j == pivot) break;
					index++;
				}
			if(index == 0){
				res++;
				break;
			}else if((mask & (1 << index)) == 0)
				break;
			pivot = index;
		}	
	}
	return res;
}

int main(){
	//for(int n = 1; n <= 24; n++){
	//	cout<<"res["<<n + 1<<"] = "<< solve(n) % 100003<<";"<<endl;
	//}
	int T; cin >> T;
	int res[26];
	res[2] = 1;
res[3] = 2;
res[4] = 3;
res[5] = 5;
res[6] = 8;
res[7] = 14;
res[8] = 24;
res[9] = 43;
res[10] = 77;
res[11] = 140;
res[12] = 256;
res[13] = 472;
res[14] = 874;
res[15] = 1628;
res[16] = 3045;
res[17] = 5719;
res[18] = 10780;
res[19] = 20388;
res[20] = 38674;
res[21] = 73562;
res[22] = 40265;
res[23] = 68060;
res[24] = 13335;
res[25] = 84884;


	for(int tt = 1; tt <= T; tt++){
		int n; cin >> n;
		cout <<"Case #"<<tt<<": "<<res[n] << endl;
	}
}
