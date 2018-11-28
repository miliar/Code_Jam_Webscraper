#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int k;
int n;
string inp;
string perm;

int main(){
	
	int t,lp;
	int i,j;
	int ret,hlp;
	char last;
	vector<int> v;
	
	cin >> t;
	
	for(lp=1;lp<=t;lp++){
		cin >> k;
		cin >> inp;
		v.resize(k);
		for(i=0;i<k;i++) v[i] = i;
		
		n = inp.size();
		perm.resize(n);
		ret = n*n*n;
		
		do{
			for(i=0;i<n/k;i++){
				for(j=0;j<k;j++){
					perm[k*i+j] = inp[k*i+v[j]];
				}
			}
			
			hlp = 1;
			last = perm[0];
			
			for(i=1;i<n;i++){
				if(perm[i] != last){
					last = perm[i];
					hlp++;
				}
			}
			
			ret = min(ret,hlp);
			
			
		}while(next_permutation(v.begin(),v.end()));
		
		printf("Case #%d: %d\n",lp,ret);
		
	}
	
	return 0;
	
}
