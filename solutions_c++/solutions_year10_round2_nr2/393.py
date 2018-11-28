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
int n, k, b, t;
vector <long long> vpos;
vector <long long> vpostime;
void doit(){
	int val, inx;
	double dval, dspeed;
	cin>>n>>k>>b>>t;
	vpos.clear();vpostime.clear();
	for(int i=0;i<n;i++){
		cin>>val;
		vpos.push_back(val);
	}
	for(int i=0;i<n;i++){
		cin>>val;
		val*=t;
		vpostime.push_back(vpos[i]+val);
	}
	val=0;
	for(inx=n-1;inx>=0;inx--){
		if(vpostime[inx]>=b)val++;
		if(val>=k)break;
	}
	if(val<k){
		cout<<"IMPOSSIBLE"<<endl;
		return;
	}
	val=0;
	for(int i=inx;i<n;i++)
	if(vpostime[i]>=b){
		for(int j=i+1;j<n;j++){
			if(vpostime[j]<b)val++;
		}
	}
	cout<<val<<endl;
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

