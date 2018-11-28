//Arash Rouhani

#include "allincludes.h"

int main(){
	int T;
	cin >> T;
	sfor(int, testcase, 1, T+1){
		string s;
		cin >> s;
		vector <LL> lookup(255, -1);
		int uq = 1;
		lookup[s[0]] = 1;
		sfor(int, i, 1, s.length()){
			if(lookup[s[i]]==-1){
				if(uq==1)
					lookup[s[i]] = 0;
				else
					lookup[s[i]] = uq;
				uq++;
			}
		}
		uq = max(uq, 2);
		LL sum = 0;

		vector <unsigned long long > product;
		product.push_back(1);
		sfor(int, i, 1, s.length()+1)
			product.push_back(*(product.end()-1)*uq);

		sfor(int, i, 0, s.length()){
			sum+= (unsigned long long)(lookup[s[i]] * product[s.length()-i-1]);
		}

		cout << "Case #" << testcase << ": " << sum << endl;

	}
}







