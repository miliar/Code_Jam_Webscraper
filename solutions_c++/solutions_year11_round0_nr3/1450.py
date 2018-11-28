#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <string>

using namespace std;
#define INF 10000000
void doit(){
	int n, minval=INF, sum=0, xr=0, tn;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>tn;
		minval=min(minval,tn);
		sum+=tn;
		xr=xr^tn;
	}
	if(xr){
		cout<<"NO"<<endl;
	}
	else{
		cout<<sum-minval<<endl;
	}
	return;
}
int main(){
    int tc;
    cin>>tc;
    for(int i=1;i<=tc;i++){
        cout<<"Case #"<<i<<": ";
        doit();
    }
    return 0;
}
