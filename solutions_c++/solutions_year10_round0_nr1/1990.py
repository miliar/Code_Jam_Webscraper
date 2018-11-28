#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;



int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int nn;
	cin >> nn;
	for (int test = 1;test <= nn; ++test){
		int n,k;
		cin >> n >> k;
		int tt = 1 << n;
		if (k % tt == (tt-1))
			printf("Case #%i: ON\n",test);
		else
			printf("Case #%i: OFF\n",test);
	}
	
	return 0;
}