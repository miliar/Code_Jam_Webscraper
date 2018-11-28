#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){
	long long t;
	cin>>t;
	long long inci=0;
	while(t--){
		long long one=1;
		long long n,k,ret=0;
		cin>>n>>k;
		inci++;
		for(int i=0;i<n;i++){
			if((one<<i) & k)
				ret++;
		}
		if(ret==n){
			cout<<"Case #"<<inci<<": ON"<<endl;
		}
		else
			cout<<"Case #"<<inci<<": OFF"<<endl;
	}
	return 0;
}