#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int T, nCase=1;
string N, nextN;

int main(){
	cin>>T;
	while(T-->0){
		cin>>N;
		nextN = N;
		next_permutation(nextN.begin(), nextN.end());
		printf("Case #%d: ", nCase++);
		if(nextN<=N){
			N = N+"0";
			sort(N.begin(), N.end());
			for(int i=0;true;i++){
				if(N[i]!='0'){
					swap(N[0], N[i]);
					break;
				}
			}
			cout<<N<<endl;
		}
		else cout<<nextN<<endl;
	
	}
    return 0;
}

