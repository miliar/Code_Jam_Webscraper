#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
main(){

	int z;
	cin >> z;
	
	for(int l=1; l<=z; l++){
		int k;
		string S;
		cin >> k >> S;

		vector <int> P;
		for(int i=0; i<k; i++){
			P.push_back(i);
		}
		
		
		int res = 100000000;
		do{
			string tmp = S;
			for(int i=0; i<S.size() / k; i++){
				for(int j=0; j<k; j++){
					tmp[k*i + j] = S[k*i + P[j]];
				}
				//tmp[i] = S[i/k + P[i % k]];			
			}
			int tmpres = 1;
		
			for(int i=1; i<tmp.size(); i++){
				if(tmp[i-1] != tmp[i]) tmpres++;
			}
			
			if(tmpres < res){
			 	res = tmpres;	
			}
			
		
		}while(next_permutation(P.begin(), P.end()));
		
		cout << "Case #" << l << ": " << res << endl; 
	}
		
}
