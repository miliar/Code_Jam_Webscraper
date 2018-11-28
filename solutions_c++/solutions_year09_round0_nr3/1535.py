#include <vector>
#include <string>
#include <map>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <set>
#include <numeric>
#include <stdio.h>

using namespace std;

#define SZ(A) A.size()
#define ALL(A) A.begin(), A.end()
#define SORT(A) sort(ALL(A))
#define REP(I,N) for(int I=0, I<N ; I++)
#define INF INT_MAX
#define PB push_back


int main(){

	int n = 0;
	cin >> n;
	string word = "welcome to code jam";
	cin.ignore(1,'\n');
	for(int t=0 ; t<n ; t++){
		
		vector<int> f(SZ(word),0);
		vector<int> s(SZ(word),0);

		string sent;
		getline(cin, sent);

		for(int i=0 ; i<SZ(sent) ; i++){
			f = s;
			for(int j=0 ; j<SZ(word) ; j++){
				if(word[j] == sent[i]){
					if(j==0)
						s[j]++;
					else
						s[j] = (f[j-1]+f[j]) % 10000;
				}
			}
		}

		int ret = s[SZ(word)-1] % 10000;

		cout << "Case #" << t+1 << ": ";
		printf("%04d\n", ret);
	}

	return 0;
}
